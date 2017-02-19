# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:37:07 2017

@author: zigarean
"""

first_name = input("First Name")
print(first_name)

last_name = input("Last Name")
print(last_name)

age = input("Enter your age in years. ")
print(int(age))

goals = input("What items would you like to save for over the next" + " " + str(90-int(age)) + " " + "years? ")
if "car" in goals:
    print("example_investment")
if "house" in goals:
    print("example_investment")
if "vacation" in goals:
    print("example_investment")
if "other" in goals:
    estimated_price = input("Please print estimated price. ")
    print(int(estimated_price))

achievement_time = input("When would you like to achieve these goals? ")
if "1" in achievement_time:
    print("0-12 Months")
if "2" in achievement_time:
    print("1-2 Years")
if "3" in achievement_time:
    print("2-3 Years")
if "4" in achievement_time:
    print("3+ Years")
    
higher_ed = input("How many years of higher education do you have? ")
if "HSLess" in higher_ed:
    print("Less Than High School")
if "HightSchoolGraduate" in higher_ed:
    print("High School Degree or GED")
if "Associate" in higher_ed:
    print("Associate's Degree")
if "Bachelor" in higher_ed:
    print("Bachelor's degree")
if "Masters" in higher_ed:
    print("Master's degree")
if "Doctorate" in higher_ed:
    print("Doctorate degree")
    
employment = input("What is your current employment status? ")
if "Student" in higher_ed:
    print("Less Than High School")
if "UnemployedSearching" in higher_ed:
    print("High School Degree or GED")
if "UnemployedNot" in higher_ed:
    print("Unemployed Not Searching")
if "PartTime" in higher_ed:
    print("Part Time")
if "FullTime" in higher_ed:
    print("Full Time")
if "SelfEmployed" in higher_ed:
    print("Self Employed") 
if "Unable" in higher_ed:
    print("Unable to Work") 
if "Other" in higher_ed:
    print("Other")   
    
'''Based on options selected, code will return balance and which 
investments to invest in '''

'''Would like to integrate machine learning package to improve 
investment choice over time'''
    
import requests
import json

customerId = '58a8f9871756fc834d9054db'
apiKey = '64c801c7a72776c2bc912d098601a0ca'

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,	
}
# Create a Savings Account
response = requests.get( 
	url, 
	# data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 200:
        account_list = json.loads(response.text)
        print("Account balance is", "$",account_list[0]["balance"])
        
        account_balance = 100 # (account_list[0]["balance"])
        if account_balance > 1000:
            print("invest", "$",account_balance*0.5, "in bonds")
        elif account_balance > 100:
            print("invest", "$", account_balance*0.4, "in stocks")
        else:
            print("Do not invest for this pay-period")

url = ''.format(customerId,apiKey)