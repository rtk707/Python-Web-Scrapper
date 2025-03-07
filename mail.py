import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail:

    def send_email(self,subject, body, to_email):
        
        from_email = os.getenv('EMAIL_ID')
        password = os.getenv('GMAIL_PASSWORD')
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(from_email, password)
                text = msg.as_string()
                server.sendmail(from_email, to_email, text)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

