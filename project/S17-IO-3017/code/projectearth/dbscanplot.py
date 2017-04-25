from pymongo import MongoClient
import requests
import time

import dblayer

from sklearn.cluster import DBSCAN

import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import random

# Create random colors in list
color_list = []
def generate_color(ncluster):
    for i in range(ncluster):
        color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(ncluster)))
        color_list.append(color)

def showLatLongInCluster(data):

    # Run the DBSCAN from sklearn
    dbscan = DBSCAN(eps=2, min_samples=5, metric='euclidean', algorithm='auto').fit(data)

    cluster_labels = dbscan.labels_
    n_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
    generate_color(n_clusters)

    plot_data = []
    # get the cluster
    for i in range(n_clusters):
        ds = data[np.where(cluster_labels == i)]
        clustername = "Cluster " + str(i + 1)

        trace = go.Scattergeo(lon=ds[:,0], lat=ds[:,1],mode='markers',marker=dict(color=color_list[i], size=5),
                              name=clustername)
        plot_data.append(trace)

        layout = go.Layout(showlegend=False, title='Earthquakes In North and South America',
                           titlefont=dict(family='Courier New, monospace',size=20,color='#7f7f7f'),
                            geo=dict(scope=('north america', 'south america'),
                                projection=dict(type='orthographic'),
                                showland=True, landcolor='#191919',
                                showcountries=True,
                                showocean=True, oceancolor='rgb(217,217,255)',
                                showframe=False,

                                ),
                               xaxis=dict(showgrid=False, zeroline=False),
                               yaxis=dict(showgrid=False, zeroline=False))

    fig = go.Figure(data=plot_data, layout=layout)
    #plotly.offline.plot(fig, filename='lat_long.html')
    div = plotly.offline.plot(fig, include_plotlyjs=True, output_type='div')

    return div

def mkLatLong():

    #### TME: Get start time
    start_time = time.time()
    ####
    sess = requests.Session()
    dbobj=dblayer.classDBLayer()
    projection = [{"$project": {"_id": 0, "mag": "$properties.mag",
                             "depth": {"$arrayElemAt": ["$geometry.coordinates", 2]},
                             "longitude": {"$arrayElemAt": ["$geometry.coordinates", 0]},
                             "latitude": {"$arrayElemAt": ["$geometry.coordinates", 1]}}}]

    df = pd.DataFrame(list(dbobj.doaggregate(projection)))
    df = df[['longitude', 'latitude']].copy()

    #### TME: Elapsed time taken to read data from MongoDB
    elapsed = time.time() - start_time
    line = "=" * 60
    print (line)
    print ("Reading Longitude and Latitude")
    print(str(elapsed) + " secs required to read " + str(df['latitude'].count()) + " records from database.")
    print (line)
    ###

    #### TME: Get start time
    start_time = time.time()
    ####

    div = showLatLongInCluster(df.values)
    response = """<html><title></title><head><meta charset=\"utf8\"> </head> <body>""" + div + """</body> </html>"""

    dbobj.closedb()

    #### TME: Elapsed time taken to cluster and plot data
    elapsed = time.time() - start_time
    line = "=" * 60
    print (line)
    print ("Applying DBSCAN clustering and plotting its output")
    print("Time taken: " + str(elapsed))
    print (line)
    ###

    return response



#sess = requests.Session()
# mkLatLong()
# client.close()
