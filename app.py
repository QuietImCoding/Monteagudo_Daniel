from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''
<a href="/">Stay here</a>
<a href="/pagetwo">Go to page two</a>
<a href="/pagethree">Go to page three</a>'''

@app.route("/pagetwo")
def pagetwo():
    return '''
<a href="/">Go back to index</a>
<a href="/pagetwo">Stay here</a>
<a href="/pagethree">Go to page three</a>'''

@app.route("/pagethree")
def pagethree():
    return '''
<a href="/">Go back to index</a>
<a href="/pagetwo">Go to page two</a>
<a href="/pagethree">Stay here</a>'''

if __name__=="__main__":
    app.run()
