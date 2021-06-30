from typing import Counter
from flask import Flask,render_template,url_for,session,redirect
from flask.globals import request
import pickle
from test import cleaning
import numpy as np
app =Flask(__name__)
app.secret_key = 'lucid'
# model=pickle.load(open('model.pkl','rb'))
user_data=[]

@app.route("/")
def index():
    session["counter"]=0
    return render_template("index.html")
@app.route("/about",methods=["GET","POST"])
def about():
    return render_template("about.html") 
@app.route("/contact",methods=["GET","POST"])
def contact():
    return render_template("contact.html")     
@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html") 

@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=="POST":
        session['username'] = request.form['name']
        session['userage'] = request.form['age']
    return render_template("home.html",
    username=session["username"],
    userage=session["userage"],
    counter=session["counter"]
    )  
       
@app.route("/form",methods=["GET","POST"])
def form():
    print(session["counter"])
    if request.method=="POST":
        session["counter"]=session["counter"]+1
        session['heartrate'] = request.form['heartrate']
        return redirect(url_for("home"))
    
    return render_template("form.html")        
@app.route("/form1",methods=["GET","POST"])
def form1():
    print(session["counter"])
    if request.method=="POST":
        session["counter"]=session["counter"]+1
        session['qn1'] = request.form['qn1']
        session['qn2'] = request.form['qn2']
        session['qn3'] = request.form['qn3']
        session['qn4'] = request.form['qn4']
        session['qn5'] = request.form['qn5']
        session['qn6'] = request.form['qn6']
        session['qn7'] = request.form['qn7']
        session['qn8'] = request.form['qn8']
        session['qn9'] = request.form['qn9']
        return redirect(url_for("home"))    
    return render_template("form1.html")     
@app.route("/form2",methods=["GET","POST"])
def form2():
    print(session["counter"])
    if request.method=="POST":
        session["counter"]=session["counter"]+1
        session['textarea'] = request.form['textarea']
        return redirect(url_for("home"))
    print(session)     
    return render_template("form2.html")
@app.route("/final",methods=["GET","POST"])
def final():
            session["counter"]=0
            text_sentiment = cleaning(session['textarea'])
            if(text_sentiment<=0):
                sentiment=0
            elif text_sentiment>0 and text_sentiment<=0.5:
                sentiment=0.5
            elif text_sentiment>0.5 and text_sentiment<=1:
                sentiment=1
            with open('E:\Final year project\LUCID\picklefinal','rb') as file:
                mp = pickle.load(file)
            a=mp.predict([[session['qn1'],session['qn2'],session['qn3'],session['qn4'],session['qn5'],session['qn6'],session['qn7'],session['qn8'],session['qn9'],sentiment,session['heartrate']]])
            if a=='LOW':
                a='LOW'
                b="Nothing to worry about here, \"All is Well\". Keep Loving yourself, You Happy Champ."
            elif a=='MED':
                a='MODERATE' 
                b="Remember to make yourself happy, spend time on things and people that make you happy."
            elif a=='HIGH':
                a='HIGH' 
                b="You are allowed to feel messed up and inside out. It doesn't mean you're defective it just means you're human."   
            return render_template("final.html",a=a,b=b)
        
if __name__=="__main__":
     app.run(debug=True)   
