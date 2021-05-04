# functions to handle request to best buy

class bbuy():
    X_btn_class = 'btn btn-disabled btn-lg btn-block add-to-cart-button'

    def __init__(self, requests, BeautifulSoup, datetime, client):
        self.requests = requests
        self.BeautifulSoup = BeautifulSoup
        self.datetime = datetime
        self.client = client

    def xbox_series_X(self):
        result = self.requests.get("https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324")
        bbuy_xbox_website = result.content
        print(bbuy_xbox_website) #you dont have permission to access...

        soup = self.BeautifulSoup(bbuy_xbox_website, 'html.parser')
        # find the sold out button on best buy's website
        button = soup.find('button', { 'class' : self.X_btn_class })