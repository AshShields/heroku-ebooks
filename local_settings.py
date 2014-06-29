'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY =  'sXm9pTwBP9VCTVOAAZssHFKhB'
MY_CONSUMER_SECRET = 'Bclqq69tc9kzUj3ZPqSjI3g2vDgnsR3z5SmWlVvC55JNp6e8SP'
MY_ACCESS_TOKEN_KEY = '2594383987-EDpD8qNHf3wu11oijW7wVbvEfg5lT1bKHcP5QXX'
MY_ACCESS_TOKEN_SECRET = ' OprHpTbLeg7Q1AcFqOa0kQ69ZCk31fzrWRHHe71Us0q6K'

SOURCE_ACCOUNTS = ["ghostattics"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "jenebooks" #The name of the account you're tweeting to.
