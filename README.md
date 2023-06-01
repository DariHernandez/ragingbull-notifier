<div><a href='https://github.com/darideveloper/ragingbull-notifier/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/ragingbull-notifier.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/ragingbull-notifier/blob/master/logo.png?raw=true' alt='Ragingbull Notifier' height='80px'/>

# Ragingbull Notifier

The project send email and telegram notification for updates in Trading Feed of page: app.ragingbull.com

Start date: **2021-09-03**

Last update: **2023-04-12**

Project type: **client's project**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a></div>

# Details

## Workflow\r
\r
1. Login to page\r
2. Go to Trading Feed secction \r
3. Send an email and telegram menssage for each post in Trading Feed\r
4. For for seach update in the Trading Feed (edit in config file) \r
5. After specific wait time, restart browser (edit in config file)

# Install

## Third party modules\r
\r
Install all modules from pip: \r
\r
\\`\\`\\` bash\r
$ pip install -r requirements.txt\r
\\`\\`\\`\r
\r
## Programs\r
\r
To run the project, the following programs must be installed:\r
\r
* [Google Chrome](https://www.google.com/intl/es/chrome) last version

# Settings

# Settings\r
\r
## config.json\r
\r
All **configurations** are saved in the **config.json file**, so **you can edit it manually**.\r
\r
Sample config.json file\r
\\`\\`\\` json \r
{\r
    \\\"page_user\\\": \\\"my_email@gmail.com\\\",\r
    \\\"page_pass\\\": \\\"my_pass\\\",\r
    \\\"refresh_time\\\": 60,\r
    \\\"restart_time\\\": 3600,\r
    \\\"email\\\": \\\"my_email@gmail.com\\\",\r
    \\\"password\\\": \\\"my password\\\",\r
    \\\"to_emails\\\": [\\\"email1@gmail.com\\\", \\\"email2@gmail.com\\\"],\r
    \\\"telegram_chats\\\": [\\\"1207825117\\\", \\\"1234567890\\\"],\r
    \\\"bot_token\\\": \\\"1922000000:AAFYpemOJaydGC_pVCMKBDoE42i-AAAAAAA\\\"\r
}\r
\\`\\`\\`\r
\r
### page_user\r
\r
Email for login in page app.ragingbull.com\r
\r
### page_pass\r
\r
Password for lofin in page app.ragingbull.com\r
\r
### refresh_time\r
\r
Time to wait (in secods) for search updates again in the page (60 seconds recomendet)\r
\r
### restart_time\r
\r
Time to wait (in secods) for restart google chrome (600 seconds recomendet)\r
\r
### email\r
\r
Email for send notifications. \r
The program currently support the next emails provaiders: \r
* gmail.com\r
* outlook.com\r
* hotmail.com\r
* live.com\r
* yahoo.com\r
* aol.com\r
\r
### password\r
\r
Password of your email or application password for the email. \r
More details about *gmail application password* in next secction.\r
\r
### to_emails\r
\r
List of emails who will recibe the notification.\r
\r
### telegram_chats\r
\r
Id of telegram chats, linked with the bot, who will recibe the notification.\r
\r
### bot_token\r
\r
Private telegram bot token.

# Run

To **start** the program **in terminal **run** the **__main__.py** file with your **python 3.9** interpreter.


