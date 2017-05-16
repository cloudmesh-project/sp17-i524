#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
from textblob import TextBlob
from time import strptime
import numpy as np
import re
import time
import zipcode
import sys, errno
from nltk.corpus import stopwords
from itertools import combinations
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
nltk.download('stopwords')

runCount=0
#Variables that contains the user credentials to access Twitter API 
access_token = "141817420-ViMO9ic2MuVmjw4u04CACINnCA0MIJEs2uaPbkYX"
access_token_secret = "LWNQKJYkHJnrAjNsH7LnrkKWmnf5qZ9akizidiWjbLhOy"
consumer_key = "SyLwuJP6pzy4FevmLMOmcWdpf"
consumer_secret = "XfZkuRRj5yqVmReRkAVvVFm9t6vaPHVeoXEdg85Iuqb8k524pU"

tweets_data = []

stop = stopwords.words('english') + ['and']
emoticons_str = r"""
	(?:
		[:=;] # Eyes
		[oO\-]? # Nose (optional)
		[D\)\]\(\]/\\OpP] # Mouth
	)"""
 
regex_str = [
	emoticons_str,
	r'<[^>]+>', # HTML tags
	r'(?:@[\w_]+)', # @-mentions
	r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
	r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
	r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
	r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
	r'(?:[\w_]+)', # other words
	r'(?:\S)' # anything else
]
	
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
Count=0
stop = stopwords.words('english')

def create_dataframe(tweets_data):
	tweets = pd.DataFrame(index=range(len(tweets_data)), 
	columns=['text','created_at','location','state','sentiment','sentiment_cat','country_code','hour'])
	
	for i in range(len(tweets_data)):
		try:
			tweets['text'][i] = tweets_data[i]['text']
		except:
			tweets['text'][i] = ""
		try:
			tweets['location'][i]=tweets_data[i]['user']['location']
		except:
			tweets['location'][i]='NA'
		try:
			tweets['country_code'][i]=tweets_data[i]['place']['country_code']
		except:
			tweets['country_code'][i]=''
		try:
			lon=tweets_data[i]['place']['bounding_box']['coordinates'][0][0][0]
		except:
			lon='NA'
		try:
			lat=tweets_data[i]['place']['bounding_box']['coordinates'][0][0][1]
		except:
			lat='NA'
		#print (lat,lon)
		try:
			tweets['created_at'][i]=tweets_data[i]['created_at']
		except:
			tweets['created_at'][i]='NA'
		try:
			tweets['hour'][i]=tweets['created_at'][i][11:13]
		except:
			tweets['hour'][i]='NA'
		try:
			stateFromData=tweets['location'][i].split(',')[1]
		except:
			stateFromData=''
		if len(stateFromData)==2:
			tweets['state'][i]=stateFromData
		else:
			if lat!='NA':
				radius=10
				incre=10
				zips=zipcode.isinradius((lat,lon),radius)
				while len(zips)==0:
					radius=radius+incre
					zips=zipcode.isinradius((lat,lon),radius)
					incre=incre+10
				myzip = zipcode.isequal(str(zips[0].zip))
				tweets['state'][i]=myzip.state
			else:
				tweets['state'][i]='NA'	
		blob = TextBlob(tweets['text'][i])
		try:
			sentence=blob.sentences[0]
			tweets['sentiment'][i]=float(sentence.sentiment.polarity)
		except:
			tweets['sentiment'][i]=0	 
		if tweets['sentiment'][i] < 0:
			tweets['sentiment_cat'][i] = 'Neg'
		else:
			if tweets['sentiment'][i] > 0:
				tweets['sentiment_cat'][i] = 'Pos'
			else:
				tweets['sentiment_cat'][i] = 'Neu'
	print (tweets.head())
	return tweets
	
def state_senti(newFolder,usStateSentiOld,tweetsFinal):

    output2=pd.DataFrame({'value' : tweetsFinal.groupby( [ "State","sentiment_cat"] ).size()}).reset_index()

    outData=pd.pivot_table(output2,values='value', index=['State'], columns=['sentiment_cat'], aggfunc=np.sum)
    outData=outData.fillna(0)
    outData['State']=outData.index
    #outData.reset_index()
    print (outData.columns.values)
    outData = pd.merge(usStateSentiOld, outData,  how='left', left_on='State', right_on = 'State')
    outData=outData.fillna(0)
    outData['Pos']=outData['Pos_x']+outData['Pos_y']
    del outData['Pos_x']
    del outData['Pos_y']
    outData['Neg']=outData['Neg_x']+outData['Neg_y']
    del outData['Neg_x']
    del outData['Neg_y']
    outData['Neu']=outData['Neu_x']+outData['Neu_y']
    del outData['Neu_x']
    del outData['Neu_y']
    outData.to_csv(newFolder+"usStates-SentiCount.csv",index=False)
    #-------------------------------------------
    try:
        outData['sum']=outData[['Neg', 'Neu', 'Pos']].sum(axis=1)
        outData['max']=outData['maxFinal']=outData[['Neg', 'Neu', 'Pos']].idxmax(axis=1)
    except:
        outData['sum']=outData[['Neu', 'Pos']].sum(axis=1)
        outData['max']=outData['maxFinal']=outData[[ 'Neu', 'Pos']].idxmax(axis=1)
    #-------------------------------------------
    for i in range(len(outData)):
        if outData['max'][i] =="Pos":
            outData['maxFinal'][i] = '1'
        else:
            if outData['max'][i] =="Neu":
                outData['maxFinal'][i] = '-1'
            else:
                outData['maxFinal'][i] = '2'
    
    del outData['max']

    d="var data =[\n"
    for i in range(len(outData)):
        row=outData.ix[i]
        #print (row)
        d += "[\'"+row['State']+"\',"+",".join([str(i) for i in row[:5]])+"],\n"
    
    return d+']'
    


def create_timechart(newFolder,oldtimedata,tweets):
    td1 = pd.DataFrame({'value' : tweets.groupby( [ "created_at"] ).size()}).reset_index()
    td1['created_at'] = td1['created_at'].astype('str')
    mask = (td1['created_at'].str.len() > 2)
    td1=td1.loc[mask]
    timedata = td1[td1.created_at != 'NA']
    timedata=oldtimedata.append(timedata, ignore_index=True)
    timedata.to_csv(newFolder+"timeseries.csv",index=False)
    data1 ={}
    data = ["var data=["]
    for i in range(0,len(timedata)):
    
        year = timedata['created_at'][i][-4:]
        if (timedata['created_at'][i][4:7] == 'Jan'):
            mon = '1'
        else:
            if (timedata['created_at'][i][4:7] == 'Feb'):
                mon = '2'
            else:
                if (timedata['created_at'][i][4:7] == 'Mar'):
                    mon = '3'
                else:
                    if (timedata['created_at'][i][4:7] == 'Apr'):
                        mon = '4'
                    else:
                        if (timedata['created_at'][i][4:7] == 'May'):
                            mon = '5'
                        else:
                            if (timedata['created_at'][i][4:7] == 'Jun'):
                                mon = '6'
                            else:
                                if (timedata['created_at'][i][4:7] == 'Jul'):
                                    mon = '7'
                                else:
                                    if (timedata['created_at'][i][4:7] == 'Aug'):
                                        mon = '8'
                                    else:
                                        if (timedata['created_at'][i][4:7] == 'Sep'):
                                            mon = '9'
                                        else:
                                            if (timedata['created_at'][i][4:7] == 'Oct'):
                                                mon = '10'
                                            else:
                                                if (timedata['created_at'][i][4:7] == 'Nov'):
                                                    mon = '11'
                                                else:
                                                    mon = '12'
        date = timedata['created_at'][i][7:10]
        hour = timedata['created_at'][i][10:13]
        minu = timedata['created_at'][i][14:16]
        sec = timedata['created_at'][i][17:20]
        value = timedata['value'][i]
        data1 = ("[Date.UTC("+str(year)+","+str(mon)+","+str(date)+","+str(hour)+","+str(minu)+","+str(sec)+"),"+str(value)+"]")
        if (len(timedata)):
            data.append
        data.append(data1)
    data = ",\n".join(data)+"\n]"
    data = data.replace("[,","[")
    return data

	
def tokenize(s):
	tokens=tokens_re.findall(s)
	return [ x for x in tokens if 'http' not in x and len(x)>1 and x.lower() not in stop]
 
def preprocess(s, lowercase=True):
	tokens = tokenize(s)
	if lowercase:
		tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
	return tokens

def collect_pairs(lines):
	pair_counter = Counter()
	for line in lines:
		unique_tokens = sorted(set(line))  # exclude duplicates in same line and sort to ensure one word is always before other
		combos = combinations(unique_tokens, 2)
		pair_counter += Counter(combos)
	return pair_counter
#Co-occurrence:
def co_occur(tweets):
	t2 = []
	t1 =tweets['text']
	for t in range(len(t1)):
		t2.append(preprocess(t1[t]))			 
	pairs = collect_pairs(t2)
	top_pairs = pairs.most_common(200)
	nodes={}
	links=["\"links\":["]
	count =0
	len_top=len(top_pairs)
	nptp = np.array(top_pairs)
	maxtp = np.max(nptp[:,1])
	for p in range(len(top_pairs)):
		for i in range(2):
			if top_pairs[p][0][i] not in nodes:
				nodes[top_pairs[p][0][i]] = count
				count+=1
		link="{ \"source\":"+str(nodes[top_pairs[p][0][0]])+",\"target\":"+str(nodes[top_pairs[p][0][1]])+",\"value\":"+str(round(top_pairs[p][1]*10/maxtp))+"}"
		links.append(link)
	links=",\n".join(links)+"\n]"
	links=links.replace("[,","[")
	nodes = sorted(nodes.items(), key=lambda x: x[1])
	nodes1=["\"nodes\":["]
	for p in range(len(nodes)):
		nodes1.append("{ \"name\":\""+nodes[p][0]+"\",\"group\":"+"0}")
	nodes1=",\n".join(nodes1)+"\n]"
	nodes1=nodes1.replace("[,","[")
	
	return nodes1,links

def heatworldgrid(newFolder,worldOld,tweets):
    contdata=pd.read_csv("continents.txt")
    contdat=contdata.fillna("NA")
    tweets['sentiment']=tweets['sentiment'].apply(pd.to_numeric)
    #print (tweets.dtypes)
    
    Countryhour=pd.DataFrame({'sentiment' : tweets.groupby( ["country_code","hour"] )['sentiment'].mean()}).reset_index()
    final=pd.merge(Countryhour, contdata, how='left',left_on="country_code",right_on="country")
    print (final.columns.values)
    del final['country']
    #del final['Unnamed: 0']
    del final['country_code']
    
    Conthour=pd.DataFrame({'sentiment' : final.groupby( ["continent","hour"] )['sentiment'].mean()}).reset_index()
    Conthour = pd.merge(worldOld, Conthour,  how='left', left_on=["continent","hour"] , right_on = ["continent","hour"] )
    Conthour=Conthour.fillna(0)
    Conthour['sentiment']=(Conthour['sentiment_x']*1000000+Conthour['sentiment_y']*10000)/(1010000)

    del Conthour['sentiment_x']
    del Conthour['sentiment_y']
    Conthour.to_csv(newFolder+"Continent-hour-senti.csv",index=False)
    minVal=min(Conthour['sentiment'])
    maxVal=max(Conthour['sentiment'])
    outputStr=""
    uniqueCont= list(np.unique(Conthour['continent']))
    outputStr+="var continent =["+",".join(["'"+i+"'" for i in uniqueCont])+"];\n"
    numCont=len(uniqueCont)
    numHour=24
    
    outputStr+="var hour =["+",".join(["'"+str(i)+"'" for i in range(numHour)])+"];\n"
    outMatrix=np.zeros(shape=(numCont,numHour))
    outputStr+="var data=["
    datastr=[]
    for i in range(len(Conthour)):
        continent=Conthour['continent'][i]
        hour=Conthour['hour'][i]
        contIndex=uniqueCont.index(continent)
        outMatrix[contIndex][int(hour)]=Conthour['sentiment'][i]
        
        
    for i in range(numCont):
        for j in range(numHour):
            datastr.append("["+str(j)+","+str(i)+","+str(int(outMatrix[i][j]))+"]")


    outputStr+=",".join(datastr)+"]; var minval = "+str(minVal)+";\n var maxval = "+str(maxVal)+";"
    
    return outputStr


