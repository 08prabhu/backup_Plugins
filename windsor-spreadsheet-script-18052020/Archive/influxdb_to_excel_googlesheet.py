#!/usr/bin/env python
# coding: utf-8

# ### pip install influxdb

# In[1]:


from influxdb import InfluxDBClient


# In[2]:


client = InfluxDBClient(host='iotdashboard.mcci.com/influxdb', port=8086, username='mcci', password='mcci*2019', database='mcci-catena-4430')


# In[3]:


dbs = client.get_list_measurements()


# In[4]:


dbs


# In[8]:


# rs = client.query("SELECT * from 112_catena_44")
# cpu_points = list(rs.get_points(measurement='cpu'))


# In[ ]:





# In[9]:


query = 'select * from "112_catena_4430"'


# In[10]:


points = client.query(query, chunked=True, chunk_size=10000).get_points()


# In[11]:


points


# In[12]:


import pandas as pd
dfs = pd.DataFrame(points)


# In[13]:


dfs.head(5)


# In[14]:



dfs.to_excel (r'C:\Users\Revathy\Desktop\export_dataframe.xlsx', index = False, header=True)


# In[16]:


# pip install gspread


# In[17]:


# pip install df2gspread 


# In[31]:


import gspread
from df2gspread import df2gspread as d2g


# In[32]:


# pip install --upgrade oauth2client


# In[33]:


# pip install PyOpenSSL


# In[42]:


from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread-json-f8e6c6e66f51.json', scope)

gc = gspread.authorize(credentials)

# wks = gc.open("gspread")


# In[47]:


dfs.head()


# In[48]:


wks_name = 'gspread'
spreadsheet_key = '1cyStnL1Ba2GZPr3cpDn5z1L8LCqXcclSnfhHpRjFRK4'
d2g.upload(dfs.head(10), spreadsheet_key, wks_name, credentials=credentials, row_names=True)   


# In[52]:


pip install ipython






