#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[3]:


page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# # 1) Write a python program to display all the header tags from wikipedia.org.

# In[5]:


Headline=soup.find('span',class_="mw-headline")
Headline.text


# In[6]:


Headline_List=[]
for i in soup.find_all('span',class_="mw-headline"): ##find_all will give you all value
    Headline_List.append(i.text)


# In[7]:


Headline_List


# # 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[8]:


IMDbpage = requests.get('https://www.imdb.com/chart/top/')


# In[9]:


IMDbpage


# In[10]:


soup_IMDB=BeautifulSoup(IMDbpage.content)
soup_IMDB


# In[11]:


name=[]
for i in soup_IMDB.find_all('td',class_="titleColumn"): 
    name.append(i.text.split('\n')[2])
    
name[:100]


# In[12]:


rating=[]
for i in soup_IMDB.find_all('td',class_="ratingColumn imdbRating"): 
    rating.append(i.text.split())
    
rating[:100]


# In[13]:


year=[]
for i in soup_IMDB.find_all('span',class_="secondaryInfo"): 
    year.append(i.text)
    
year[:100]


# In[14]:


import pandas as pd
df= pd.DataFrame({'name':name[:100],'rating':rating[:100],'year':year[:100]})


# In[15]:


df


# # 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[16]:


IMDbIndpage = requests.get('https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=CCDDW8BW2C8ZMGGKQHQ7&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_hd')


# In[17]:


IMDbIndpage


# In[18]:


soup_IMDbIndpage=BeautifulSoup(IMDbIndpage.content)
soup_IMDbIndpage


# In[19]:


Indname=[]
for i in soup_IMDbIndpage.find_all('td',class_="titleColumn"): 
    Indname.append(i.text.split('\n')[2])
    
Indname[:100]


# In[20]:


Indrating=[]
for i in soup_IMDbIndpage.find_all('td',class_="ratingColumn imdbRating"): 
    Indrating.append(i.text.split())
    
Indrating[:100]


# In[21]:


Indyear=[]
for i in soup_IMDbIndpage.find_all('span',class_="secondaryInfo"): 
    Indyear.append(i.text)
    
Indyear[:100]


# In[22]:


import pandas as pd
dfInd= pd.DataFrame({'name':Indname[:100],'rating':Indrating[:100],'year':Indyear[:100]})


# In[23]:


dfInd


# # 4) Write a python program to scrape product name, price and discounts from https://meesho.com/bags-ladies/pl/p7vbp .

# In[24]:


meeshopage= requests.get('https://meesho.com/bags-ladies/pl/p7vbp')

meeshopage


# In[25]:



soup_meeshopage=BeautifulSoup(meeshopage.content)
soup_meeshopage


# In[26]:


prodname=[]
for i in soup_meeshopage.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"): 
    prodname.append(i.text)
    
prodname


# In[132]:


price=[]
for i in soup_meeshopage.find_all('h5',class_="Text__StyledText-sc-oo0kvp-0 hiHdyy"): 
    price.append(i.text.split('₹')[1])
    
price


# In[137]:


discount=[]
for i in soup_meeshopage.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 fCJVtz NewProductCard__DiscountTextParagraph-sc-j0e7tu-16 kmYsnm NewProductCard__DiscountTextParagraph-sc-j0e7tu-16 kmYsnm"): 
    discount.append(i.text.split()[0])
    
discount


# In[138]:


import pandas as pd
dfmeesho= pd.DataFrame({'Product Name':prodname,'price':price,'discount':discount})
dfmeesho


# # Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape

# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[30]:


cricket= requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/test')

cricket


# In[31]:


soup_cricket=BeautifulSoup(cricket.content)
soup_cricket


# In[32]:


team=[]
for i in soup_cricket.find_all('span',class_="u-hide-phablet"): 
    team.append(i.text)

  
    
team


# In[33]:


matches=[] 
for i in soup_cricket.find_all('td',class_="table-body__cell u-center-text"): 
    matches.append(i.text)  
    
matches


# In[34]:


matches


# In[35]:


