# from apify_client import ApifyClient
import requests

# Define your API endpoint and parameters
# api_url = 'https://api.apify.com/v2/acts/{act_id}/run-sync'
from apify_client import ApifyClient
print("**************** WELCOME TO OUR BOT ********************")
# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_jDxlb5wZ0DaIQEEOMp41CAcHJJcb0e1q3g0A")
search = input("Write Coin Symbol: $")
name = input("Write Name of Coin: ")
# Prepare the Actor input
run_input = {
    "addUserInfo": True,
    "maxTweets": 10,
    "scrapeTweetReplies": True,
    "searchMode": "live",
    "searchTerms": [
        f"${search}",
        f"{name}"
    ],
    "sinceDate": "2009-01-01",
    "untilDate": "2010-04-02",
    "urls": [
        "https://twitter.com/search?q=gpt&src=typed_query&f=live"
    ]
}
print("***************** EXTRACTING TWEETS **************************")
run = client.actor("heLL6fUofdPgRXZie").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    tweet_url = item.get("url", "")
    tweet_date = item.get("created_at", "")
    tweet_text = item.get("full_text", "")

    # Print the extracted information
    print("URL:", tweet_url)
    print("Date:", tweet_date)
    print("Tweet text:", tweet_text)
    print()



# act_id = 'mAxIirfenUcKwNXST'
# api_token = 'apify_api_jDxlb5wZ0DaIQEEOMp41CAcHJJcb0e1q3g0A'
#
# # Define your input parameters
# input_params = {
#         "customMapFunction": "(object) => { return {...object} }",
#         "listIds": [
#             "1657850814910590977",
#             "1199504381886050304"
#         ],
#         "maxItems": 1000,
#         "startUrls": [
#             "https://twitter.com/i/lists/78783491"
#         ]
# }
#
# # Set up the request headers
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {api_token}'
# }
#
# response = requests.post(api_url.format(act_id=act_id), json=input_params, headers=headers)
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Error: {response.status_code} - {response.text}")

# print("******************* Processing Data *************************")
# apify_client = ApifyClient('apify_api_jDxlb5wZ0DaIQEEOMp41CAcHJJcb0e1q3g0A')
# dataset = apify_client.dataset('9NdgFVg7vCRb3G0r6')
# dataset_items = dataset.list_items()
# oldest_items = []
#
# for item in dataset_items.items:
#     created_at = item.get('createdAt')
#     if created_at:
#         oldest_items.append((item, created_at))
# oldest_items.sort(key=lambda x: x[1])
# oldest_10_items = oldest_items[:10]
# for i, (item, created_at) in enumerate(oldest_10_items, start=1):
#     print(item)
#     print()

import requests
# 0x8000F432747ccDc71B9DF9F8eB96EFfeeac6218E
# Replace 'your_etherscan_api_key' with your actual Etherscan API key
etherscan_api_key = 'UWBP3JCUCITC9DS9ZHE5SEXIDB71FUEUR8'

wallet = input("Enter Your Wallet: ")

# Specify the coins you are interested in (e.g., Ethereum and any other ERC-20 tokens)
coins_of_interest = ['ETH', 'BTC', 'DEF']

# Specify the date range for transactions (optional)
start_date = '2009-01-01'
end_date = '2024-12-31'

# Make a request to Etherscan API to retrieve transaction data for the wallet address
response = requests.get(f'https://api.etherscan.io/api?module=account&action=txlist&address={wallet}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={etherscan_api_key}')
transaction_data = response.json()
print("************* Extracting Transaction Details *****************")
# Filter transactions by coin and date range
relevant_transactions = [tx for tx in transaction_data['result'] if tx['from'].lower() == wallet.lower() or tx['to'].lower() == wallet.lower()]

# Print relevant transaction information
for tx in relevant_transactions:
    print(f"Transaction Hash: {tx['hash']}, From: {tx['from']}, To: {tx['to']}, Value: {tx['value']} Wei")
