import sys # Import the sys module for command line arguments

from formatting import format_message
from create_mail import myMail


def send(name = None, to_mail = None): # Define the send function with name and to_mail as arguments
    assert to_mail is not None # Check if to_mail is not None
    
    msg = format_message(name=name) # Format the message with the name provided as an argument to the function
    
    try:
        myMail(body=msg, to_mails=[to_mail], html = None) # Send the email with the formatted message and the receiver's email address as arguments to the function
        return True
    except Exception as e: # Catch any exceptions that occur during the execution of the try block and store them in the variable e
        # print(f"An error occurred: {e}")
        return False


if __name__ == '__main__':
    print(sys.argv) # Print the command line arguments
    name = "Unknown" # Set the default name

    if len(sys.argv) > 1: # Check if the length of sys.argv is greater than 1
        name = sys.argv[1] # Set the name to the first argument
    
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2] # Set the email to the second argument

    response = send(name, email) # Send the email

    if response:
        print("Email sent successfully!")
    else:
        print("Email not sent! Something went wrong.")