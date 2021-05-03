import requests
from bs4 import BeautifulSoup
from datetime import datetime


def msft_xbox_check(txt, label):
    return txt == 'Out of stock' and label == 'Checkout bundle'

Red = '\033[91m'
Endc = '\033[0m'

result = requests.get("https://www.xbox.com/en-us/configure/8wj714n3rbtl")
msft_xbox_website = result.content

soup = BeautifulSoup(msft_xbox_website, 'html.parser')

buttons = soup.find_all('button')
for button in buttons:
    aria_label = button.get('aria-label')
    btn_txt = button.text
    if msft_xbox_check(btn_txt, aria_label) == True:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        print('') #padding
        print('Microsoft Store : Xbox Series X 1TB {:>26} {:>10}'.format(f'{Red} Out of stock {Endc}', current_time))
        print('') #padding
        break