#matches1 = [matches[i] for i in range(len(matches)) if i % 2 = 0]
#points1 = [matches[i] for i in range(len(matches)) if i % 2 != 0]
matches[0::2]


# In[36]:


matches[1::2]


# In[37]:


ratings=[] 
for i in soup_cricket.find_all('td',class_="table-body__cell u-text-right rating"): 
    ratings.append(i.text)  
    
ratings


# In[140]:


import pandas as pd
cricket2= pd.DataFrame({'team':team[1:10],'matches':matches[0::2],'points':matches[1::2],'ratings':ratings})
cricket2


# for first row

# In[39]:


team1=[]
for i in soup_cricket.find_all('span',class_="u-hide-phablet"): 
    team1.append(i.text)
  
    
team1[0]


# In[40]:


matches1=[] 
for i in soup_cricket.find_all('td',class_="rankings-block__banner--matches"): 
    matches1.append(i.text)  
    
matches1


# In[41]:


point1=[] 
for i in soup_cricket.find_all('td',class_="rankings-block__banner--points"): 
    point1.append(i.text)  
    
point1


# In[42]:


ratings1=[] 
for i in soup_cricket.find_all('td',class_="rankings-block__banner--rating u-text-right"): 
    ratings1.append(i.text.split()[0])  
    
ratings1


# In[43]:


import pandas as pd
cricket1= pd.DataFrame({'team':team1[0],'matches':matches1,'points':point1,'ratings':ratings1})
cricket1


# combining both Dataframe

# In[141]:


union = pd.concat([cricket1, cricket2])
union


# Top 10 ODI Batsmen along with the records of their team and rating

# In[45]:


batsman= requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/test')

batsman


# In[142]:


batsman_info=BeautifulSoup(batsman.content)
batsman_info


# In[47]:


batsman_name=[] 
for i in batsman_info.find_all('td',class_="table-body__cell name"): 
    batsman_name.append(i.text.split('\n')[1])  
    
batsman_name[0:9]


# In[48]:


batsman_team=[] 
for i in batsman_info.find_all('td',class_="table-body__cell nationality-logo"): 
    batsman_team.append(i.text.split('\n')[2])  
    
batsman_team[0:9]


# In[157]:


batsman_ratings=[] 
for i in batsman_info.find_all('td',class_="table-body__cell u-text-right rating"): 
    batsman_ratings.append(i.text.split('\n'))  
    
batsman_ratings[0:9]


# In[144]:


import pandas as pd
batsman2= pd.DataFrame({'Name':batsman_name[0:9],'Team':batsman_team[0:9],'ratings':batsman_ratings[0:9]})
batsman2


# In[145]:


batsman_name1=[] 
for i in batsman_info.find_all('div',class_="rankings-block__banner--name"): 
    batsman_name1.append(i.text)  
    
batsman_name1[0:1]


# In[52]:


batsman_team1=[] 
for i in batsman_info.find_all('div',class_="rankings-block__banner--nationality"): 
    batsman_team1.append(i.text.split('\n')[2])  
    
batsman_team1[0:1]


# In[146]:


batsman_ratings1=[] 
for i in batsman_info.find_all('div',class_="rankings-block__banner--rating"): 
    batsman_ratings1.append(i.text)  
    
batsman_ratings1[0:1]


# In[147]:


#import pandas as pd
batsman1= pd.DataFrame({'Name':batsman_name1[0:1],'Team':batsman_team1[0:1],'ratings':batsman_ratings1[0:1]})
batsman1


# In[148]:


union_batsman = pd.concat([batsman1, batsman2])
union_batsman


# Top 10 ODI bowlers along with the records of their team and rating.

# In[149]:


bowler2= pd.DataFrame({'Name':batsman_name[9:18],'Team':batsman_team[9:18],'ratings':batsman_ratings[9:18]})
bowler2


# In[150]:


bowler1= pd.DataFrame({'Name':batsman_name1[1:2],'Team':batsman_team1[1:2],'ratings':batsman_ratings1[1:2]})
bowler1


# In[151]:


union_bowler = pd.concat([bowler1, bowler2])
union_bowler


# # Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[59]:



cricket_women= requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')

cricket_women


# In[60]:


soup_cricket_wn=BeautifulSoup(cricket_women.content)
soup_cricket_wn


# In[61]:


team_wn=[]
for i in soup_cricket_wn.find_all('span',class_="u-hide-phablet"): 
    team_wn.append(i.text)

  
    
team_wn[1:10]


# In[62]:


matches_wn=[] 
for i in soup_cricket_wn.find_all('td',class_="table-body__cell u-center-text"): 
    matches_wn.append(i.text) 
    
matches_wn


# In[63]:


matches_wn_matches=matches_wn[0::2]
matches_wn_matches#[0:9]


# In[64]:


matches_wn_points= matches_wn[1::2]
matches_wn_points[0:9]


# In[65]:


ratings_wn=[] 
for i in soup_cricket_wn.find_all('td',class_="table-body__cell u-text-right rating"): 
    ratings_wn.append(i.text)  
    
ratings_wn[0:9]


# In[66]:



import pandas as pd
cricket2_wn= pd.DataFrame({'team':team_wn[1:10],'matches':matches_wn_matches[0:9],'points':matches_wn_points[0:9],'ratings':ratings_wn[0:9]})
cricket2_wn


# In[67]:


matches_wn1=[] 
for i in soup_cricket_wn.find_all('td',class_="rankings-block__banner--matches"): 
    matches_wn1.append(i.text) 
    
matches_wn1


# In[68]:


matches_wn_points1=[] 
for i in soup_cricket_wn.find_all('td',class_="rankings-block__banner--points"): 
    matches_wn_points1.append(i.text) 
    
matches_wn_points1


# In[69]:


ratings_wn1=[] 
for i in soup_cricket_wn.find_all('td',class_="rankings-block__banner--rating u-text-right"): 
    ratings_wn1.append(i.text.split()) 
    
ratings_wn1


# In[70]:



import pandas as pd
cricket1_wn= pd.DataFrame({'team':team_wn[0:1],'matches':matches_wn1,'points':matches_wn_points1,'ratings':ratings_wn1})
cricket1_wn


# In[71]:


union_wn = pd.concat([cricket1_wn, cricket2_wn])
union_wn


# # 7) Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content and the code for the video from the link for the youtube video from the post.

# In[72]:



coreyms= requests.get('https://coreyms.com/')

coreyms


# In[119]:


soup_coreyms=BeautifulSoup(coreyms.content)
soup_coreyms


# In[74]:


heading_coreyms=[]
for i in soup_coreyms.find_all('a',class_="entry-title-link"): 
    heading_coreyms.append(i.text)

  
    
heading_coreyms


# In[75]:


date_coreyms=[]
for i in soup_coreyms.find_all('time',class_="entry-time"): 
    date_coreyms.append(i.text)

  
    
date_coreyms


# In[76]:


content_coreyms=[]
for i in soup_coreyms.find_all('div',class_="entry-content"): 
    content_coreyms.append(i.text.split('\n')[1])

  
    
content_coreyms


# In[127]:


print(len(heading_coreyms),len(date_coreyms),len(content_coreyms))


# In[128]:


import pandas as pd
coreyms_final= pd.DataFrame({'Heading':heading_coreyms,'Date':date_coreyms,'Content':content_coreyms})#,'ratings':ratings_wn1})
coreyms_final


# # 8) Write a python program to scrape house details from mentioned URL. It should include house title, location, area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, Rajaji Nagar.

# In[162]:


page_house = requests.get('https://www.nobroker.in/property/sale/bangalore/Indiranagar?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9XQ==&radius=2.0&city=bangalore&locality=Indiranagar')
page_house


# In[163]:


soup_house=BeautifulSoup(page_house.content)
soup_house


# In[164]:


