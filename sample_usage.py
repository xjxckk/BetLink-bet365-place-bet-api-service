import requests

betlink_sample_server = 'https://api.betlink.ml/sample' # Sample server to send test requests to
api_key = 'SAMPLE-API-KEY'

login_details = {
    'username': 'your_bet365_username',
    'password': 'your_bet365_password',
    'api_key': api_key
    }
response = requests.post(betlink_sample_server + '/setup', json=login_details)
print('Status code:', response)
print('Response data:', response.json())
# Successful response: {'Saved': True}

## Send a bet
# Market names and selection names must be in English and match the names on bet365

# To place a bet on Daniil Medvedev to win the 19th game
bet_details = {
    'match_link': 'https://www.bet365.com/#/IP/EV15902690325C13/',
    'market': '19th Game Winner',
    'selection': 'Daniil Medvedev',
    'stake': '1.00',
    'api_key': api_key
    }
# To place a bet on Asian Handicap > Tunuisia U20 +1.5
bet_details = {
    'match_link': 'https://www.bet365.com/#/AC/B1/C1/D8/E137535717/F3/I3/',
    'market': 'Asian Handicap',
    'selection': '+1.5',
    'column': 2, # The 2nd column across is Tunisia U20 (away team) and 1st Column is the home team (England U20)
    'stake': '1.00',
    'api_key': api_key
    }
# To place a bet on Goal Line > Under 2.5, 3.0
bet_details = {
    'match_link': 'https://www.bet365.com/#/AC/B1/C1/D8/E137535717/F3/I3/',
    'market': 'Goal Line',
    'selection': '2.5, 3.0',
    'column': 3, # The 3rd column across is Under, 2nd Column is Over and 1st Column is the row labels (e.g. 2.5, 3.0)
    'stake': '1.00',
    'api_key': api_key
    }
response = requests.post(server_ip + '/place-bet', json=bet_details)
print('Status code:', response)
response = response.json()
print('Response data:', response)
'''
Successful response:
    {
        'Received': True,
        'BetID': '268d1e51-d62d-41b5-8a0a-2fa9f580d0c4'
    }
'''

bet_id = response['BetID']

placed_bet = {
    'BetID': bet_id,
    'api_key': api_key
    }

sleep(5)
for poll_check in range(30):
    response = requests.post(server_ip + '/bet-result', json=placed_bet)
    print('Status code:', response)
    print('Response data:', response.json())
'''
Bet still placing:
    {'Error': "Bet ID: '268d1e51-d62d-41b5-8a0a-2fa9f580d0c4' not yet placed"}

Successful response:
    {
        'PlacerResult': 'Bet placed',
        'BetID': '268d1e51-d62d-41b5-8a0a-2fa9f580d0c4'
    }
'''
