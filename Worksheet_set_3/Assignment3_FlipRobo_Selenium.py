#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No

# In[2]:


#importing Selenium web driver, Panda library

import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[3]:


#2nd way to access driver is need to add into homepage and call directly

driver=webdriver.Chrome('chromedriver.exe')


# In[ ]:


url='https://www.naukri.com'
driver.get(url)


# In[ ]:


search_job=driver.find_element_by_class_name("suggestor-input ")
search_job


# In[ ]:


search_job.send_keys("Data Analyst") 


# In[ ]:


#2nd way by using Absolute x path
search_loc=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input")
search_loc


# In[ ]:


search_loc.send_keys("Bangalore")


# In[ ]:


#to send click on search button
search_btn=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[6]")
search_btn


# In[ ]:


search_btn.click()


# job-title

# In[ ]:


# 3rd way to search
title_tags=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]') 
len(title_tags)
title_tags[0:11]


# In[ ]:


job_title=[] #--> empty list

for i in title_tags[0:11]:
    job_title.append(i.text)
job_title
    


# In[ ]:


#ellipsis fleft fs12 lh16 
exp_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]') ### IMPORTANT if we write element then it will
#give only one value hence we need to make sure that it is "elements" not "element"
len(exp_tags)
exp_tags[0:2]


# In[ ]:


exp=[] #--> empty list

for i in exp_tags[0:11]:
    exp.append(i.text)
exp
    


# In[ ]:


#Location 
loc_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]') ### IMPORTANT if we write element then it will
#give only one value hence we need to make sure that it is "elements" not "element"
len(loc_tags)
loc_tags[0:10]


# In[ ]:


location=[] #--> empty list

for i in loc_tags[0:11]:
    location.append(i.text)
location


# #company name

# In[ ]:


#Company
company_tags=driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]') ### IMPORTANT if we write element then it will
#give only one value hence we need to make sure that it is "elements" not "element"
len(company_tags)
company_tags[0:10]


# In[ ]:


company_name=[] #--> empty list

for i in company_tags[0:11]:
    company_name.append(i.text)
company_name


# In[ ]:


print(len(job_title),len(location),len(company_name),len(exp))


# In[ ]:





# # create dataframe

# In[ ]:


import pandas as pd


# In[ ]:


jobs=pd.DataFrame({'job-title':job_title,'job-location':location,'company_name':company_name,'experience_required':exp })
jobs


# # Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[ ]:


url='https://www.naukri.com'
driver.get(url)


# In[ ]:


search_job=driver.find_element_by_class_name("suggestor-input ")
search_job


# In[ ]:


search_job.send_keys("Data Scientist") 


# In[ ]:


search_loc=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input")
search_loc


# In[ ]:


search_loc.send_keys("Bangalore")


# In[ ]:


#to send click on search button
search_btn=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[6]")
search_btn


# In[ ]:


search_btn.click()


# In[ ]:


# 3rd way to search
title_tags=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]') 
#len(title_tags)
#title_tags[0:11]

DS_job_title=[] #--> empty list

for i in title_tags[0:11]:
    DS_job_title.append(i.text)
DS_job_title
    


# In[ ]:


#ellipsis fleft fs12 lh16 
exp_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]') ### IMPORTANT if we write element then it will


DS_exp=[] #--> empty list

for i in exp_tags[0:11]:
    DS_exp.append(i.text)
DS_exp


# In[ ]:


#Location 
loc_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]') ### IMPORTANT if we write element then it will

ds_location=[] #--> empty list

for i in loc_tags[0:11]:
    ds_location.append(i.text)
ds_location


# In[ ]:


#Company
company_tags=driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]') ### IMPORTANT if we write element then it will


ds_company_name=[] #--> empty list

for i in company_tags[0:11]:
    ds_company_name.append(i.text)
ds_company_name


# In[ ]:


ds_jobs=pd.DataFrame({'job-title':DS_job_title,'job-location':ds_location,'company_name':ds_company_name,'experience_required':DS_exp })
ds_jobs


# # Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
#         You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required. The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[ ]:


url='https://www.naukri.com'
driver.get(url)


# In[ ]:


