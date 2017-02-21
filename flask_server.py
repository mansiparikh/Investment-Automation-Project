# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 08:09:35 2017

@author: zigarean
"""

from flask import Flask, render_template, request
from capitalone import capone


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello():

    if request.method == "GET":
        return render_template("investment_wizard.html")
    
    if request.method == "POST":
        account_balance = capone(request)
        #capital one code here
    #insert equation to calculate best investment based on form variables


        return render_template("investment_wizard.html", b=account_balance)
    

if __name__ == "__main__":
    app.run("localhost", port=8080)
