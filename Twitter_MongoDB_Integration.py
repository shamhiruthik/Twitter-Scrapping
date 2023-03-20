import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
import datetime
import pymongo
import time
 
# REQUIRED VARIABLES
client = pymongo.MongoClient("mongodb+srv://shamhiruthik14:C3Rs*a8%kksJvmD@twitterscraper.kbofooj.mongodb.net/?retryWrites=true&w=majority")  # To connect to MONGODB
mydb = client["TwitterScraper"]    # To create a DATABASE
tweets_df = pd.DataFrame()
dfm = pd.DataFrame()
st.write("# Twitter data scraping")
option = st.selectbox('How would you like the data to be searched?',('Keyword', 'Hashtag'))
word = st.text_input('Please enter a '+option, 'Example: LIC Policy')
start = st.date_input("Select the start date", datetime.date(2022, 1, 1),key='d1')
end = st.date_input("Select the end date", datetime.date(2023, 1, 1),key='d2')
tweet_c = st.slider('How many tweets to scrape', 0, 1000, 5)
tweets_list = []

# SCRAPE DATA USING TwitterSearchScraper
if word:
    try:
        if option=='Keyword':
            for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{word} lang:en since:{start} until:{end}').get_items()):
                if i>tweet_c-1:
                    break
                tweets_list.append([ tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount ])
            tweets_df = pd.DataFrame(tweets_list, columns=['Content', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount'])
        else:
            for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'{word} lang:en since:{start} until:{end}').get_items()):
                if i>tweet_c-1:
                    break            
                tweets_list.append([ tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount ])
            tweets_df = pd.DataFrame(tweets_list, columns=['Content', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount'])
    except Exception as e:
        st.error(f"Too many requests, TwitterRateLimit exceeded, please try again after few hours")
        st.stop()
else:
    st.warning(option,' cant be empty', icon="⚠️")

# DOWNLOAD AS CSV
@st.cache # IMPORTANT: Cache the conversion to prevent computation on every rerun
def convert_df(df):    
    return df.to_csv().encode('utf-8')

if not tweets_df.empty:
    csv = convert_df(tweets_df)
    st.download_button(label="Download data as CSV",data=csv,file_name='Twitter_data.csv',mime='text/csv',)

    # DOWNLOAD AS JSON
    json_string = tweets_df.to_json(orient ='records')
    st.download_button(label="Download data as JSON",file_name="Twitter_data.json",mime="application/json",data=json_string,)

    # UPLOAD DATA TO DATABASE
    if st.button('Upload Tweets to Database'):
        coll=word
        coll=coll.replace(' ','_')+'_Tweets'
        mycoll=mydb[coll]
        dict=tweets_df.to_dict('records')
        if dict:
            mycoll.insert_many(dict) 
            ts = time.time()
            mycoll.update_many({}, {"$set": {"KeyWord_or_Hashtag": word+str(ts)}}, upsert=False, array_filters=None)
            st.success('Successfully uploaded to database', icon="✅")
            st.balloons()
        else:
            st.warning('Cant upload because there are no tweets', icon="⚠️")

    # SHOW TWEETS
    if st.button('Show Tweets'):
        st.write(tweets_df)

# SIDEBAR
with st.sidebar:   
    st.write('Uploaded Datasets: ')
    for i in mydb.list_collection_names():
        mycollection=mydb[i]
        #st.write(i, mycollection.count_documents({}))        
        if st.button(i):            
            dfm = pd.DataFrame(list(mycollection.find())) 

# DISPLAY THE DOCUMENTS IN THE SELECTED COLLECTION
if not dfm.empty: 
    st.write( len(dfm),'Records Found')
    st.write(dfm) 


            