search_job=driver.find_element_by_class_name("suggestor-input ")
search_job


# In[ ]:


search_job.send_keys("Data Scientist") 


# In[ ]:


search_loc=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input")
search_loc


# In[ ]:


search_loc.send_keys("Delhi/NCR")


# In[ ]:


#to send click on search button
search_btn=driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div/div[6]")
search_btn


# In[ ]:


search_btn.click()


# In[ ]:


salary_check=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[4]/div[2]/div[2]/label/i")
salary_check


# In[ ]:


salary_check.click()


# In[ ]:


# 3rd way to search
title_tags=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]') 
#len(title_tags)
#title_tags[0:11]

fil_DS_job_title=[] #--> empty list

for i in title_tags[0:11]:
    fil_DS_job_title.append(i.text)
fil_DS_job_title


# In[ ]:



#ellipsis fleft fs12 lh16 
exp_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi experience"]') ### IMPORTANT if we write element then it will


fil_DS_exp=[] #--> empty list

for i in exp_tags[0:11]:
    fil_DS_exp.append(i.text)
fil_DS_exp


# In[ ]:


#Location 
loc_tags=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]') ### IMPORTANT if we write element then it will

fil_DS_location=[] #--> empty list

for i in loc_tags[0:11]:
    fil_DS_location.append(i.text)
fil_DS_location


# In[ ]:


#Company
company_tags=driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]') ### IMPORTANT if we write element then it will


fil_DS_company_name=[] #--> empty list

for i in company_tags[0:11]:
    fil_DS_company_name.append(i.text)
fil_DS_company_name


# In[ ]:


fil_DS_jobs=pd.DataFrame({'job-title':fil_DS_job_title,'job-location':fil_DS_location,'company_name':fil_DS_company_name,'experience_required':fil_DS_exp })
fil_DS_jobs


# # Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. Product Description
# 3. Price
# The attributes which you have to scrape is ticked marked in the below image
# 
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url : https://www.flipkart.com/
# 2. Enter “sunglasses” in the search field where “search for products, brands andmore” is written and click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this pageyou can scrap the required data as usual.

# In[ ]:


#2nd way to access driver is need to add into homepage and call directly

driver=webdriver.Chrome('chromedriver.exe')


# In[ ]:


url_flip='https://www.flipkart.com/'
driver.get(url_flip)


# In[ ]:


search_flip=driver.find_element_by_class_name("_3704LK")
search_flip


# In[ ]:


search_flip.send_keys("sunglasses") 


# In[ ]:


#to send click on search button
search_btn_flip=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search_btn_flip


# In[ ]:



search_btn_flip.click()


# In[ ]:


# 3rd way to search
Brand_tags=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]') 
#len(Brand_tags)
#Brand_tags[0:11]

fil_DS_job_title=[] #--> empty list

for i in Brand_tags[0:101]:
    fil_DS_job_title.append(i.text)
fil_DS_job_title


# In[ ]:


#IRpwTa

#ellipsis fleft fs12 lh16 
Title_tags=driver.find_elements_by_xpath('//a[@class="IRpwTa"]') ### IMPORTANT if we write element then it will


fil_DS_exp=[] #--> empty list

for i in Title_tags[0:101]:
    fil_DS_exp.append(i.text)
fil_DS_exp


# In[ ]:



#Location 
price_tags=driver.find_elements_by_xpath('//div[@class="_30jeq3"]') ### IMPORTANT if we write element then it will

fil_DS_location=[] #--> empty list



for i in price_tags[0:101]:
    fil_DS_location.append(i.text)
fil_DS_location


# In[ ]:



fil_sunglasess1=pd.DataFrame({'Brand':fil_DS_job_title,'Product Description':fil_DS_exp,'Price':fil_DS_location })
fil_sunglasess1


# In[ ]:



#to send click on next button
second_page=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
second_page


# In[ ]:


second_page.click()


# In[ ]:


Brand_tags=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]') 
#len(Brand_tags)
#Brand_tags[0:11]

fil_DS_job_title=[] #--> empty list

for i in Brand_tags[0:101]:
    fil_DS_job_title.append(i.text)

    
#Location 
price_tags=driver.find_elements_by_xpath('//div[@class="_30jeq3"]') ### IMPORTANT if we write element then it will

