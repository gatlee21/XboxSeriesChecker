import requests
from bs4 import BeautifulSoup
from datetime import datetime


def msft_xbox_double_check(txt, label):
    return txt == 'Out of stock' and label == 'Checkout bundle'

Red = '\033[91m'
Green = '\033[92m'
Yellow = '\033[93m'
Endc = '\033[0m'
class_text = '_-_-node_modules--xbox-web-partner-core-build-pages-BundleBuilder-Components-BundleBuilderHeader-__BundleBuilderHeader-module___checkoutButton w-100 bg-light-green btn btn-primary'

result = requests.get("https://www.xbox.com/en-us/configure/8wj714n3rbtl")
msft_xbox_website = result.content

soup = BeautifulSoup(msft_xbox_website, 'html.parser')

#can we do a specific one time search for that btn. 1 is there 0 its not.
button = soup.find('button', { 'class' : class_text })
if button is not None:
    #run it through a double check just in case
    if msft_xbox_double_check(button.text, button.get('aria-label')):
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        print('') #padding
        print('Microsoft Store : Xbox Series X 1TB {:>26} {:>10}'.format(f'{Red} {button.text} {Endc}', current_time))
        print('') #padding
    else:
        print('Mircosoft Store: Xbox Series X 1TB {:>26} {:>10}'.format(f'{Yellow} Unsure {Endc}', current_time))
else:
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    print('')
    print('Microsoft Store : Xbox Series X 1TB {:>26} {:>10}'.format(f'{Green} In Stock {Endc}', current_time))
    print('')


