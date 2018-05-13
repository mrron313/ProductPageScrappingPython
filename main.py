from bs4 import BeautifulSoup
import requests
import pandas as pd 
from user_agent import generate_user_agent

# generate a user agent
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}

df = pd.DataFrame(columns=['Name','Price'])

#page_link ='https://priyoshop.com/baggitude'
page_link ='https://priyoshop.com/stripe-polo-2'

# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

i=0
for details in page_content.find_all('div', attrs={'class':'details'}):
    #print(details.h2.text)
    for foo in details.find_all('span', attrs={'class': 'actual-price'}):
        #print(foo.text)
        price = foo.text.split(' ')[-1]
        name = details.h2.text.strip('\n')
        df.loc[i] = [name,price]
        i+=1
        
print(df)   
df.to_csv('tshirts.csv', sep=',',index=False)     
        