fil_DS_location=[] #--> empty list



for i in price_tags[0:101]:
    fil_DS_location.append(i.text)

    
#IRpwTa

#ellipsis fleft fs12 lh16 
Title_tags=driver.find_elements_by_xpath('//a[@class="IRpwTa"]') ### IMPORTANT if we write element then it will


fil_DS_exp=[] #--> empty list

for i in Title_tags[0:101]:
    fil_DS_exp.append(i.text)



fil_sunglasess2=pd.DataFrame({'Brand':fil_DS_job_title,'Product Description':fil_DS_exp,'Price':fil_DS_location })
fil_sunglasess2


# In[ ]:



#to send click on next button
third_page=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[4]")
third_page


# In[ ]:


third_page.click()


# In[ ]:


Brand_tags=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]') 
#len(Brand_tags)
#Brand_tags[0:11]

fil_DS_job_title=[] #--> empty list

for i in Brand_tags[0:101]:
    fil_DS_job_title.append(i.text)

    
#Location 
price_tags=driver.find_elements_by_xpath('//div[@class="_30jeq3"]') ### IMPORTANT if we write element then it will

fil_DS_location=[] #--> empty list



for i in price_tags[0:101]:
    fil_DS_location.append(i.text)

    
#IRpwTa

#ellipsis fleft fs12 lh16 
Title_tags=driver.find_elements_by_xpath('//a[@class="IRpwTa"]') ### IMPORTANT if we write element then it will


fil_DS_exp=[] #--> empty list

for i in Title_tags[0:101]:
    fil_DS_exp.append(i.text)



fil_sunglasess3=pd.DataFrame({'Brand':fil_DS_job_title,'Product Description':fil_DS_exp,'Price':fil_DS_location })
fil_sunglasess3


# Top 100 records

# In[ ]:


union = pd.concat([fil_sunglasess1, fil_sunglasess2,fil_sunglasess3])[0:100]
union


# # Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-power- adapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC TSVZAXUHGREPBFGI&marketplace.
# When you will open the above link you will reach to the below shown webpage .
# As shown in the above page you have to scrape the tick marked attributes.These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100 reviews.
# Note: All the steps required during scraping should be done through code only and not manually.
# Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com andsearch for “sneakers” in the search field.
# You have to scrape 4 attributes of each sneaker:
# 1. Brand
# 2. Product Description
# 3. Price
# As shown

# In[ ]:


driver=webdriver.Chrome('chromedriver.exe')


# In[ ]:


url_flip='https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-power- adapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC TSVZAXUHGREPBFGI&marketplace.'
driver.get(url_flip)


# In[ ]:





# In[ ]:


#/html/body/div[1]/div/div[3]/div[1]/div[2]/div[8]/div/div/div[5]/div/a/div/span


#to send click on search button
All_review_click=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[8]/div/div/div[5]/div/a/div/span")
All_review_click

All_review_click.click()


# # given by Sapna
# 
# start=0
# 
# end=4
# 
# for page in range(start,end):#for loop for scrapping 4 page
# 
#     ratings_tags=driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]') 
#     
#     for i in ratings_tags:
#         fil_DS_job_title.append(i.text)
# 
# 
#     #prices=driver.find_elements_by_xpath("//div[@class='_30jeq3']")# scraping the price from the xpath
# 
#     #for i in prices:
#         #price.append(i.text)
# 
#         
# 
#     nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")#scraping the list of buttons from the page
# 
#     try:
# 
#         driver.get(nxt_button[1].get_attribute('href'))#getting the link from the list for next page
# 
#     except:
# 
#         driver.get(nxt_button[0].get_attribute('href'))    
# 
# fil_DS_job_title
# #price
# 
# 

# In[ ]:


# loop for ratings

start=100

end=0

rating_info=[]

while(start>=end):

    ratings_tags=driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]') 
    
    for i in ratings_tags:
        rating_info.append(i.text)
        end=len(rating_info)
       

    nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")#scraping the list of buttons from the page

    try:

        driver.get(nxt_button[1].get_attribute('href'))#getting the link from the list for next page

    except:

        driver.get(nxt_button[0].get_attribute('href'))    

