import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_emails(email_list_file, message_file, sender_email, sender_password):
    try:
        with open(email_list_file, "r") as file:
            recipients = [line.strip() for line in file.readlines() if line.strip()]
        
        with open(message_file, "r") as file:
            message_content = file.read().strip()
        
        if not recipients:
            print("Error: No recipients found.")
            return
        if not message_content:
            print("Error: The message file is empty.")
            return
        
        subject = "Automated Email"
        
        smtp_server = "smtp.gmail.com"
        port = 465  # SSL port
        
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            
            for recipient in recipients:
                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = recipient
                msg["Subject"] = subject
                msg.attach(MIMEText(message_content, "plain"))
                
                server.sendmail(sender_email, recipient, msg.as_string())
                print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    email_list = "emails.txt"  # File containing recipient emails (one per line)
    message_file = "message.txt"  # File containing the email content
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"  # Consider using an App Password
    
    send_emails(email_list, message_file, sender_email, sender_password)
