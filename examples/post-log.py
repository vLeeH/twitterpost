# -*- coding utf-8 -*-
"""
[INFO]
Don't forget to create an Developer account in Twitter
[IMPORTANT]
api_key - is the api key of your app in Twitter api.
secret_key - is the secret key of your app in Twitter api.
token_key - is the token key of your app in Twitter api.
token_secret - is the token secret of your app in Twitter api.
"""

from twitterposts import Twitter
import os
import pprint
from time import sleep

from datetime import date

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")
token_key = os.getenv("TOKEN_KEY")
token_secret = os.getenv("TOKEN_SECRET")


twitter = Twitter(api_key, secret_key, token_key, token_secret)


def menu():
    """Menu of twitterposts example"""
    os.system("cls")
    # os.system("clear")

    print(
        """
████████╗██╗    ██╗██╗████████╗████████╗███████╗██████╗ ██████╗  ██████╗ ███████╗████████╗███████╗
╚══██╔══╝██║    ██║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔════╝
   ██║   ██║ █╗ ██║██║   ██║      ██║   █████╗  ██████╔╝██████╔╝██║   ██║███████╗   ██║   ███████╗
   ██║   ██║███╗██║██║   ██║      ██║   ██╔══╝  ██╔══██╗██╔═══╝ ██║   ██║╚════██║   ██║   ╚════██║
   ██║   ╚███╔███╔╝██║   ██║      ██║   ███████╗██║  ██║██║     ╚██████╔╝███████║   ██║   ███████║
   ╚═╝    ╚══╝╚══╝ ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝
"""
    )

def publicate_tweet(post):
    """Post the tweet function of twitterposts"""
    twitter.tweet(post)

def post_tweet():
    """Main function to put posts publicated in a log.txt"""
    while True:
        ask_post1 = str(input("Do you want post a Tweet[Y/N]? ")).upper().strip()
        if ask_post1 == "Y":
            try:
                sleep(1)
                post = str(input("Inform your tweet: "))
                resp = publicate_tweet(post)
                data = date.today()
                try:
                    with open("tweet_posted.txt", "at+", encoding="utf8") as t:
                        t.write(f"{data.day}/{data.month}/{data.year} - {post}")
                except UnicodeDecodeError as u:
                    print(f"[ERROR] - {u}")
                sleep(1)
                print("Tweet posted with success.")
                sleep(1)
                again_post = str(input("Want to post again[Y/N]? ")).upper().strip()
                if again_post == "N":
                    break
            except Exception as e:
                print(e)

        else:
            break


def post_search():
    """Function to search for tweets and put in a log.txt"""
    while True:
        ask_search = (
            str(input("Do you want to search for a Tweet[Y/N]? ")).upper().strip()
        )
        if ask_search == "Y":
            sleep(1)
            country = (
                str(input("Which country do you want to search? ")).lower().strip()
            )
            language = (
                str(input("And wich language do you want search? ")).lower().strip()
            )
            data = date.today()
            # Use the funtion of twittlib to search for posts
            searching = twitter.search(country, language)
            for result in searching:
                print(f"{result['user']['screen_name']}:")
                print(f"{result['text']} \n")
                print()
                try:
                    with open("results.txt", "at+", encoding="utf8") as t:
                        t.write(
                            f""" {data.day}/{data.month}/{data.year}: \n @{result['user']['screen_name']}: {result['text']} \n\n """
                        )
                except Exception as u:
                        print(f"[ERROR] - {u}")

            sleep(1)
            print("Tweets searched with success.")
            sleep(1)
            again_search = str(input("Want to search again?[Y/N] ")).upper().strip()
            if again_search == "N":
                break

        else:
            break


menu()
post_tweet()
post_search()
