import requests
import urllib
from pathlib import Path
import datetime


class Fixerio(object):
    """Fixer.io free API Python wrapper"""

    _base_url = 'http://data.fixer.io/api/'

    def __init__(self, access_key):
        self._access_key = access_key
    
    def current(self, pairs):
        """get current exchange rate for given pair(s)"""

        # convert input to list TODO: create method for this
        if isinstance(pairs, str):
            pairs = [pairs]

        # convert pairs into 3 letter currencies
        symbols = self._parse_pairs(pairs)

        # create payload for API
        payload = self._create_payload(symbols, endpoint = 'latest')

        # Send request to API
        response = requests.get(payload).json()

        #TODO: Validate response
        self._confirm_response(response)

        # Convert the response to the rates for each pair
        rates = self._rate_converter(pairs, response)
        
        return rates


    def historical(self, pairs, date):
        """get exchange rate for given pair on given date"""
        
        if isinstance(pairs, str):
            pairs = [pairs]

        symbols = self._parse_pairs(pairs)
        
        payload = self._create_payload(symbols, endpoint = 'historical', date = date)

        response = requests.get(payload).json()

        self._confirm_response(response)

        rates = self._rate_converter(pairs, response)

        return rates


    def time_series(self, pairs, start_date, end_date):
        """get exhcange rate for given pair(s) between given dates)"""
        
        # creating a list of dates between given date range
        dates = []
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        delta = end_date - start_date
        for i in range(delta.days + 1):
            dates.append(start_date + datetime.timedelta(days = i))
        dates = [x.strftime('%Y-%m-%d') for x in dates]

        # creating dictionary of rates for each day using historical API endpoint
        dated_rates = {}
        for date in dates:
            dated_rates[date] = self.historical(pairs, date)

        return dated_rates



    def _parse_pairs(self, pairs):
        """method to convert currency pairs to correct format for fixerio API"""
        if isinstance(pairs, str):
            pairs = [pairs]

        base = []
        quoted = []
        for pair in pairs:
            base.append(pair[0:3])
            quoted.append(pair[3:6])
        
        # creating a unique list of requested currencies
        symbols = []
        for b, q in zip(base, quoted):
            if b not in symbols:
                symbols.append(b)
            if q not in symbols:
                symbols.append(q)

        symbols = [x.upper() for x in symbols] # convert all to uppercase
        symbols_comma = ','.join(symbols) # convert to comma seperated string
        
        return symbols_comma


    def _create_payload(self, symbols, endpoint, date=None):
        """method to create payload"""
        param_dict = {'access_key': self._access_key,
                 'base': 'EUR',    # always EUR in the request due to free API limit
                 'symbols': symbols}
        params = urllib.parse.urlencode(param_dict)

        if endpoint == 'latest': 
            url = self._base_url + endpoint + '?' +  params

        elif endpoint == 'historical':
            url = self._base_url + date + '?' + params

        return url


    def _confirm_response(self, response):
        """method to ensure expected response / raise error if not"""
        return response

    def _rate_converter(self, pairs, response):
        """method to convert response to the exchange rate for given pairs"""

        rates = response['rates']
        converted = {}
        
        # calc and add to dictionary correct rate for each pair
        for pair in pairs:
            base = pair[0:3]
            quoted = pair[3:6]
            b_rate = rates[base]
            b_quoted = rates[quoted]
            exchange = b_quoted / b_rate
            converted[pair] = exchange

        return converted


if __name__ == '__main__':
    fx = Fixerio('c263b908a641e8146deac4b2eeb27c17')
    print(fx.current(['EURUSD', 'GBPMXN']))
    print(fx.historical('MXNUSD', '2019-12-22')) 
    print(fx.time_series('USDGBP', '2019-12-22','2019-12-23'))


