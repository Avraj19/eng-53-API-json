import requests

# path - url
# variable

path = 'http://api.postcodes.io/postcodes/'
arg = 'UB3 3PN'
response_post_code = requests.get(path + 'ub33ef')

# print(response_post_code.status_code)
# print(response_post_code.headers)
info = response_post_code.json()
print(info['result'])
print('Longitude: ' + str(info['result']['longitude']))
print('Latitude: ' + str(info['result']['latitude']))
print('Country: ' + str(info['result']['country']))
print('nuts :' + info['result']['nuts'])
