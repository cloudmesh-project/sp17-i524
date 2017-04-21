from pymongo import MongoClient
import requests
import time

import dblayer

import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import random
from sklearn.cluster import KMeans

NUM_CLUSTER = 3

def generate_color():
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(NUM_CLUSTER)))
    return color

# Create random colors in list
color_list = []
for i in range(NUM_CLUSTER):
    color_list.append(generate_color())

def showMagnitudesInCluster(data):
    kmeans = KMeans(n_clusters=NUM_CLUSTER)
    kmeans.fit(data)

    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    plot_data = []

    for i in range(NUM_CLUSTER):
        ds = data[np.where(labels == i)]
        clustername = "Cluster " + str(i+1)

        trace = go.Scatter(x=ds[:, 0], y=ds[:, 1], mode='markers', showlegend='false', name=clustername, marker=dict(size=5, color=color_list[i]))
        plot_data.append(trace)

        # plot the centroids
        trace = go.Scatter(x=centroids[i, 0], y=centroids[i, 1], mode='markers', marker=dict(size=10, color='black'))
        plot_data.append(trace)

    layout = go.Layout(title='Magnitude Vs. Depth - K-Means Clusters', titlefont=dict(family='Courier New, monospace',size=20,color='#7f7f7f'),
                       xaxis=dict(title='Depth of Earthquake', titlefont=dict(family='Courier New, monospace',size=18,color='#7f7f7f')),
                       yaxis=dict(title='Magnitude',titlefont=dict(family='Courier New, monospace',size=18,color='#7f7f7f'))
                       )

    fig = go.Figure(data=plot_data, layout=layout)
    #plotly.offline.plot(fig, filename='mag_depth.html')
    div = plotly.offline.plot(fig, include_plotlyjs=True, output_type='div')

    return div

def mkMag():
    #### TME: Get start time
    start_time = time.time()
    ####
    sess = requests.Session()
    dbobj = dblayer.classDBLayer()

    projection = [
        {"$project": {"_id": 0, "mag": "$properties.mag", "depth": {"$arrayElemAt": ["$geometry.coordinates", 2]}}}]

    #dframe_mag = pd.DataFrame(list(dbobj.doaggregate(projection)))
    dframe_mag = pd.DataFrame(list(dbobj.doaggregate(projection)))

    #### TME: Elapsed time taken to read data from MongoDB
    elapsed = time.time() - start_time
    line = "=" * 60
    print (line)
    print ("Reading Magnitude and Depth data")
    print(str(elapsed) + " secs required to read " + str(dframe_mag['depth'].count()) + " records from database.")
    print (line)
    ####

    #### TME: Get start time
    start_time = time.time()
    ####
    div = showMagnitudesInCluster(dframe_mag.values)
    response = """<html><title></title><head><meta charset=\"utf8\"> </head> <body>""" + div + """</body> </html>"""

    #### TME: Elapsed time taken to cluster and plot data
    elapsed = time.time() - start_time
    line = "=" * 60
    print (line)
    print ("Applying K-Means clustering and plotting its output")
    print("Time taken: " + str(elapsed))
    print (line)
    ####

    dbobj.closedb()
    return response

#sess = requests.Session()
#mkMag()
# client.close()
