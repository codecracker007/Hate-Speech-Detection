


# importing Flask and other modules
from flask import Flask, request, render_template,render_template_string
from model import requestResults
# Flask constructor
app = Flask(__name__)   
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET" , "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       tweet = request.form.get("tweet")
       print(tweet)
       resu = requestResults(tweet)
       return f'''
       <p> the tweet {tweet} has {resu}% probability of Being hate speech</p> 
       '''
    return render_template("webpage.html")
  
if __name__=='__main__':
   app.run(host='0.0.0.0',port=5000)
