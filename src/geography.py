import json
import os
import sys
import requests
from requests.exceptions import ConnectionError

key = 'dd53d44d5549b30b1a2537fdc1d0ad5b6a19030c'
api_url = 'http://api.census.gov/data'

def _create_params(params):
    args = ''
    for i, p in enumerate(params.keys()):
        args += "%s=%s" % (p, params[p])
        if i < len(params) - 1:
            args += "&"
    return args

class Geography(object):
    def __init__(self):
        self.area = {
            'state' : 'state',
            'county' : 'county', 
            'zip' : 'zip+code+tabulation+area'
            }

        self.states = {}
        self.counties = {}
        self.zips = {}
        self.data = {
            'state' : self.states,
            'county' : self.counties,
            'zip' : self.zips
            }


        self.codes = {
            'state' : None,
            'county' : None
            }
        
    def download_states(self, output_file):
        year = 2010
        url = api_url + '/' + str(year) + '/sf1'

        payload = { 'for' : 'state:*',
                    'get': 'NAME',
                    'key' : key }
        full = url + '?' + _create_params(payload)
    
        try:
            res = requests.get(full)
            if res.status_code == 200:
                f = open(output_file, "w")
                f.write(res.text)
                f.close()
        except ConnectionError as e:
            print e.explanation

    def download_counties(self, output_file):
        year = 2010
        url = api_url + '/' + str(year) + '/sf1'

        for s in self.states.keys():
            payload = { 'for' : 'county:*',
                        'in' : 'state:%s' % self.states[s], 
                        'get': 'NAME',
                        'key' : key }
            full = url + '?' + _create_params(payload)
    
            try:
                res = requests.get(full)
                if res.status_code == 200:
                    f = open(output_file + '-' + s, "w")
                    f.write(res.text.encode('utf8'))
                    f.close()
            except ConnectionError as e:
                print e.explanation

    def download_zip(self, output_file):
        year = 2010
        url = api_url + '/' + str(year) + '/sf1'

        for s in self.states.keys():
            payload = { 'for' : self.area['zip'] + ':*',
                        'in' : 'state:%s' % self.states[s], 
                        'get': 'NAME',
                        'key' : key }
            full = url + '?' + _create_params(payload)
    
            try:
                res = requests.get(full)
                if res.status_code == 200:
                    f = open(output_file + '-' + s, "w")
                    f.write(res.text.encode('utf8'))
                    f.close()
            except ConnectionError as e:
                print e.explanation

    def load_state_codes(self, input_file):
        f = open(input_file, "r")
        out = f.read()
        data =  json.loads(out)
        for i, d in enumerate(data):
            if i > 0:
                self.states[d[0]] = d[1]

        # Also create a reverse index
        self.state_codes = {v:k for k, v in self.states.items()}
        self.codes['state'] = self.state_codes

    def load_county_codes(self, input_file):
        self.county_codes = {}
        for s in self.states.keys():
            state_file = input_file + '-' + s
            f = open(state_file, "r")
            out = f.read()
            data = json.loads(out)

            self.counties[s] = []
            self.county_codes[s] = {}
            for i, d in enumerate(data):
                if i > 0:
                    cd = str(int(d[2]))
                    self.counties[s].append( { d[0] : cd } )
                    self.county_codes[s][cd] = d[0]

        self.codes['county'] = self.county_codes
                    
    def load_zip_codes(self, input_file):
        for s in self.states.keys():
            state_file = input_file + '-' + s
            f = open(state_file, "r")
            out = f.read()
            data = json.loads(out)

            self.zips[s] = []
            for i, d in enumerate(data):
                if i > 0:
                    self.zips[s].append( d[2] )
def main(argv=None):
    geo = Geography()
    geo.download_states(os.path.join(argv[1], "state_codes"))
    geo.load_state_codes(os.path.join(argv[1], "state_codes"))
    geo.download_counties(os.path.join(argv[1], "county_codes"))
    geo.download_zip(os.path.join(argv[1], "zip_codes"))
    geo.load_county_codes(os.path.join(argv[1], "county_codes"))
    geo.load_zip_codes(os.path.join(argv[1], "zip_codes"))

if __name__ == "__main__":
    main(sys.argv)
