from user import User
from database import Database
from twitter_utils import get_access_token,get_request_token, get_oauth_verifier

Database.intiallize(user = 'postgres',
password = '123456' ,
database = 'learning' ,
host = 'localhost')



requested_email=input("Please enter your Email: ")

user=User.load_from_db_by_email(requested_email)

if not user:


    request_token =get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)

    first_name = input("Please Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    user = User(requested_email,first_name,last_name,access_token['oauth_token'], access_token['oauth_token_secret'],None)
    user.save_to_db()




tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=smartphones+filter:images')

for tweet in tweets['statuses']:
    print(tweet['text'])
    print("\n")
