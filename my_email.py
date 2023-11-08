import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#import CVS
import csv

# Set your Gmail email and password (or App Password)
sender_email = "omarfarahat@patroneg.com"
sender_password = "OMAR@12345"
# for OFIC email sender_password = "lqgl evmd xkvn ahkc"

#use the open function to read CSV file for Schools
with open('schools_emails.csv', 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Read the header row
    header = next(csv_reader)

    # Initialize an empty list for the dictionaries
    recipients_schools = []

    # Iterate through the rows and convert them to dictionaries
    for row in csv_reader:
       row_dict = {header[i]: row[i] for i in range(len(header))}
       recipients_schools.append(row_dict)
    #Test to see the recipients in the list
    #print(recipients_schools)

#use the open function to read CSV file for VCs
with open('vcs_emails.csv', 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Read the header row
    header = next(csv_reader)

    # Initialize an empty list for the dictionaries
    recipients_vcs = []

    # Iterate through the rows and convert them to dictionaries
    for row in csv_reader:
       row_dict = {header[i]: row[i] for i in range(len(header))}
       recipients_vcs.append(row_dict)
    #Test to see the recipients in the list
    #print(recipients_vcs)

#use the open function to read CSV file for lenders
with open('lenders_emails.csv', 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Read the header row
    header = next(csv_reader)

    # Initialize an empty list for the dictionaries
    recipients_lenders = []

    # Iterate through the rows and convert them to dictionaries
    for row in csv_reader:
       row_dict = {header[i]: row[i] for i in range(len(header))}
       recipients_lenders.append(row_dict)

    #Test to see the recipients in the list
    #print(recipients_lenders)

# List of recipients and their names
# recipients = [
#     {"email": "omar_farahat@live.com", "name": "Omar"},
#     {"email": "farah.leila@hotmail.com", "name": "Farah"},
#     {"email" : "ahmedfayed@patroneg.com", "name" : "Ahmed Alaa" }
# ]

#create a function to send emails
def start_sending(list_selected):
    """
    This is a function to start sending emails to a certain list
    
    The arguments contain the intended list to send the email to. 

    The message is predefined globally and independtn of this function this function
        
    """
    
    # Create the common email message
    subject = "Hello from Omar V1.3"
    message_text = f"This is a test email sent from my first Python code to send emails in bulks. \nI hope you can receive this!"

    # Connect to the Gmail SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

# Send personalized emails to each recipient with Bcc. This is based on the list type entered by the user
    for list_selected in list_selected:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["Subject"] = subject

        # Customize the email content for each recipient
        message_text = f"Hello, {list_selected['name']}!\nThis is a customized test email sent from my first Python code to send emails in bulks. \nI hope you can receive this!"
        msg.attach(MIMEText(message_text, "plain"))

        # Use Bcc to hide other recipients' email addresses
        msg["Bcc"] = list_selected["email"]

        # Send the email
        server.sendmail(sender_email, [list_selected["email"]], msg.as_string())
    
    #Test to see the recipients in the list
    print(list_selected)
    # Quit the server
    server.quit()

#choose which list you want to send an email to 
## recipients_vcs or recipient_lenders or reciepient_schools ##
start_sending(recipients_vcs)
