import random
import string
import getusgsdata as usgs
import kmeansplot as kplot
import dbscanplot as dbplot

import cherrypy

class usgsdataanalysis(object):
    @cherrypy.expose
    def index(self):
        response = "Application usage: <br/><br/>"
        response = response + "1. Click <a href=\"/getdata\">getdata</a> method to download data.<br/>"
        response = response + "2. Click <a href=\"/plotmag\">plotmag</a> method to view earthquakes magnitude on scatter plot.<br/>"
        response = response + "3. Click <a href=\"/plotlatlong\">plotlatlong</a> method to view lat long plot.<br/>"
        return response

    @cherrypy.expose
    def getdata(self):
        return usgs.doGetData()

    @cherrypy.expose
    def plotmag(self):
        return kplot.mkMag()

    @cherrypy.expose
    def plotlatlong(self):
        return dbplot.mkLatLong()

if __name__ == '__main__':
    cherrypy.config.update({"server.socket_host":"0.0.0.0","server.socket_port":8081})
    cherrypy.quickstart(usgsdataanalysis())
