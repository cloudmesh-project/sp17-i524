README
========
 
This Ansible Galaxy project collects realtime twitter streaming data and performs multiple text analysis likeon
identifying the sentiment of the tweet (using naiveBayes on a spark cluster), finding the top co-occuring word in the tweet
Projecting the sentiment of tweets across US States,etc.

Requirements
================

You are expected to use a Linux machine which has the following packages installed:
- Git
- Cloudmesh Client (and having a valid cloudmesh.yml file for accessing Chameleon Cloud)
- Ansible

You are expected to create API keys in twitter to collect the data from Twittr. This can be achieved using the following steps:
```
1- Log into the Twitter Developers section.If you don't already have an account, you can login with your normal Twitter credentials
2- Go to "Create an app"
3- Fill in the details of the application you'll be using to connect with the API
4- Your application name must be unique. If someone else is already using it, you won't be able to register your application until you can think of something that isn't being used.
5- Click on Create your Twitter application
6- Details of your new app will be shown along with your consumer key and consumer secret.scroll down and click Create my access token.

```
These 2 keys and 2 tokens are necessary to run the Python script that fetches the data from Twitter streaming API.
================
