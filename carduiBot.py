# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: March 27th, 2025
# | Last update..: March 27th, 2025
# | WhatIs.......: EmailBot - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------

# ------------------------- Libraries -------------------------
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------------------- Variables -------------------------
carduibotEmail = "carduibot@gmail.com"
carduibotPassword = ""

myEmail = "vanessa@reteguin.com"

# -------------------------- Class ----------------------------
class EmailBot:
    def __init__(self):
        self.feeling = "good"

    def sendMail(self):
        # Send message with smtplib

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=carduibotEmail, password=carduibotPassword)
        connection.sendmail(from_addr=carduibotEmail,
                            to_addrs=myEmail,
                            msg="<h1>Holaaaaa! Esto es un prueba de una Manessa medio dormida :)</h1>")
        connection.close()