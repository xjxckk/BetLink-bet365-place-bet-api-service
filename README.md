### BetLink: bet365 place bet API service
We offer a third party API service for bet365 that supports placing bets

![bet365 place bet API service](https://github.com/xjxckk/bet365-place-bet-api-service/blob/master/Placebet.gif)

### Features:
* Login with your bet365 account
* Place undetected bets on prematch events
* Place undetected bets on inplay events

### Sample usage (Python):
Request:
```python
import requests

placebet_server_url = 'http://3.8.91.128:555' # Sample server to send test requests to

login_details = {
    'username': 'your_bet365_username',
    'password': 'your_bet365_password'
    }

response = requests.post(placebet_server_url + '/setup', json=login_details)

bet_details = {
  'home': 'Reilly Opelka',
  'away': 'Oscar Otte',
  'market': '14th Game Winner',
  'Selection': 'Reilly Opelka'
  }

response = requests.post(placebet_server_url + '/bet', json=bet_details)
```
Setup call response:
```python
{'logged_in': True}
```
Bet call response:
```python
{'place_bet_result': 'Bet Placed'}
```

### How it works
* We set up a custom server for you
* You send a request to our setup API with your bet365 account so the bot can login
* You send bet details to our placebet API
* The bet will be placed with our undetected custom browser automation solution
* The result of the placebet request will be returned to you

### How to get access:
Contact me on Telegram: @xJxckk

Message me on Discord: jx#2099
