from splinter import Browser
from bs4 import BeautifulSoup


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape():
# NASA Mars News SIte

    url = "https://mars.nasa.gov/news/"
    response = req.get(url)
     soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_="rollover_description_inner").text

#JPL Mars Space Images    
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(jpl_url)
    response = requests.get(jpl_url)
    base_url = 'https://www.jpl.nasa.gov'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #Find elements for featured_image_url
    featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    featured_image_url = base_url + featured_image_url

#Mars Weather
    weather_url = 'https://twitter.com/MarsWxReport?lang=en'
    browser.visit(weather_url)
    response = requests.get(weather_url)    
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_weather = soup.find_all('div', class_="js-tweet-text-container")

#Mars Hemispheres
     hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    response = requests.get(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')   

    hemisphere_image_urls = []
    list = soup.find_all('div', class_='item')
    for i in list:
        title = soup.find('div', class_="description").find('h3').text  
        img_url = soup.find('a', class_='itemLink product-item')['href']
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

    data = {
     "News_Title": news_title,
     "Paragraph_Text": news_p,
     "Featured Image": featured_image_url,
     "Mars_Weather": mars_weather,
     "Mars Facts": html_table,
     "Mars Hemispheres": hemisphere_image_urls
     }        
     
     return data