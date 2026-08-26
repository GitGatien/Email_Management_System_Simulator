import datetime

class Email:
    '''
    Class to create email objects
    '''
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    # This method changes the email status to read
    def mark_as_read(self):
        self.read = True

    # This method displays the full email content
    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    # This is a 'magic method' that shows Python how to print an email
    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


#-----------------------------------------------------------------------------------------------------------------------------
class User:
    '''
    Class to create users
    '''
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    # This allows a user to send an email to a receiver
    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # This allows a user to check their inbox
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    # This allows a user to read a specific email
    def read_email(self, index):
        self.inbox.read_email(index)

    # This allows a user to delete a specific email
    def delete_email(self, index):
        self.inbox.delete_email(index)

#-----------------------------------------------------------------------------------------------------------------------------
class Inbox:
    '''
    This class allows users to have their own box to store emails
    '''
    def __init__(self):
        self.emails = []

    # This appends a new email to the inbox list
    def receive_email(self, email):
        self.emails.append(email)

    # This lists all the emails currently in the inbox
    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    # This checks if the email exists in the inbox before displaying it
    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    # This checks if the email exists in the inbox before deleting it
    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')
