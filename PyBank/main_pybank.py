#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[4]:


csvpath =  os.path.join('budget_data.csv')


# In[5]:


csvpath


# In[6]:



total_months = 0 
total_revenue = []
months = []
with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader, None)


    for row in csvreader:
        total_months += 1
        months.append(row[0])
        total_revenue.append(int(row[1]))


# In[7]:


total_months


# In[8]:


greatest_increase= total_revenue[0]
greatest_decrease= total_revenue[0]


for row in range(len(total_revenue)):

    if total_revenue[row] >= greatest_increase:

        greatest_increase = total_revenue[row]

        greatest_inc_date = months[row]

    elif total_revenue[row] <= greatest_decrease:

        greatest_decrease = total_revenue[row]

        greatest_dec_date = months[row]


# In[9]:


total_rev = sum(total_revenue)
total_rev


# In[10]:


average_change = round(total_rev/total_months,2)
average_change


# In[11]:


print('Financial Analysis')
print('Total Months: {}'.format(total_months))
print('Average Change: {}'.format(average_change))
print('Greatest Increase in Profits: {} ${}'.format(greatest_inc_date,greatest_increase))
print('Greatest Decrease in Profits: {} ${}'.format(greatest_dec_date,greatest_decrease))


# In[12]:


with open('pyBank.text', 'w') as writefile:

    writefile.writelines('Financial Analysis\n')

    writefile.writelines('----------------------------' + '\n')

    writefile.writelines('Total Months: ' + str(total_months) + '\n')

    writefile.writelines('Total Revenue: $' + str(total_rev) + '\n')

    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')

    writefile.writelines('Greatest Increase in Revenue: ' + greatest_inc_date + ' ($' + str(greatest_increase) + ')'+ '\n')

    writefile.writelines('Greatest Decrease in Revenue: ' + greatest_dec_date + ' ($' + str(greatest_decrease) + ')')


# In[ ]:




