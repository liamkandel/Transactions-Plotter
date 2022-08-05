
# In[6]:


import pandas as pd
import sys

file = sys.argv[1]
df = pd.read_csv(file)


# In[7]:


import re

regex = r"([a-zA-Z ]*)\d*.*"
for item in df.Description:
    str_search = re.search(regex, item)
    desc_trail = str_search.group(1)
    
def filter_descriptions(item):
    a = re.search(regex, item)
    return  a.group(1)

df['Description'] = df['Description'].apply(filter_descriptions)


# In[8]:


from datetime import datetime as dt

df.drop(columns=['Transaction Type', 'Check/Serial #'])
df.Date = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
df.sort_values(by='Date')

def get_year(date):
    return date.year

df['Year'] = df['Date'].apply(get_year)

def convert_date_to_string(time_obj):
    return time_obj.strftime("%m %d %Y")

df['Date'] = df['Date'].apply(convert_date_to_string)


# In[9]:


def take_num_amount(amount):
    get_num = r"[-+]?[0-9]*\.?[0-9]+"
    if amount[0] == '(':
        test = re.search(get_num, amount).group(0)
        amount = amount.replace(amount, test)
        amount = -abs(float(amount))
    else:
        amount = float(amount[1:])     
    return amount


df['Amount'] = df['Amount'].apply(take_num_amount)


# In[10]:


import iqplot
from bokeh.plotting import save, show

p = iqplot.strip(
    data=df,
    cats=['Year', 'Month'],
    q='Amount',
    spread='jitter',
    q_axis='y',
    plot_height=800,
    plot_width=1280,
    tooltips=[
    ('Description', '@{Description}'),
    ('Amount', '$@Amount'),
    ('Date', '@Date')
],
)

show(p)


# In[ ]:




