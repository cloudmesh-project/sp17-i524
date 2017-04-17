#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

OutFile = "C:\\Users\\sriram\OneDrive for Business\\Election2016-"
Count=0
Fileno=1
TweetCount=0
out=open(OutFile+str(Fileno)+".txt","w")

#Variables that contains the user credentials to access Twitter API 
access_token = "141817420-ViMO9ic2MuVmjw4u04CACINnCA0MIJEs2uaPbkYX"
access_token_secret = "LWNQKJYkHJnrAjNsH7LnrkKWmnf5qZ9akizidiWjbLhOy"
consumer_key = "SyLwuJP6pzy4FevmLMOmcWdpf"
consumer_secret = "XfZkuRRj5yqVmReRkAVvVFm9t6vaPHVeoXEdg85Iuqb8k524pU"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print (data)
        global Count
        global TweetCount
        global Fileno
        global out
        Count+=1
        TweetCount+=1
        if Count%10000==0:
            #print (Count)
            out.close()
            Count=0
            Fileno+=1
            out=open(OutFile+str(Fileno)+".txt","w")
        if TweetCount%500==0:
            print (TweetCount, " tweets received")
        out.write(data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    OutFile = "C:\\Users\\sriram\OneDrive for Business\\Election2016-"
    Count=1
    Fileno=1
    TweetCount=1
    out=open(OutFile+str(Fileno)+".txt","w")
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(languages=["en"],track=['election2016', 'hilary', 'hillary','trump','republican','democrat','clinton'])