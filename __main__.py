import os
import time as t
from log import Log
from config import Config
from scraping_manager.automate import Web_scraping
from email_manager.sender import Email_manager
from telegram.bot import telegram_bot_sendtext

# Global variables
scraper = None
credentials = Config()
logs = Log(os.path.basename(__file__))

def login (): 
    """ Login to page and create scraper instance """

    # Global variables
    global scraper
    global credentials
    global logs

    # Web scraping instance
    logs.info("Starting browser and login in main page", print_text=True)
    home_page = "https://app.ragingbull.com/member/login"
    scraper = Web_scraping(home_page, headless=True)

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
    scraper.set_page(web_page)
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
        post_elem = scraper.get_text (selector_post)

        index_post = 0
        for elem in post_elem: 

            index_post += 1

            # Get post 
            selector_meta = f"{selector_post}:nth-child({index_post}) > .announcement-right > .annoucement-meta"
            selector_text = f"{selector_post}:nth-child({index_post}) > .announcement-right > .annoucement-text"

            meta = scraper.get_text (selector_meta)
            text = scraper.get_text (selector_text)
            post = f"{meta} {text}"

            # Validate last posts
            if text and meta:
                if post not in post_list and "Ben Sturgill" in meta: 
                    post_list.append (post)
                    logs.info(f"New post: {post}", print_text=True)
                    send_notifications (post)

        # Debug lines
        # post = "sample post meta: sample post text."
        # logs.info(f"New post: {post}", print_text=True)
        # send_notifications (post)

        # Wait for the next scrape
        refresh_time = credentials.get_credential("refresh_time")
        t.sleep (refresh_time)

if __name__ == "__main__":
    main()