def createwordcloud(tweets):  
	# Read the whole text.
	#text = open(path.join(d, 'constitution.txt')).read()
	textpos = tweets[tweets.sentiment_cat == 'Pos']
	textneg = tweets[tweets.sentiment_cat == 'Neg']
	
	postweets=""
	for i in textpos.index.values:
		postweets+=textpos['text'][i]+" "
	negtweets=""
	for i in textneg.index.values:
		negtweets+=textneg['text'][i]+" "
	
	textp = preprocess(postweets)
	textp=" ".join(textp)
	textn = preprocess(negtweets)
	textn=" ".join(textn)
	wordcloudp = WordCloud( stopwords=stop,background_color='white',width=1200,height=1000).generate(textp)
	wordcloudn = WordCloud( stopwords=stop,background_color='white', width=1200,height=1000).generate(textn)
	image1 = wordcloudp.to_image()
	image2= wordcloudn.to_image()
	image1.save("wordcloup.png")
	image2.save("wordcloudn.png")

	
def analyze(tweets_data):
	oldFolder="Data\\"
	outputFolder="OutputJS\\"
	newFolder="NewData\\"

	#Dataframe is created from the list of json tweets, sentiment is also calculated
	tweets=create_dataframe(tweets_data)
	statedata=pd.read_csv(oldFolder+"states.csv")
	tweetsFinal=pd.merge(tweets, statedata, how='left',left_on="state",right_on="Abbreviation")

	#UsStatewise Tweets
	usStateOld=pd.read_csv(oldFolder+"usStatesCount.csv")
	usState=pd.DataFrame({'value' : tweetsFinal.groupby( [ "State"] ).size()}).reset_index()
	usState_new = pd.merge(usStateOld, usState,  how='left', left_on='State', right_on = 'State')
	usState_new=usState_new.fillna(0)
	usState_new['value']=usState_new['value_x']+usState_new['value_y']
	del usState_new['value_x']
	del usState_new['value_y']
	usState_new.to_csv(newFolder+"usStatesCount.csv",index=False)
	print (usState_new.head())
	usStateJson=usState_new.to_json(orient = "records")
	usStateJsonfinalOutput=usStateJson[33:len(usStateJson)-1].upper().replace("\"STATE\"","ucName").replace("\"VALUE\"","value")
	with open(outputFolder+'usStates-tweetCount.json', 'w') as outfile:
		outfile.write(usStateJsonfinalOutput)
	
	
	#UsStatewise Sentiment
	usStateSentiOld=pd.read_csv(oldFolder+"usStates-SentiCount.csv")
	statesentiout=state_senti(newFolder,usStateSentiOld,tweetsFinal)
	with open(outputFolder+'usStates-SenitCount.js', 'w') as outfile:
		outfile.write(statesentiout)
	
	#TimeSeries Chart
	timeOld=pd.read_csv(oldFolder+"timeseries.csv")
	timedata=create_timechart(newFolder,timeOld,tweets)
	with open(outputFolder+'tweet_cnt-1.js', 'w') as outfile:
		outfile.write(timedata)

	
	#Co-occur Chart
	nodes1,links=co_occur(tweets)
	with open(outputFolder+'cooccur_word-1.json', 'w') as outfile:
		outfile.write("{\n"+nodes1+",\n"+links+"}\n")
		
	#Heat World Grid
	worldOld=pd.read_csv(oldFolder+"Continent-hour-senti.csv")
	heatjson=heatworldgrid(newFolder,worldOld,tweets)
	with open(outputFolder+'heatchart_data-1.js', 'w') as outfile:
		outfile.write(heatjson)
	#WordCloud
	createwordcloud(tweets)
	
#This is a basic listener that just prints received tweets to stdout.

class StdOutListener(StreamListener):

	def on_data(self, data):
		global Count,tweets_data
		Count+=1
		#TweetCount+=1
		if Count%1000==0:
			print ("Analyze data started")
			x=time.time()
			analyze(tweets_data)
			print ("Analyze data Completed in ", time.time()-x)
			sys.exit(errno.EACCES)
			tweets_data=[]
			Count=0
		tweet = json.loads(data)
		tweets_data.append(tweet)
		return True

	def on_error(self, status):
		print (status)

if __name__ == '__main__':

	#This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)

	#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	stream.filter(languages=["en"],track=['a', 'e', 'i','o','u','#'])