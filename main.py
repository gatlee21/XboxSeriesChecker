# Main script with functions to check for Xbox series X | S at the 
# following retailers:
#   - Microsoft Store 


import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime
from twilio.rest import Client
from  msft import msft

#Twilio setup
account_sid = 'ACac6e9a6d3094bf5004a12c8455b4f1b3'
auth_token = 'f391f902c9d6714f2cc3a60f62f35ebd'
client = Client(account_sid, auth_token)

msft = msft(requests, BeautifulSoup, datetime, client)
X_msg = msft.xbox_series_X()
S_msg = msft.xbox_series_S()

#send twilio text msg - comment out for debugging
# message = client.messages \
#                 .create(
#                     body='{0} {1}'.format(X_msg, S_msg),
#                     from_='+17042884313',
#                     to='+16107905285'
#                 )

