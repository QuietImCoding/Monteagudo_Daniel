from flask import Flask, render_template, request, redirect, url_for, session
import random, hashlib

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def login():        
    if request.form != None:
        session.pop("user")
    if "user" in session:
        return redirect("/results")
    return render_template("loginpage.html")


@app.route("/jacobo")
def js():
    return redirect("http://xkcd.com")
    
@app.route("/create")
def newAccount():
    return render_template("makeaccount.html")

@app.route("/createsuccess", methods=['POST'])
def creationSuccess():
    sentUser = request.form['username']
    sentPass = request.form['pass']
    sentPassConfirm = request.form['passconfirm']
    if sentPass != sentPassConfirm:
        return "<h1>Passwords did not match</h1><a href='/create'>Try again</a>"
    if sentUser in parseCSV("demlogins.csv"):
        return "<h1>Username in use</h1><a href='/create'>Try again</a>"
    logins = open("demlogins.csv", "a")
    logins.write(sentUser + ',' + hashlib.sha1(sentPass).hexdigest() + '\n')
    return "<h4>ACCOUNT CREATED SUCCESSFULLY</h4>" + render_template("loginpage.html")

def parseCSV(location):
    loginstring = open("demlogins.csv", "r")
    loginstring = loginstring.read()
    loginpairs = loginstring.split("\n")
    logins = {}
    print "\n\n\n"
    for pair in loginpairs:
        if len(pair)>1:
            logins[pair[0:pair.index(',')]] = pair[pair.index(",")+1:]
    print "\n\n\n"
    return logins

@app.route("/results", methods=['GET', 'POST'])
def results():
    if "user" in session:
        return render_template("output.html", success=True)
    else:
        logins = parseCSV("demlogins.csv")
        #logins = open("demlogins.csv", "r")
        
        myHash = hashlib.sha1(request.form['pass'])
        #myHash.hexdigest()#update(request.form['pass'])
        sentUser = request.form['username']
        sentPwd = request.form['pass']
        session["user"] = sentUser
        if sentUser in logins and logins[sentUser] == myHash.hexdigest():
            #if sentUser=='breakerOfRepos' and myHash.hexdigest()==hashlib.sha1('H1MrBr0wn!!').hexdigest():
            return render_template("output.html", success=True)
        else:
            return render_template("output.html", success=False)
        
if __name__=="__main__":
    app.debug = True
    app.secret_key = "I4m4H4ppyR0b0tW00pW00pW00pW00p"
    app.run()
