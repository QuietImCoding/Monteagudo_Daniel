from flask import Flask, render_template

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

pals = ['Kelly', 'Sachal', 'Jason', 'Lawrence']

@app.route("/mytemplate")
def template():
    return render_template("ninja.html", pals=pals, color="green")

if __name__=="__main__":
    app.debug = True
    app.run()
