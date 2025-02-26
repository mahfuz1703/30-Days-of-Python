import imaplib # Importing the imaplib module for accessing emails
import email # Importing the email module for parsing emails


host = 'imap.gmail.com' # The email host
username = 'Your email'
password = 'Your email app password'

def myInbox():
    mail = imaplib.IMAP4_SSL(host) # Create an IMAP4_SSL object for the email host with SSL encryption 
    mail.login(username, password) # Login to the email host with the username and password
    mail.select('inbox') # Select the inbox folder of the email account 
    status, search_dta = mail.search(None, 'UNSEEN') # Search for unread emails in the inbox folder 

    if status != 'OK': # Check if the status is not OK 
        print("No messages found!")
        return []

    messages = [] # Create an empty list for the messages

    for num in search_dta[0].split()[:3]: # Iterate over the first 3 unread emails in the inbox 
        email_dta = {} # Create an empty dictionary for the email data

        status, data = mail.fetch(num, '(RFC822)') # Fetch the email data in RFC822 format (raw email) 

        if status != 'OK':
            print(f"Failed to fetch email with ID {num}")
            continue

        raw_email = data[0][1] # Get the raw email data from the fetched data
        msg = email.message_from_bytes(raw_email) # Parse the raw email data into a message object

        for header in ['subject', 'to', 'from', 'date']: # Iterate over the headers of the email message object
            email_dta[header] = msg[header] # Get the value of the header and store it in the email data dictionary

        for part in msg.walk(): # Iterate over the parts of the email message object
            if part.get_content_type() == 'text/plain': # Check if the content type is plain text 
                body = part.get_payload(decode=True).decode() # Get the plain text body of the email and decode it 
                email_dta['body'] = body # Store the plain text body in the email data dictionary
            elif part.get_content_type() == 'text/html': # Check if the content type is HTML 
                html = part.get_payload(decode=True).decode() # Get the HTML body of the email and decode it
                email_dta['html'] = html # Store the HTML body in the email data dictionary
                 
        messages.append(email_dta) # Append the email data to the message list

    return messages # Return the message list

if __name__ == '__main__':
    messages = myInbox() # Get the messages from the inbox
    for msg in messages:  # Iterate over the messages
        print(f"Subject: {msg['subject']}")  # Print the subject of the email
        print(f"To: {msg['to']}")  # Print the receiver of the email
        print(f"From: {msg['from']}")  # Print the sender of the email
        print(f"Date: {msg['date']}")  # Print the date of the email
        print(f"Body: {msg.get('body', 'No plain text body')}")  # Print the body of the email
        print(f"HTML: {msg.get('html', 'No HTML body')}")  # Print the html of the email
        print("\n")  # Print a new line


    # print(messages) # Print the messages



