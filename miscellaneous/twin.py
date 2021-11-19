import twint
import json

from contextlib import contextmanager
import sys, os




@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

c = twint.Config()
#lol = [["hindu" , "chutiya"] ,  ["muslim","terrorist"] , ["lgbt" , "kill"] , ["muslim isis"] , ["hindu","madarchod"] , "madarchod" , "chutiya" , ["muslim" , "chutiya"]]
#lol = [["hindu" , "proud"] , ["hindu" , "rss"] , ["muslim" , "mecca"] , ["muslim" , "mubarak"] , ["lgbt" , "rights"] , ["lgbt" , "pride"]]
#for i in range(0,len(lol)):
#c.Search = lol[i] # hindu , muslim terrorist , hindu chutiya , muslim isis , 
c.Lang = "en"
c.Geo = "28.7041,77.1025,25km" #lang and lat of delhi 
c.Limit = 20
#c.Output = f'./output{i+1}.csv'
c.Output = './output.csv'
c.Store_csv = True
with suppress_stdout():
	twint.run.Search(c)




'''tweets = []
for line in open('output.json', 'r'):
    tweets.append(json.loads(line))



for i in range(0,len(tweets)):
	st = tweets[i]['tweet']
	print(f"{i+1}) {st}")
	
'''
