# Twitter-Scrapping   ![MIT LICENSE](https://badgen.net//badge/license/MIT/green)   ![MAINTAINED BADGE](https://img.shields.io/badge/Maintained%3F-yes-green.svg)   

Application Link : https://shamhiruthik-twitter-scrapping-twitter-scraper-app-m9zje5.streamlit.app/

Demo Video Link  :

## About

This Web application basically scrapes information from Twitter. Users can scrape data by entering any keyword or hashtag respectively to the Timeline.



## Built using
 * Streamlit
 * Snscrape
 * MongoDb
 * Python Script
 
## Overview:

I have Created a GUI using streamlit that contains the follwing features
 * Can enter any keyword or Hashtag to be searched,
 * select the starting date
 * select the ending date
 * Number of tweets needs to be scrapped.

After scraping is done, it has the following options
 * Download data as CSV
 * Download data as JSON
 * Upload data to DATABASE
 * Display All the Tweets scraped
 * All the Uploaded Collections in Database are Displayed in the left side

## WORKING:

`Step1:` Initially I collected the Keyword, Start date, End date, and Number of tweets from the user using streamlit

`Step 2:` The above details are fed to TwitterSearchScraper and TwitterHashtagScraper. A dataframe is created to store the entire scraped data Now we can download this scraped data in the form of CSV or JSON format

`Step3:` The database connection is established using pymongo A new collection will be created and data is uploaded into that collection if the user wish to upload

`Step4:` A separate sidebar is created to display all the collections that are uploaded to the database, On clicking any collection, we can see the documents in that collection
 
 
 
 ## Demo Images
 
 ### 1. Web App
 ![s1](./Img/s1.png)
 
 ### 2. Request Tweet
 ![s2](./Img/s2.png)
 
 
 ### 3. Results
 ![s3](./Img/s3.png)
 
 ## Installation and Running
 
 open cmd:
1. > C:\Users\shamhiruthik> pip install virtualenv 
2. > C:\Users\shamhiruthik> virtualenv my_twitter_env
3. > C:\Users\shamhiruthik> cd my_twitter_env
4. > C:\Users\shamhiruthik\my_twitter_env> cd Scripts
5. > C:\Users\shamhiruthik\my_twitter_env\Scripts>activate                    # It will activate the virtual environment
6. > (my_twitter_env)  C:\Users\shamhiruthik\> mkdir TwitterScraper           #create a folder 
7. > (my_twitter_env)  C:\Users\shamhiruthik\> cd TwitterScraper              # download the above files from this repository and place inside this folder
8. > (my_twitter_env)  C:\Users\shamhiruthik\TwitterScraper> pip install -r requirements.txt       # it will install all the required modules in the environment
9. > (my_twitter_env)  C:\Users\shamhiruthik\TwitterScraper> streamlit run Twitter_Scraper_App.py   # Now run the app using streamlit
10. > You can now view your Streamlit app in your browser.
