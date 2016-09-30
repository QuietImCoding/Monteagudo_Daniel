from flask import Flask, render_template, request
import random, hashlib

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("loginpage.html")

@app.route("/create")
def newAccount():
    return render_template("makeaccount.html")

@app.route("/createsuccess", methods=['POST'])
def creationSuccess():
    sentUser = request.form['username']
    sentPass = request.form['pass']
    file logins = open("demlogins.csv", "a")
    logins.write(sentUser + ',' + sentPass)

@app.route("/results", methods=['POST'])
def results():
    file logins = open("demlogins.csv", "r")
    
    myHash = hashlib.sha1(request.form['pass'])
    #myHash.hexdigest()#update(request.form['pass'])
    sentUser = request.form['username']
    sentPwd = request.form['pass']
    
    if sentUser=='breakerOfRepos' and myHash.hexdigest()==hashlib.sha1('H1MrBr0wn!!').hexdigest():
        return render_template("output.html", success=True)
    else:
        return render_template("output.html", success=False)
    
if __name__=="__main__":
    app.debug = True
    app.run()