len(rating_info)
#price


# In[ ]:


url_flip='https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-power- adapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC TSVZAXUHGREPBFGI&marketplace.'
driver.get(url_flip)


# In[ ]:


All_review_click=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[8]/div/div/div[5]/div/a/div/span")
All_review_click

All_review_click.click()


# In[ ]:


# loop for Review
review=[]
#nxt_button=[]
start=100

end=0



while(start>=end):
    
    reviews=driver.find_elements_by_xpath("//p[@class='_2-N8zT']")# scraping the price from the xpath

    for i in reviews:
        review.append(i.text)
        end=len(review)
       

    nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")#scraping the list of buttons from the page

    try:

        driver.get(nxt_button[1].get_attribute('href'))#getting the link from the list for next page

    except:

        driver.get(nxt_button[0].get_attribute('href'))    

len(review)
#price


# In[ ]:


url_flip='https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-power- adapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC TSVZAXUHGREPBFGI&marketplace.'
driver.get(url_flip)


# In[ ]:


All_review_click=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[8]/div/div/div[5]/div/a/div/span")
All_review_click

All_review_click.click()


# In[ ]:


# loop for Review
fullreview=[]    
nxt_button=[]
start=100

end=0



while(start>=end):
    
   
    fullreviews=driver.find_elements_by_xpath("//div[@class='t-ZTKy']")# scraping the price from the xpath

    for i in fullreviews:
        fullreview.append(i.text)
        end=len(fullreview)
       

    nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")#scraping the list of buttons from the page

    try:

        driver.get(nxt_button[1].get_attribute('href'))#getting the link from the list for next page

    except:

        driver.get(nxt_button[0].get_attribute('href'))    

len(fullreview)
#price


# In[ ]:


filpkart=pd.DataFrame({'Rating':rating_info[0:100],'Review summary':review[0:100],'Full Review':fullreview[0:100]})
filpkart


# # Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com andsearch for “sneakers” in the search field.
# You have to scrape 4 attributes of each sneaker:
# 1. Brand
# 2. Product Description
# 3. Price
# As shown in the below image, you have to scrape the tick marked attributes

# In[ ]:


url_flip='https://www.flipkart.com/'
driver.get(url_flip)


# In[ ]:


search_flip=driver.find_element_by_class_name("_3704LK")
search_flip


# In[ ]:


search_flip.send_keys("sneakers") 


# In[ ]:


#to send click on search button
search_btn_flip=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search_btn_flip


# In[ ]:


search_btn_flip.click()


# In[ ]:


#_2WkVRV
brand=[]
brands=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")# scraping the price from the xpath

for i in brands:
    brand.append(i.text)
brand


# In[ ]:


# loop for Review
brand=[]    
nxt_button=[]
start=100

end=0



while(start>=end):
  
    brands=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")# scraping the price from the xpath

    for i in brands:
        brand.append(i.text)
        end=len(brand)
       

    nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")#scraping the list of buttons from the page

    try:

        driver.get(nxt_button[1].get_attribute('href'))#getting the link from the list for next page

    except:

        driver.get(nxt_button[0].get_attribute('href'))    

len(brand)
#price


# In[ ]:


url_flip='https://www.flipkart.com/'
driver.get(url_flip)


# In[ ]:


search_flip=driver.find_element_by_class_name("_3704LK")
search_flip


# In[ ]:


search_flip.send_keys("sneakers") 


# In[ ]:


#to send click on search button
search_btn_flip=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search_btn_flip


# In[ ]:


search_btn_flip.click()


# In[ ]:


# loop for Review
Product=[]    
nxt_button=[]
start=100

end=0



while(start>=end):
  
    Products=driver.find_elements_by_xpath("//a[@class='IRpwTa']")# scraping the price from the xpath

    for i in Products:
        Product.append(i.text)
        end=len(Product)
       

    nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")#scraping the list of buttons from the page

    try:

        driver.get(nxt_button[1].get_attribute('href'))#getting the link from the list for next page

    except:

        driver.get(nxt_button[0].get_attribute('href'))    

len(Product)
#price


# In[ ]:


url_flip='https://www.flipkart.com/'
driver.get(url_flip)


# In[ ]:


search_flip=driver.find_element_by_class_name("_3704LK")
search_flip


# In[ ]:


search_flip.send_keys("sneakers") 


# In[ ]:


#to send click on search button
search_btn_flip=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search_btn_flip


# In[ ]:


search_btn_flip.click()


# In[ ]:


# loop for Review
Price=[]    
nxt_button=[]
start=100

end=0



while(start>=end):
  
    Prices=driver.find_elements_by_xpath("//div[@class='_30jeq3']")# scraping the price from the xpath

    for i in Prices:
        Price.append(i.text)
        end=len(Price)
       

    nxt_button=driver.find_elements_by_xpath("//a[@class='_1LKTO3']")#scraping the list of buttons from the page

    try:

        driver.get(nxt_button[1].get_attribute('href'))#getting the link from the list for next page

    except:

        driver.get(nxt_button[0].get_attribute('href'))    

len(Price)
#price


# In[ ]:


Sneakers=pd.DataFrame({'Brand':brand[0:100],'Product':Product[0:100],'Price':Price[0:100]})
Sneakers


# # Q7: Go to the link - https://www.myntra.com/shoes
# Set Price filter to “Rs. 7149 to Rs. 14099 ” , Color filter to “Black”, as shown inthe below image.
# And then scrape First 100 shoes data you get. The data should include “Brand” of the shoes , Short Shoe description, price of the shoe as shown in the below image.

# In[ ]:


url_flip='https://www.myntra.com/shoes'
driver.get(url_flip)


# to check on filters

# In[ ]:


price_check=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label")
price_check


# In[ ]:


price_check.click()


# In[ ]:


color_check=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label")
color_check


# In[ ]:


color_check.click()


# In[ ]:


#product-brand
Product_myntra=[]
Products_myntra=driver.find_elements_by_xpath("//h3[@class='product-brand']")# scraping the price from the xpath
for i in Products_myntra:
    Product_myntra.append(i.text)
len(Product_myntra)


# In[ ]:


desc_myntra=[]
descs_myntra=driver.find_elements_by_xpath("//h4[@class='product-product']")# scraping the price from the xpath
for i in descs_myntra:
    desc_myntra.append(i.text)
len(desc_myntra)


# In[ ]:


Price_myntra=[]
Prices_myntra=driver.find_elements_by_xpath("//div[@class='product-price']")# scraping the price from the xpath
for i in Prices_myntra:
    Price_myntra.append(i.text.split()[1])
len(Price_myntra)


# # loop for Review
# Product_myntra=[]    
# nxt_button=[]
# start=100
# 
# end=0
# 
# 
# 
# while(start>=end):
#   
#     Products_myntra=driver.find_elements_by_xpath("//h3[@class='product-brand']")# scraping the price from the xpath
#     for i in Products_myntra:
#         Product_myntra.append(i.text)    
#         end=len(Product_myntra)
#         
#     next_button=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/div[2]/ul/li[12]/a")#scraping the list of buttons from the page
#     
#     next_button.click()
#         
#     #next_button=driver.find_element_by_xpath("//a[@rel='pagination-next']")#scraping the list of buttons from the page
# 
#     try:
# 
#         driver.get(next_button[1].get_attribute('href'))#getting the link from the list for next page
# 
#     except:
# 
#         driver.get(next_button[0].get_attribute('href'))    
# 
# #len(Product_myntra)
# #price
# 
# 

# In[ ]:


Product_myntra=[]
desc_myntra=[]
Price_myntra=[]

Products_myntra=driver.find_elements_by_xpath("//h3[@class='product-brand']")# scraping the price from the xpath
for i in Products_myntra:
    Product_myntra.append(i.text)
        
    
descs_myntra=driver.find_elements_by_xpath("//h4[@class='product-product']")# scraping the price from the xpath
for i in descs_myntra:
    desc_myntra.append(i.text)



Prices_myntra=driver.find_elements_by_xpath("//div[@class='product-price']")# scraping the price from the xpath
for i in Prices_myntra:
    Price_myntra.append(i.text.split()[1])
Price_myntra= [w.replace('Rs.', '') for w in Price_myntra]


