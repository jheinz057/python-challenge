#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import csv
from collections import Counter


# In[2]:


# import the csv
csvpath = os.path.join('election_data.csv')


# In[3]:


# calculate the total number of votes and candidate votes
total_votes = 0
candidate_votes = []
with open (csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    next(csv_reader, None)
    for row in csv_reader:
        total_votes += 1
        candidate_votes.append(row[2])


# In[4]:


total_votes


# In[5]:


# distinct list of all candidates and their respective number of votes
c= Counter(candidate_votes)  
c= dict(c)


# In[6]:


type(c)


# In[7]:


# determine the percentage of total votes each candidate received
c_percent = {k:v / total for total in (sum(c.values()),) for k, v in c.items()}
c_percent


# In[8]:


# determine winner based on popular vote
winner = max(c, key= lambda key: c[key])
winner


# In[9]:


# merge the count dictionary and count percentage dictionary
ml = [c,c_percent]
md= {}
for k in c.keys():
    md[k] = tuple(md[k] for md in ml)


# In[10]:


md


# In[11]:


# print results using the specified format
print('Election Results')
print('Total Votes: {}'.format(total_votes))
for x,y in md.items():
    print("{}: {:0.0%} ({})".format(x,y[1],y[0]))
print('Winner: {}'.format(winner))


# In[12]:


pypoll2_file = open("pypoll.txt", "w")



# writing the text file

pypoll2_file.write("Election Results \n")

pypoll2_file.write("-------------------------------------------- \n")

pypoll2_file.write("Total Votes: " + str(total_votes) + "\n")

pypoll2_file.write("Winner: " + str(winner) + "\n")
                  


# In[ ]:





# In[ ]:





# In[ ]:




