from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # 1.Visit the website mars to get the latest title and article
    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    #1a. getting the first news title
    result=soup.find("div",class_="content_title")
    news_title=result.get_text()
    
    #1b.gettint the first news paragrapgh
    result=soup.find("div",class_="article_teaser_body")
    news_p=result.get_text()  
    #2a. find the image url for the current Featured Mars Image 
    url="https://spaceimages-mars.com/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    result=soup.find("div",class_="floating_text_area")
    link=result.a["href"]
    print(link)
    featured_image_url=url+link


    #3. table extraction
    url="https://galaxyfacts-mars.com/"
    tables=pd.read_html(url)
    tables[0]
    df = tables[0]
    df.columns = ['', 'Mars', 'Earth']
    
    html_table = df.to_html(classes="table table-striped")

    #html_table.replace('\n', '')
     

    #hemisphere img and title 
    url = "https://marshemispheres.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    #getting all the hemisphere links
    list=[]
    refs = soup.find_all('a')
    for i in refs:
        link=i["href"]
        if link !="#":
            list.append(i["href"])
    l_list=[list[i] for i in range(len(list)) if i % 2 !=0 ]
    link_list=[url+l_list[i] for i in range(len(l_list)) ]
    #EXTRACTING THE TITLE AND IMAGE LINK AND THEN SAVING THE DICT IN A BIG_LIST
    big_list=[]
    for list in link_list:
        dict={}
        base_url="https://marshemispheres.com"
        browser.links.find_by_href(list)
        print(list)
        browser.visit(list)
        html=browser.html
        soup = bs(html, "html.parser")
        #print(soup)
        result=soup.find_all("a", target="_blank")[2]
        print(result)
        sublink=result["href"]
        print(sublink)
        result2=soup.find("h2",class_="title").get_text()
    
        dict["img_url"]=base_url+result["href"]
        dict["title"]=result2
        big_list.append(dict)

    
    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "table" :  html_table,
        "big_list" : big_list
    }
    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

if __name__=="__main__":
    print(scrape_info())
