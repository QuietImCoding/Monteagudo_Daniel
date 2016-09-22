from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return '''
<a href="/">Stay here</a>
<a href="/pagetwo">Go to page two</a>
<a href="/pagethree">Go to page three</a>
<a href="/mytemplate">Go to my render template</a>'''

@app.route("/pagetwo")
def pagetwo():
    return '''
<a href="/">Go back to home</a>
<a href="/pagetwo">Stay here</a>
<a href="/pagethree">Go to page three</a>'''

@app.route("/pagethree")
def pagethree():
    return '''
<a href="/">Go back to home</a>
<a href="/pagetwo">Go to page two</a>
<a href="/pagethree">Stay here</a>'''


file=open("occupations.csv", "r")
stringthing = file.read()

# Splits the string into an array called splitString
splitString = str.split(stringthing, "\r\n")

dict = {}
# Loops through array line by line
for line in splitString:
	if "Total" not in line:
		if len(line)>0 and line[0]=='"':
			line = line[1:]
			dict[float(line[line.index('"')+2:])]=line[0:line.index('"')]
		elif len(line)>0 and splitString.index(line)!=0:
			#print line
			dict[float(line[line.index(',')+1:])]=line[0:line.index(',')]
        

def getRandomOccupation():
	r = random.randint(0,997)
	temp = 0 
	for key in dict:
		temp += 10 * key
		if r < temp:
			return dict[key]
		if temp == 859:
			return dict[key]

pals = ['Kelly', 'Sachal', 'Jason', 'Lawrence']

@app.route("/occupations")
def tablify():
    return render_template("ninja.html", dict=dict, title="Occupations", occupation=getRandomOccupation())
        
if __name__=="__main__":
    app.debug = True
    app.run()
