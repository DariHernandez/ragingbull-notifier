import os
import time as t
import datetime
from log import Log
from config import Config
from scraping_manager.automate import Web_scraping
from email_manager.sender import Email_manager
from telegram.bot import telegram_bot_sendtext

# Global variables
scraper = None
credentials = Config()
logs = Log(os.path.basename(__file__))
posts_file_path = os.path.join (os.path.dirname (__file__), "last_posts.txt")

# Get stonks list from local file
stonks_path = os.path.join ("stocks_list.txt")
with open (stonks_path) as stonks_file:
    stonks = stonks_file.read().lower().split (", ")

    # Create stonks dicctionary
    stonks_dict = {}
    for stonk in stonks:
        stonks_dict[stonk] = {
            "counter": 0,
            "posts": []
        }

def get_post_time (post_text):
    
    time_start = post_text.find (" - ")
    time_text = str(post_text[:time_start]).strip()
    post_time = datetime.datetime.strptime (time_text, "%b %d, %Y at %I:%M %p")
    return post_time

def login (): 
    """ Login to page and create scraper instance """

    # Global variables
    global scraper
    global credentials
    global logs

    # Web scraping instance
    logs.info("Starting browser and login in main page", print_text=True)
    home_page = "https://app.ragingbull.com/member/login"
    while True:
        try:
            scraper = Web_scraping(home_page, headless=False)
        except: 
            continue
        else: 
            break

    # login to page
    user = credentials.get_credential("page_user")
    password = credentials.get_credential("page_pass")

    selector_email = "#email"
    selector_password = "#password"
    selector_login = 'button[type="submit"]'

    scraper.send_data(selector_email, user)
    scraper.send_data(selector_password, password)
    scraper.click_js(selector_login)
    t.sleep(5)

    # Disclaimer
    logs.info("Accepting disclaimer", print_text=True)
    scraper.refresh_selenium()
    selector_disclaimer = ".btn.btn-success.btn-lg"
    scraper.click_js(selector_disclaimer)
    t.sleep(5)

    # Target page
    logs.info("Loading target page", print_text=True)
    web_page = "https://app.ragingbull.com/rooms/rb-the-workshop"
    while True:
        try:
            scraper.set_page(web_page)
        except: 
            continue
        else: 
            break
    t.sleep(5)    

def send_notifications (post): 
    """ Send email and telegram notifications """

    # # Get email credentials
    # email = credentials.get_credential("email")
    # password = credentials.get_credential("password")
    # to_emails = credentials.get_credential("to_emails")
    
    # # Send email
    # email_sender = Email_manager(email, password)
    # email_sender.send_email(receivers=to_emails,
    #                         subject="New message of Trading Feed", 
    #                         body=post, 
    #                         print_status=True)

    # Get telegram credentials
    bot_token = credentials.get_credential("bot_token")
    bot_message = f"New message: {post}"
    chat_ids = credentials.get_credential("telegram_chats")

    # Send telegram message
    telegram_bot_sendtext (bot_token, bot_message, chat_ids)

def update_posts_file (post):
    with open (posts_file_path, "a") as file: 
        file.write(f"{post}\n")


def get_posts_list ():
    with open (posts_file_path) as file: 
        return str(file.read()).splitlines()

def main (): 

    """ Extract data, send notifications and restart browser """

    # Global variables
    global scraper
    global credentials
    global logs

    # Start time and first login 
    start_time = t.time()
    login()

    # Main loop for get post
    post_list = []
    while True: 

        # Calculate time for restart browser
        current_time = t.time()
        restart_time = credentials.get_credential("restart_time")
        if (current_time - start_time) > restart_time: 
            print ("Restarting browser...")
            scraper.end_browser()
            login()
            start_time = t.time()

        # Get post
        logs.info("Refreshing page", print_text=True)
        scraper.refresh_selenium()
        selector_post = "section.announcement-wrapper.panel.panel-primary > div > div > ul > li"
        post_elems = scraper.get_text (selector_post)

        index_post = 0
        if post_elems:
            for elem in post_elems: 

                index_post += 1

                # Get post 
                selector_meta = f"{selector_post}:nth-child({index_post}) > .announcement-right > .annoucement-meta"
                selector_text = f"{selector_post}:nth-child({index_post}) > .announcement-right > .annoucement-text"

                meta = scraper.get_text (selector_meta)
                text = scraper.get_text (selector_text)
                post = f"{meta}   {text}"

                # Validate last posts
                if text and meta:

                    last_posts = get_posts_list()
                    if not post in last_posts:

                        # if post not in post_list and ("Ben Sturgill" in meta or "Taylor" in meta): 
                        post_list.append (post)
                        logs.info(f"New post: {post}", print_text=True)
                        send_notifications (post)
                        update_posts_file (post)

                # Validate stonks
                for stonk in stonks:

                    # Search stonk in message
                    valid_post = False
                    stonks_formated = [
                        f" {stonk} ",
                        f",{stonk},",
                        f" {stonk},",
                        f":{stonk} ",
                        f":{stonk},",
                        f":{stonk}.",
                        f" {stonk}.",
                    ]

                    stonks_end =  [
                        f",{stonk}"
                        f" {stonk}"
                    ]

                    for stonk_formated in stonks_formated:
                        if stonk_formated in post.lower():
                            valid_post = True
                            break
                    
                    if not valid_post:
                        for stonk_end in stonks_end:
                            if post.lower().endswith(stonk_end):
                                valid_post = True
                                break

                    # Incress counters and send message
                    if valid_post:
                        if not post in stonks_dict[stonk]["posts"]:
                            stonks_dict[stonk]["counter"] += 1
                            stonks_dict[stonk]["posts"].append (post)

                        # Create stonk message
                        if stonks_dict[stonk]["counter"] >= 2:
                            new_post = stonks_dict[stonk]["posts"][-1]
                            last_post = stonks_dict[stonk]["posts"][-2]

                            # Order post
                            new_post_time = get_post_time (new_post)
                            last_post_time = get_post_time (last_post)

                            if  new_post_time > last_post_time: 
                                stonk_message = f"Stonk: {stonk.upper()}\n\nNew post: \n{new_post}\n\nLast post: \n{last_post}\n"
                            else:
                                stonk_message = f"Stonk: {stonk.upper()}\n\nNew post: \n{last_post}\n\nLast post: \n{new_post}\n"
                                
                            # Clean text for save in local file
                            stonk_message_formated = stonk_message.replace ("\n", " ")

                            # Send stonk message
                            last_posts = get_posts_list()
                            if not stonk_message_formated in last_posts:
                                post_list.append (post)
                                logs.info(f"New stonk: {stonk_message}", print_text=True)
                                send_notifications (stonk_message)
                                update_posts_file (stonk_message_formated)

            # Debug lines
            # post = "sample post meta: sample post text."
            # logs.info(f"New post: {post}", print_text=True)
            # send_notifications (post)

        # Wait for the next scrape
        refresh_time = credentials.get_credential("refresh_time")
        t.sleep (refresh_time)

if __name__ == "__main__":
    main()