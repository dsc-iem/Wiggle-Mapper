#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import required libraries
import pandas as pd    # Read CSV data from Wigle Wifi Capture
import folium          # Mapping Library


# In[2]:


# import CSV file
df = pd.read_csv('./dataset/sample.csv', delimiter = ',', encoding='latin-1', header=1)


# In[3]:


# Verify that files have been successfully imported
df.sample(5)


# In[7]:


mymap = folium.Map( location=[ df.CurrentLatitude.mean(), df.CurrentLongitude.mean() ], zoom_start=12)


# In[11]:


for coord in df[['CurrentLatitude','CurrentLongitude', 'SSID', 'Type', 'MAC']].values:
    if (coord[3] == 'WIFI'):
        folium.CircleMarker(location=[coord[0],coord[1]], radius=1,color='red', popup=["SSID:", coord[2], "BSSID:", coord[4]]).add_to(mymap)


# In[12]:


# Save MapData To HTML File:
mymap.save('mapdata.html')


# In[13]:


get_ipython().run_cell_magic('HTML', '', '<iframe width="100%" height="650" src="mapdata.html"></iframe>')

