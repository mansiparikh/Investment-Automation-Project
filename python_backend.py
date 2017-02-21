# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:37:07 2017

@author: zigarean
"""   
              
def capone(request):
    ''' 
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    goals = request.form["goals"]
    estimated_price = request.form["estimated_price"]
    achievement_time = request.form["achievement_time"]
    higher_ed = request.form["higher_ed"]
    employment = request.form["employment"]
    '''
                
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
            account_balance = account_balance*0.5
        elif account_balance > 100:
            account_balance = account_balance*0.4
        else:
            account_balance = "Do not recommend investing"

        url = ''.format(customerId, apiKey)
    
        return account_balance
