
# coding: utf-8

# In[25]:


import pandas as pd 
#import MySQLdb

#cnx = mysql.connector.connect(user='scott', database='employees')
#cursor = cnx.cursor()


# In[26]:


df = pd.read_csv('casper_web_sessions.csv') 
print(df)


# In[38]:


statements = []
for index, row in df.iterrows():
    statements.append("INSERT INTO casper.sessions (user_id, session, session_time, marketing_source) "+
          "VALUES ('{}', {}, '{}', '{}');".format(row.user_id, row.session_id, row.session_time, row.marketing_source)) 


# In[39]:



with open('sessions.sql', 'w') as f: 
    f.write('\n'.join(statements))