heading_house=[]
for i in soup_house.find_all('span',class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full"): 
    heading_house.append(i.text)

  
    
heading_house


# In[165]:


location_house=[]
for i in soup_house.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95"): 
    location_house.append(i.text)

  
    
location_house


# In[166]:


all_house=[]
for i in soup_house.find_all('div',class_="font-semi-bold heading-6"): 
    all_house.append(i.text)

  
    
all_house


# In[167]:


emi=[]
for word in all_house:
    if word.endswith('Month'):
       # print(word)
        emi.append(word)

emi


# In[168]:


area=[]
for word in all_house:
    if word.endswith('sqft'):
       # print(word)
        area.append(word)

area


# In[169]:


price=[]
for word in all_house:
    if word.endswith('Crores'):
       # print(word)
        price.append(word)

price


# In[170]:


print(len(heading_house),len(location_house),len(emi),len(area),len(price))


# In[172]:


import pandas as pd
house= pd.DataFrame({'House Title':heading_house,'Location':location_house,'EMI':emi,'Area':area,'Price':price  })#,'ratings':ratings_wn1})
house


# # 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[90]:


page_hotel = requests.get('https://www.dineout.co.in/delhi-restaurants/welcome-back')
page_hotel


# In[91]:


soup_hotel=BeautifulSoup(page_hotel.content)
soup_hotel


# In[92]:


#class="restnt-info cursor"
heading_hotel=[]
for i in soup_hotel.find_all('div',class_="restnt-info cursor"): 
    heading_hotel.append(i.text)

  
    
heading_hotel


# In[93]:


#span class="double-line-ellipsis"

cuisine_hotel=[]
for i in soup_hotel.find_all('span',class_="double-line-ellipsis"): 
    cuisine_hotel.append(i.text.split('|')[1])

  
    
cuisine_hotel


# In[94]:


cuisine_hotel=[]
for i in soup_hotel.find_all('span',class_="double-line-ellipsis"): 
    cuisine_hotel.append(i.text.split('|')[0])

  
    
cuisine_hotel


# In[95]:


#class="restnt-loc ellipsis"

location_hotel=[]
for i in soup_hotel.find_all('div',class_="restnt-loc ellipsis"): 
    location_hotel.append(i.text)

  
    
location_hotel


# In[96]:


#restnt-rating rating-4

rating_hotel=[]
for i in soup_hotel.find_all('div',class_="restnt-rating rating-4"): 
    rating_hotel.append(i.text)

  
    
rating_hotel


# In[97]:


#no-img img

image_hotel=[]
for i in soup_hotel.find_all('img',class_="no-img"): 
    image_hotel.append(i['data-src'])

  
    
image_hotel


# In[175]:


import pandas as pd
hotel= pd.DataFrame({'Restuarant Name':heading_hotel,'cuisine':cuisine_hotel,'Location':location_hotel,'Rating':rating_hotel,'Image URL':image_hotel  })#,'ratings':ratings_wn1})
hotel


# # 10) Write a python program to scrape first 10 product details which include product name , price , Image URL from https://www.bewakoof.com/women-tshirts?ga_q=tshirts

# In[99]:


#'https://www.bewakoof.com/women-tshirts?ga_q=tshirts'
page_shopping = requests.get('https://www.bewakoof.com/women-tshirts?ga_q=tshirts')
page_shopping


# In[100]:


soup_shopping=BeautifulSoup(page_shopping.content)
soup_shopping


# In[101]:


#productCardDetail 

product_name_shopping=[]
for i in soup_shopping.find_all('div',class_="productCardDetail"): 
    product_name_shopping.append(i.text.split('₹')[0])

  
    
product_name_shopping[0:10]


# In[102]:


#productCardDetail 

price_shopping=[]
for i in soup_shopping.find_all('span',class_="discountedPriceText"): 
    price_shopping.append(i.text)

  
    
price_shopping


# In[103]:


#productCardDetail 

image_shopping=[]
for i in soup_shopping.find_all('img',class_="productImgTag"): 
    image_shopping.append(i['src'])

image_shopping


# In[176]:


import pandas as pd
shopping= pd.DataFrame({'Product name':product_name_shopping[0:10],'Price':price_shopping[0:10],'Image URL':image_shopping[0:10]})#,'ratings':ratings_wn1})
shopping
# To get 10 rows


# In[ ]:




