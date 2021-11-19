import time
import pandas as pd
import numpy as np
import re
def get_related_tweets():
    tweets_list = []
    count = 50
    try:
        df=pd.read_csv('modified.csv')
        print(df)
        # for tweet in api.search(q=text_query, count=count):
        #     print(tweet.text)
        #df['tweet'] = np.vectorize(remove_pattern)(df['tweet'], "@[\w]*") 
        #df['tweet'] = df['tweet'].str.replace("[^a-zA-Z#]", " ")
        #print(df['tweet'])
        return df['tweet']

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt
    
    
get_related_tweets()
