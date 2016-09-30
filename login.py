from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("loginpage.html")

@app.route("/results", methods=['POST'])
def results():
    if request.form['username']=='breakerOfRepos' and request.form['pass']=='H1MrBr0wn!!':
        return render_template("output.html", success=True)
    else:
        return render_template("output.html", success=False)
    
if __name__=="__main__":
    app.debug = True
    app.run()
