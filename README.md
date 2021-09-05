# Ragingbull Notifier
**python version: 3.9**

The project send email and telegram notification for updates in Trading Feed of page: app.ragingbull.com

## Workflow

1. Login to page
2. Go to Trading Feed secction 
3. Send an email and telegram menssage for each post in Trading Feed
4. For for seach update in the Trading Feed (edit in config file) 
5. After specific wait time, restart browser (edit in config file) 

# Install
## Third party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

## Programs

To run the project, the following programs must be installed:

* [Google Chrome](https://www.google.com/intl/es/chrome) last version

# Run the program

To **start** the program **in terminal **run** the **__main__.py** file with your **python 3.9** interpreter.

# Settings

## config.json

All **configurations** are saved in the **config.json file**, so **you can edit it manually**.

Sample config.json file
``` json 
{
    "page_user": "my_email@gmail.com",
    "page_pass": "my_pass",
    "refresh_time": 60,
    "restart_time": 3600,
    "email": "my_email@gmail.com",
    "password": "my password",
    "to_emails": ["email1@gmail.com", "email2@gmail.com"],
    "telegram_chats": ["1207825117", "1234567890"],
    "bot_token": "1922000000:AAFYpemOJaydGC_pVCMKBDoE42i-AAAAAAA"
}
```

### page_user

Email for login in page app.ragingbull.com

### page_pass

Password for lofin in page app.ragingbull.com

### refresh_time

Time to wait (in secods) for search updates again in the page (60 seconds recomendet)

### restart_time

Time to wait (in secods) for restart google chrome (600 seconds recomendet)

### email

Email for send notifications. 
The program currently support the next emails provaiders: 
* gmail.com
* outlook.com
* hotmail.com
* live.com
* yahoo.com
* aol.com

### password

Password of your email or application password for the email. 
More details about *gmail application password* in next secction.

### to_emails

List of emails who will recibe the notification.

### telegram_chats

Id of telegram chats, linked with the bot, who will recibe the notification.

### bot_token

Private telegram bot token.

## Gmail application password

With this [tutorial](https://youtu.be/QI2NM9Uy6R4) you can create your application password for gmail.

### Instructions: 

1. Access your gmail account.
2. Click on your profile forum.
3. Click on "Manage your Google Account".
4. Go to the "Security" tab.
5. Select "2-steps verification".
6. Click on "Get started".
7. Enter your password.
8. Verify your phone number.
9. Select SMS confirmation.
10. Wait to receive a text message on your cell phone.
11. When you receive it, confirm the security key.
12. Activate 2-Step Verification.
13. Go back to the security tab.
14. Click on "App passwords".
15. Confirm your password again.
16. In "Select app" select "Other".
17. Give it the name "Python Emails", or something similar, so you can identify it.
18. Click on "generate".
19. Save the 16-character password that appears on the screen.
20. Use the Application password that you just generated to access the program.
