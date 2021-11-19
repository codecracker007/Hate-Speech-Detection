from flask import Flask, render_template, request, redirect, url_for
from joblib import load
#from get_tweets import get_related_tweets
#from a import get_related_tweets,remove_pattern
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
token = load('tok_up.joblib')
f = open('result.txt' , 'w')
pipeline = load("blah_up.joblib")


def requestResults(name):
    tweets = [name]
    #tweets = get_related_tweets()
    print(tweets)
    #print(tweets['tweet'])
    sequences = token.texts_to_sequences(tweets)
    data = pad_sequences(sequences,maxlen=75)
    print(type(data))
    #tweets['prediction'] = pipeline.predict(data)
    #pred = tweets['prediction'].tolist()
    tweets = pipeline.predict(data)
    probab = round(tweets[0][0]*100,2)
    return str(probab)
    #print(tweets[0][0])
    #print(type(tweets))
    #f.writeline(tweets)
    #for i in pred:
    	#f.writelines(str(i))
    #print(type(pred))
    #return data + str(tweets)
    #tweets.to_csv('predict.csv' , columns=["prediction"])







#requestResults('i love muslims')


'''app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)
    
'''
