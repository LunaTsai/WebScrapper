
import requests 
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/newest') #choose target website to get web contents
soup = BeautifulSoup(res.text,'html.parser') #the website I am going to parse is html website
links = soup.select('.titleline') #select all contents that include class = .titleline
subtext = soup.select('.subtext') #select all contents that include class = .subtext

'''
my original Code
def create_custom_hn(links, subtext): # both links and subtexts are an array 
    hn = [] #declare as a list as we will use "append" function in the end
    for idx, item in enumerate(links): # look at each link we get
        title = item.getText() # get the title of each link
        href = item.get('href', None)  # get the real link in each link array, if no link, return "None"
        vote = subtext[idx].select('.score') # get the score of each link
        if len(vote):  
            print(vote[0].getText())
            if vote[0].getText().find(' points'):
                
                points = vote[0].getText().replace(' points', '')
                print('I am with s')
                
            elif vote[0].getText().find(' point') : 
                points = vote[0].getText().replace(' point', '')
                print('I am without s')
                
            hn.append({'title': title, 'link': href, 'vote': points})
    return hn

#hn_print = create_custom_hn(links, subtext)
create_custom_hn(links, subtext)
'''

'''
Corrected Code
'''
def create_custom_hn(links, subtext): 
    hn = [] 
    for idx, item in enumerate(links): 
        title = item.getText() 
        href = item.get('href', None)  
        vote = subtext[idx].select('.score') 
        if len(vote):  
            if ' points' in vote[0].getText():
                points = vote[0].getText().replace(' points', '')
                print('I am with s')
            else: 
                points = vote[0].getText().replace(' point', '')
                print('I am without s')
            hn.append({'title': title, 'link': href, 'vote': points})
    return hn

#hn_print = create_custom_hn(links, subtext)
create_custom_hn(links, subtext)