# In[ ]:


print(len(Product_myntra),len(desc_myntra),len(Price_myntra))


# In[ ]:


next_button=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[2]/div/div[2]/section/div[2]/ul/li[12]/a")#scraping the list of buttons from the page


# In[ ]:


next_button.click()


# In[ ]:


Products_myntra=driver.find_elements_by_xpath("//h3[@class='product-brand']")# scraping the price from the xpath
for i in Products_myntra:
    Product_myntra.append(i.text)
        
    
descs_myntra=driver.find_elements_by_xpath("//h4[@class='product-product']")# scraping the price from the xpath
for i in descs_myntra:
    desc_myntra.append(i.text)



Prices_myntra=driver.find_elements_by_xpath("//div[@class='product-price']")# scraping the price from the xpath
for i in Prices_myntra:
    Price_myntra.append(i.text.split()[1])
Price_myntra= [w.replace('Rs.', '') for w in Price_myntra]


# In[ ]:


print(len(Product_myntra),len(desc_myntra),len(Price_myntra))


# In[ ]:


myntra_sneakers=pd.DataFrame({'Product':Product_myntra,'Short Desc':desc_myntra,'Price':Price_myntra})
myntra_sneakers


# # Q8: Go to webpage https://www.amazon.in/
# Enter “Laptop” in the search field and then click the search icon.
# Then set CPU Type filter to “Intel Core i7” and “Intel Core i9” as shown in the below image:
#     After setting the filters scrape first 10 laptops data. You have to scrape 3 attributesfor each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[318]:


url_flip='https://www.amazon.in/'
driver.get(url_flip)


# In[319]:



search_amazon=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search_amazon

 


# In[320]:


search_amazon.send_keys("Laptop")


# In[321]:


#to send click on search button
search_btn_amazon=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div")
search_btn_amazon


# In[322]:



search_btn_amazon.click()


# In[323]:


CPU_check=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[10]/span/a/div/label/i")
CPU_check


# In[324]:


CPU_check.click()


# In[ ]:


CPU_check=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[12]/span/a/div/label/i")
CPU_check

#CPU_check9=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[13]/span/a/div/label/i")
#CPU_check9


# In[ ]:


CPU_check.click()


# In[325]:


#a-size-medium a-color-base a-text-normal

title_myntra=[]
desc_myntra=[]
Price_myntra=[]

title_myntras=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")# scraping the price from the xpath
for i in title_myntras:
    title_myntra.append(i.text)
        
    
#ratings_myntras=driver.find_elements_by_xpath("//i[@class='a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom']")# scraping the price from the xpath
#for i in ratings_myntras:
    #ratings_myntra.append(i.text)



price_myntra=[]
prices_myntra=driver.find_elements_by_xpath("//span[@class='a-price-whole']")# scraping the price from the xpath
for i in prices_myntra:
    price_myntra.append(i.text)


# In[ ]:


search_flip=driver.find_element_by_class_name("_3704LK")
search_flip


# In[326]:


final_myntra=pd.DataFrame({'Title':title_myntra[0:10],'Price':price_myntra[0:10]})
final_myntra


# # Q9: Write a python program to scrape data for first 10 job results for Data Scientist Designation in Noida location. You have to scrape company name, No. of days ago when job was posted, Rating of the company. This task will be done in following steps:
# 1. First get the webpage https://www.ambitionbox.com/
# 2. Click on the Job option as shown in the image
# 3. After reaching to the next webpage, In place of “Search by Designations, Companies, Skills” enter “Data Scientist” and click on search button.
# ASSIGNMENT 2
# 4. You will reach to the following web page click on location and in place of “Search location” enter “Noida” and select location “Noida”.
# 5. Then scrape the data for the first 10 jobs results you get on the above shown page.
# 6. Finally create a dataframe of the scraped data.
# Note: All the steps required during scraping should be done through code only and not manually.

# In[327]:


url_flip='https://www.ambitionbox.com/'
driver.get(url_flip)


# In[334]:


#/html/body/section[1]/div/div[2]/form/span/input

click_job=driver.find_element_by_xpath("/html/body/div[1]/nav/nav/a[6]")
click_job


