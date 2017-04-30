README
========
 
This Ansible Galaxy project collects realtime twitter streaming data and performs multiple text analysis including
identifying the sentiment of the tweet (using naiveBayes on a spark cluster), finding the top co-occuring word in the tweet
Projecting the sentiment of tweets across US States,etc.

Pre Requisites
================

You are expected to use a Linux machine which has the following packages installed:
- Git
- Cloudmesh Client (and having a valid cloudmesh.yml file for accessing Chameleon Cloud)
- Ansible

You are expected to create API keys in twitter to collect the data from Twitter. This can be achieved using the following steps:
```
1- Log into the Twitter Developers section.If you don't already have an account, you can login with your normal 
Twitter credentials
2- Go to "Create an app"
3- Fill in the details of the application you'll be using to connect with the API
4- Your application name must be unique. If someone else is already using it, you won't be able to register your 
application until you can think of something that isn't being used.
5- Click on Create your Twitter application
6- Details of your new app will be shown along with your consumer key and consumer secret.scroll down and click 
Create my access token.
```
These 2 keys and 2 tokens are necessary to run the Python script that fetches the data from Twitter streaming API.

Ansible Deployment
==================


Visualization
================

Below are the six different visualization that shows the output of the analysis performed. Each of the those can be accessed using the
public ip of the system as shown above each chart. It is necessary that the security groups are updated so that the ports "5025" and "1234"
"1240" can be accessed from the local machine running the ansisble playbooks.

URI: http://public_ip:1234

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/realtime.JPG" alt="Realtime Tweet" width="600" height="449"/>

URI: http://public_ip:1240/US_heat_count

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/us_tweet.JPG" alt="US State Tweet Count" width="600" height="388"/>

URI: http://public_ip:1240/map-pies

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/us_senti.JPG" alt="US State-wise Sentiment" width="600" height="388"/>

URI: http://public_ip:1240/co_occur_new.html

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/cooccur.JPG" alt="Tweet token Co-occurence" width="727" height="727"/>

URI: http://public_ip:1240/dynamic-master-detail

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/timechart.JPG" alt="Total Tweets vs Time" width="800" height="300"/>

URI: http://public_ip:1240/heatmap

<img src="https://github.com/sriramsitharaman/sp17-i524/blob/master/project/S17-IR-P001/Images/senticont.jpeg" alt="Sentiment Heatgrid" width="600" height="401"/>
