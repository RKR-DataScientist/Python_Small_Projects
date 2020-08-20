import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

data = pd.read_excel("Your Excel location")

# TO get the columns from the email
email_col = data.get("email")
list_of_email = list(email_col)
print(list_of_email)

try:
    server = sm.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("ravikrrahul0@gmail.com", "Password")

    from = "ravikrrahul0@gmail.com"
    to_ = list_of_email

    message = MIMEMultipart("alternative")
    message['from'] = "ravikrrahul0@gmail.com"
    message['Subject'] = "This email has been sended by python testing"

    html = '''
    <html>
    <head>
    
    </head>
    <body>
        <h1> <\h1>
        <h2> <\h1>
        <p>  </p>
        <button style="padding:20px; background:green; color:white;"> Verify </button>
        
    </body>
    
    '''
    text = MIMEText(html, "html")
    message.attach(text)

    server.send(from_, to_, message.as_string())
    print("Message has been sent on email")

except Exception as e:
    print(e)




