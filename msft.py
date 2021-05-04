#functions to handle request to microsoft store

class msft():

    #color terminal output
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Endc = '\033[0m'

    #button html classes
    X_class_text = '_-_-node_modules--xbox-web-partner-core-build-pages-BundleBuilder-Components-BundleBuilderHeader-__BundleBuilderHeader-module___checkoutButton w-100 bg-light-green btn btn-primary'
    S_class_text = '_-_-node_modules--xbox-web-partner-core-build-pages-BundleBuilder-Components-BundleBuilderHeader-__BundleBuilderHeader-module___checkoutButton w-100 bg-light-green text-gray-900 btn btn-primary'
    time_format = '%I:%M %p'

    def __init__(self, requests, BeautifulSoup, datetime, client):
        self.requests = requests
        self.BeautifulSoup = BeautifulSoup
        self.datetime = datetime
        self.client = client

    def xbox_series_X(self):
        result = self.requests.get("https://www.xbox.com/en-us/configure/8wj714n3rbtl")
        msft_xbox_website = result.content

        soup = self.BeautifulSoup(msft_xbox_website, 'html.parser')

        #can we do a specific one time search for that btn. 1 is there 0 its not.
        button = soup.find('button', { 'class' : self.X_class_text })
        if button is not None:
            #run it through a double check just in caseself.
            if self.msft_xbox_double_check(button.text, button.get('aria-label')):       #Out of stock
                now = self.datetime.now()
                current_time = now.strftime(self.time_format)
                print('') #padding
                print('Microsoft Store : Xbox Series X 1TB {:>26} {:>10}'.format(f'{self.Red} {button.text} {self.Endc}', current_time))
                return 'MSFT Store : Series X  Out of stock {0}'.format(current_time)
            else:   #Button is there but don't know 
                now = self.datetime.now()
                current_time = now.strftime(self.time_format)
                print('Mircosoft Store: Xbox Series X 1TB {:>26} {:>10}'.format(f'{self.Yellow} Unsure {self.Endc}', current_time))
                print('')
                return 'MSFT Store : Series X   Unsure '
        else:       #Possibily in stock 
            now = self.datetime.now()
            current_time = now.strftime(self.time_format)
            print('')
            print('Microsoft Store : Xbox Series X 1TB {:>26} {:>10}'.format(f'{self.Green} In Stock {self.Endc}', current_time))
            return 'MSFT Store : Series X   In Stock'

    def xbox_series_S(self):
        result = self.requests.get("https://www.xbox.com/en-us/configure/942J774TP9JN?ranMID=24542&ranEAID=AKGBlS8SPlM&ranSiteID=AKGBlS8SPlM-rraowjl6v6LYgVrhvaWJcQ&epi=AKGBlS8SPlM-rraowjl6v6LYgVrhvaWJcQ&irgwc=1&OCID=AID2000142_aff_7593_1243925&tduid=%28ir__lgev9o9dlkkfq0rz2kainzir222xu1tshxpyuevp00%29%287593%29%281243925%29%28AKGBlS8SPlM-rraowjl6v6LYgVrhvaWJcQ%29%28%29&irclickid=_lgev9o9dlkkfq0rz2kainzir222xu1tshxpyuevp00")
        msft_xbox_website = result.content

        soup = self.BeautifulSoup(msft_xbox_website, 'html.parser')

        #can we do a specific one time search for that btn. 1 is there 0 its not.
        button = soup.find('button', { 'class' : self.S_class_text })
        if button is not None:
            #run it through a double check just in case
            if self.msft_xbox_double_check(button.text, button.get('aria-label')):       #Out of stock
                now = self.datetime.now()
                current_time = now.strftime(self.time_format)
                print('Microsoft Store : Xbox Series S 512GB {:>24} {:>10}'.format(f'{self.Red} {button.text} {self.Endc}', current_time))
                print('') #padding
                return 'MSFT Store : Series S  Out of stock {0}'.format(current_time)
            else:   #Button is there but don't know 
                now = self.datetime.now()
                current_time = now.strftime(self.time_format)
                print('Mircosoft Store: Xbox Series S 512TB {:>24} {:>10}'.format(f'{self.Yellow} Unsure {self.Endc}', current_time))
                return 'MSFT Stroe : Series S   Unsure '
        else:   #Possibily in stock 
            now = self.datetime.now()
            current_time = now.strftime(self.time_format)
            print('Microsoft Store : Xbox Series S 512GB {:>24} {:>10}'.format(f'{self.Green} In Stock {self.Endc}', current_time))
            print('')
            return 'MSFT Store : Series S  In Stock'


    def msft_xbox_double_check(self, txt, label):
        return txt == 'Out of stock' and label == 'Checkout bundle'
