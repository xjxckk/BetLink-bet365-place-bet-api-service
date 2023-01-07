import requests

betlink_sample_server = 'http://api.betlink.ml/sample' # Sample server to send test requests to

login_details = {
    'username': 'your_bet365_username',
    'password': 'your_bet365_password'
    }
response = requests.post(betlink_sample_server + '/setup', json=login_details)
print('Status code:', response)
print('Response data:', response.json())

bet_details = {
    'home': 'Reilly Opelka',
    'away': 'Oscar Otte',
    'market': '14th Game Winner',
    'selection': 'Reilly Opelka',
    'stake': '0.10'
    }
response = requests.post(betlink_sample_server + '/bet', json=bet_details)
print('Status code:', response)
print('Response data:', response.json())
