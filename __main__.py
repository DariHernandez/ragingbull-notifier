import os
import time as t
from log import Log
from config import Config
from scraping_manager.automate import Web_scraping

def main (): 

    # Config instance
    credentials = Config()
    
    # Web scraping instance
    home_page = "https://app.ragingbull.com/member/login"
    scraper = Web_scraping(home_page, headless=False)

    # login to page
    user = credentials.get_credential("page_user")
    password = credentials.get_credential("page_pass")

    selector_email = "#email"
    selector_password = "#password"
    selector_login = 'button[type="submit"]'

    scraper.send_data(selector_email, user)
    scraper.send_data(selector_password, password)
    scraper.click(selector_login)
    t.sleep(5)


    # Disclaimer
    scraper.refresh_selenium()
    selector_disclaimer = ".btn.btn-success.btn-lg"
    scraper.click(selector_disclaimer)
    t.sleep(5)

    # Target page
    web_page = "https://app.ragingbull.com/rooms/rb-the-workshop"
    scraper.set_page(web_page)
    t.sleep(5)


    # Get post
    scraper.refresh_selenium()
    selector_post = "section.announcement-wrapper.panel.panel-primary > div > div > ul > li"
    post_elem = scraper.get_elems (selector_post)

    post_list = []

    index_post = 0
    for elem in post_elem: 

        index_post += 1

        # Get post 
        selector_meta = f"{selector_post}:nth-child({index_post}) > .announcement-right > .annoucement-meta"
        selector_text = f"{selector_post}:nth-child({index_post}) > .announcement-right > .annoucement-text"

        meta = scraper.get_text (selector_meta)
        text = scraper.get_text (selector_text)

        post = f"{meta} {text}"
        
        # if not post_list: 
        #     post_list.app


    input ("end?")


    


if __name__ == "__main__":
    main()