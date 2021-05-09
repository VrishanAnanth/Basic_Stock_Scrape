#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
finalnames=[]
finalsectors=[]
finalopen=[]
finalclose=[]


# In[2]:


class StockSpy(scrapy.Spider):
    name='StockSpyder'
    
    def start_requests(self):
        url= 'https://www.moneycontrol.com/india/stockpricequote'
        yield scrapy.Request(url=url, callback=self.findstock)
    
    def findstock(self, response):
        stocklink=[]
        links=response.xpath('//div[@class="PT15"]//td/a/@href').extract()
        for link in links:
            stocklink.append(link)
        for link in stocklink:
            yield response.follow(url=link, callback= self.getprice)
            
    def getprice(self, response):
        name=response.xpath('//div[@id="stockName"]/h1/text()').extract()
        cleanname=[n.strip() for n in name]
        for i in cleanname:
            finalnames.append(i)
        
        
        sector=response.xpath('//div[@id="stockName"]//strong/a/text()').extract()
        cleansector=[s.strip() for s in sector]
        for i in cleansector:
            finalsectors.append(i)
            
        open_p=response.xpath('//div[@class="nsestock_overview bsestock_overview"]//td[@class="nseopn bseopn"]/text()').extract()
        cleanopen=[o.strip() for o in open_p]
        for i in cleanopen:
            finalopen.append(i)
            
        close_p=response.xpath('//div[@class="nsestock_overview bsestock_overview"]//td[@class="nseprvclose bseprvclose"]/text()').extract()
        cleanclose=[c.strip() for c in close_p]
        for i in cleanclose:
            finalclose.append(i)
        
        
    
        
        
      
                     
process= CrawlerProcess()
process.crawl(StockSpy)
process.start()

StockData=pd.DataFrame()
StockData['StockName']=finalnames
StockData['Sector']=finalsectors
StockData['OpenPrice']=finalopen
StockData['PrevClose']=finalclose
StockData.to_excel('MoneyControl.xlsx', sheet_name='NSE_Stocks')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




