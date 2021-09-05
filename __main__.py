import os
import time as t
from log import Log
from config import Config
from scraping_manager.automate import Web_scraping
from email_manager.sender import Email_manager

# Global variables
scraper = None
credentials = Config()

def login (): 
    """ Login to page and create scraper instance """
    
    # Web scraping instance
    global scraper
    global credentials
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
    scraper.refresh_selenium()
    selector_disclaimer = ".btn.btn-success.btn-lg"
    scraper.click_js(selector_disclaimer)
    t.sleep(5)

    # Target page
    web_page = "https://app.ragingbull.com/rooms/rb-the-workshop"
    scraper.set_page(web_page)
    t.sleep(5)

def send_notifications (post): 
    """ Send email and telegram notifications """

    # Send email
    email = credentials.get_credential("email")
    password = credentials.get_credential("password")
    to_emails = credentials.get_credential("to_emails")
    email_sender = Email_manager(email, password)
    email_sender.send_email(receivers=to_emails,
                            subject="New menssage of Trading Feed", 
                            body=post, 
                            print_status=True)

    # Send notification


def main (): 

    """ Extract data, send notifications and restart browser """

    # Start time and first login 
    global scraper
    global credentials
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
        scraper.refresh_selenium()
        selector_post = "section.announcement-wrapper.panel.panel-primary > div > div > ul > li"
        post_elem = scraper.get_elems (selector_post)

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
            if post not in post_list: 
                post_list.append (post)
                print (f"New post: {post}")
                send_notifications (post)

        # Debug lines
        post = "sample_post"
        send_notifications (post)

        # Wait for the next scrape
        refresh_time = credentials.get_credential("refresh_time")
        t.sleep (refresh_time)

if __name__ == "__main__":
    main()