# In[335]:


click_job.click()


# In[336]:


#/html/body/div/div/div/div[2]/div/div/div/div[1]/span/input
Search=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div/div/div/span/input")
Search


# In[337]:


Search.send_keys("Data Scientist") 


# In[338]:


#/html/body/section[1]/div/div[2]/form/span/input

search_click=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div/div/button/span")
search_click


# In[339]:


search_click.click()


# In[346]:


#
location_click=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]")
location_click


# In[347]:


location_click.click()


# In[348]:


#/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input
noida_click=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input")
noida_click


# In[349]:


noida_click.send_keys("Noida") 


# In[350]:


#/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input
enter_click=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/label")
enter_click


# In[351]:


enter_click.click()


# In[359]:


job_ambition=[]
job_ambitions=driver.find_elements_by_xpath("//a[@class='title noclick']")# scraping the price from the xpath
for i in job_ambitions:
    job_ambition.append(i.text)
job_ambition


# In[365]:


#p company body-medium
desc_ambition=[]
desc_ambitions=driver.find_elements_by_xpath("//span[@class='body-small-l']")# scraping the price from the xpath
for i in desc_ambitions:
    desc_ambition.append(i.text)
desc_ambition=desc_ambition[::2]
desc_ambition


# In[366]:


#span body-small
rating_ambition=[]
rating_ambitions=driver.find_elements_by_xpath("//span[@class='body-small']")# scraping the price from the xpath
for i in rating_ambitions:
    rating_ambition.append(i.text)
#desc_ambition=desc_ambition[::2]
rating_ambition


# In[367]:


print(len(job_ambition),len(desc_ambition),len(rating_ambition))


# In[368]:


Ambition=pd.DataFrame({'Job':job_ambition,'Job Post':desc_ambition,'Rating':rating_ambition})
Ambition


# # Q10: Write a python program to scrape the salary data for Data Scientist designation.
# You have to scrape Company name, Number of salaries, Average salary, Minsalary, Max Salary. The above task will be, done as shown in the below steps:
# 1. First get the webpage https://www.ambitionbox.com/
# 2. Click on the salaries option as shown in the image.
# ASSIGNMENT 2
# 3. After reaching to the following webpage, In place of “Search Job Profile” enters “Data Scientist” and then click on “Data Scientist”.
# You have to scrape the data ticked in the above image.
# 4. Scrape the data

# In[12]:


url_flip='https://www.ambitionbox.com/'
driver.get(url_flip)


# In[13]:


#to send click on search button
Salary_click=driver.find_element_by_xpath("/html/body/div[1]/nav/nav/a[4]")
Salary_click


# In[14]:


Salary_click.click()


# In[15]:


#/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/input

search=driver.find_element_by_xpath("/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/input")
search


# In[16]:


search.send_keys("Data Scientist") 


# In[17]:


#/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/div/div/div[1]/div/div

select=driver.find_element_by_xpath("/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/input")
select


# In[18]:


select.click()


# In[424]:


#/html/body/div/div/div/main/section[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/div[1]/a
job_ambition1=[]
no_sal=[]
job_ambition=driver.find_elements_by_xpath("//div[@class='name']")

for i in job_ambition:
    job_ambition1.append(i.text.split('\n')[0])
job_ambition1

for i in job_ambition:
    no_sal.append(i.text.split('\n')[1])
no_sal


# In[420]:


# div value body-medium
min_salary=[]
lis_min_salary=driver.find_elements_by_xpath("//div[@class='value body-medium']")

for i in lis_min_salary:
    min_salary.append(i.text)#.split('\n')[0])
min_salary[0::2]
max_salary[1::2]


# In[422]:


#p averageCtc
avg_salary=[]
lis_avg_salary=driver.find_elements_by_xpath("//p[@class='averageCtc']")

for i in lis_avg_salary:
    avg_salary.append(i.text)#.split('\n')[0])
avg_salary


# In[429]:


ambitionbox=pd.DataFrame({'Company name':job_ambition1,'No Of Salary':no_sal,'Min Salary':min_salary[0::2],'Avg Salary':avg_salary,'Max Salary':min_salary[1::2]})
ambitionbox


# In[ ]:




