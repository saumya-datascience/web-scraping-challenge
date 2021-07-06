# web-scraping-challenge! Time for Space Scraping
Webscraping Mars

# Goals
Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Steps performed:
## Step 1 - Scraping

* Used Jupyter Notebook(`mission_to_mars.ipynb`), BeautifulSoup, Pandas, and Requests/Splinter.

Following are the Websites used to scrape the data and the task performed:

### 1 NASA Mars News

* [Mars News Site](https://redplanetscience.com/) 
* collected the latest News Title and Paragraph Text. 
* Assign the text to variables to reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### 2 JPL Mars Space Images - Featured Image

* Accessed Featured Space Image site [here](https://spaceimages-mars.com).

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Made sure to find the image url to the full size `.jpg` image.

* Made sure to save a complete url string for this image.

```python
# Example:
featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
```

### Mars Facts

* Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.

###3  Mars Hemispheres

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

*  Clicked each of the links to the hemispheres in order to find the image url to the full resolution image.

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Staredt by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of  scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, created a route called `/scrape` that will import  `scrape_mars.py` script and call  `scrape` function.

  * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that will query  Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

