from apify_client import ApifyClient
import requests

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_jDxlb5wZ0DaIQEEOMp41CAcHJJcb0e1q3g0A")

# Define the function to extract tweets
def extract_tweets():
    search = input("Write Coin Symbol: $")
    name = input("Write Name of Coin: ")
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
    run = client.actor("heLL6fUofdPgRXZie").call(run_input=run_input)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        tweet_url = item.get("url", "")
        tweet_date = item.get("created_at", "")
        tweet_text = item.get("full_text", "")
        print("URL:", tweet_url)
        print("Date:", tweet_date)
        print("Tweet text:", tweet_text)
        print()

# Define the function to extract transactions
def extract_transactions():
    etherscan_api_key = 'UWBP3JCUCITC9DS9ZHE5SEXIDB71FUEUR8'
    wallet = input("Enter Your Wallet: ")
    response = requests.get(f'https://api.etherscan.io/api?module=account&action=txlist&address={wallet}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={etherscan_api_key}')
    transaction_data = response.json()
    print("************* Extracting Transaction Details *****************")
    relevant_transactions = [tx for tx in transaction_data['result'] if tx['from'].lower() == wallet.lower() or tx['to'].lower() == wallet.lower()]
    for tx in relevant_transactions:
        print(f"Transaction Hash: {tx['hash']}, From: {tx['from']}, To: {tx['to']}, Value: {tx['value']} Wei")

# Define the function to extract user info from tweets
def extract_user_info():
    ai_promt = input("write the hashtag whom first member you want to have?")
    run_input = {
        "addUserInfo": True,
        "maxTweets": 10,
        "scrapeTweetReplies": True,
        "searchMode": "live",
        "searchTerms": [
            f"${ai_promt}",
        ],
        "sinceDate": "2009-01-01",
        "untilDate": "2010-04-02",
        "urls": [
            "https://twitter.com/search?q=gpt&src=typed_query&f=live"
        ]
    }
    run = client.actor("heLL6fUofdPgRXZie").call(run_input=run_input)
    first_tweet = next(client.dataset(run["defaultDatasetId"]).iterate_items(), None)
    print("***RESPONDING**")
    if first_tweet:
        tweet_user_name = first_tweet["user"]["name"]
        tweet_date = first_tweet["created_at"]
        print("User Name:", tweet_user_name)
        print("User Description:", tweet_date)
    else:
        print("No tweets found.")

# Define the function to extract mentioned users
def extract_mentioned_users():
    ai_prompt2 = input("FROM WAT KEYWORDS YOU WANT TO GET MAXIMUM MENTIONED USERS? ")
    run_input = {
        "addUserInfo": True,
        "maxTweets": 10,  
        "scrapeTweetReplies": True,
        "searchMode": "live",
        "searchTerms": [
            f"${ai_prompt2}",
        ],
        "sinceDate": "2009-01-01",
        "untilDate": "2010-04-02",
        "urls": [
            "https://twitter.com/search?q=gpt&src=typed_query&f=live"
        ]
    }
    run = client.actor("heLL6fUofdPgRXZie").call(run_input=run_input)
    for i, item in enumerate(client.dataset(run["defaultDatasetId"]).iterate_items()):
        if i >= 10:
            break
        tweet_user_name = item["user"]["name"]
        tweet_description = item["user"]["description"]
        tweet_date = item["created_at"]
        print(f"Tweet {i+1}:")
        print("User Name:", tweet_user_name)
        print("User Description:", tweet_description)
        print("Tweet Date:", tweet_date)
        print("------------------------")

# Define the main menu loop
while True:
    print("**************** WELCOME TO OUR BOT ********************")
    print("1. Extract Tweets")
    print("2. Extract Transactions")
    print("3. Extract User Info from Tweets")
    print("4. Extract Mentioned Users")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        extract_tweets()
    elif choice == '2':
        extract_transactions()
    elif choice == '3':
        extract_user_info()
    elif choice == '4':
        extract_mentioned_users()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
