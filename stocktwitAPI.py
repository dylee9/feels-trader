"""
stocktwitAPI.py
"""

import requests
import json
import datetime
import os

# Load configuration from environment variables or config file
try:
    from config import STOCKTWITS_USER_ID, STOCKTWITS_USERNAME, STOCKTWITS_ACCESS_TOKEN
    USER_ID = STOCKTWITS_USER_ID
    USERNAME = STOCKTWITS_USERNAME
    ACCESS_TOKEN = STOCKTWITS_ACCESS_TOKEN
except ImportError:
    # Fall back to environment variables
    USER_ID = os.getenv("STOCKTWITS_USER_ID", "")
    USERNAME = os.getenv("STOCKTWITS_USERNAME", "")
    ACCESS_TOKEN = os.getenv("STOCKTWITS_ACCESS_TOKEN", "")
    
    if not all([USER_ID, USERNAME, ACCESS_TOKEN]):
        raise ValueError("StockTwits API credentials not found. Please create config.py from config.py.example or set environment variables.")

SCOPE = "read"
SAVEPATH = "data/test_data_%s.json" % str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

# access stocktwits API via trending data request
raw_data = requests.get("https://api.stocktwits.com/api/2/streams/trending.json?access_token=" + ACCESS_TOKEN)
raw_data_json = raw_data.json()
message_data = raw_data_json['messages']

# preprocess raw data
processed_data = dict()
for message in message_data:
	# print(message)
	print("message_id: ", message['id'])
	print("message_body: ", message['body'])
	print("created_at: ", message['created_at'])
	print("user_follower_count: ", message['user']['followers'])
	print("symbols :", [symb['symbol'] for symb in message['symbols']])
	print("sentiment :", message['entities']['sentiment'] if message['entities'] else None)
	print("\n")

	processed_message = {
		'body': message['body'],
		'datetime': message['created_at'],
		'user_follower_count': message['user']['followers'],
		'symbols': [symb['symbol'] for symb in message['symbols']],
		'sentiment': message['entities']['sentiment'] if message['entities'] else None
	}
	processed_data[message['id']] = processed_message

# save preprocessed trending data as json
with open(SAVEPATH, 'w') as fp:
    json.dump(processed_data, fp)







