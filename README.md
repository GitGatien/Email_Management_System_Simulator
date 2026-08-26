Email Management System
Description

This is a small Python project that simulates a basic email system.

The program allows users to send emails to each other and manage the emails they receive in their inbox.

I made this project to practice object-oriented programming in Python.

Features
Create users
Send emails between users
Receive emails in an inbox
Check the inbox
Read an email
Mark an email as read
Delete an email
Show the date and time when an email was received
Classes

The project contains three classes:

Email

This class represents an email.

It stores:

The sender
The receiver
The subject
The body
The date and time
The read/unread status

It also has a method to display the complete email.

User

This class represents a user.

Each user has their own inbox.

A user can:

Send an email
Check their inbox
Read an email
Delete an email
Inbox

This class manages the emails received by a user.

It stores the emails in a list and contains methods to:

Receive an email
Display the emails
Read an email
Delete an email
Python concepts used

This project helped me practice:

Classes and objects
Methods
Constructors
Lists
Conditional statements
datetime
F-strings
The __str__() method
How it works

When a user sends an email, an Email object is created.

The email is then added to the receiver's inbox.

When the receiver reads the email, it is automatically marked as read.

For example:

alice = User("Alice")
bob = User("Bob")

alice.send_email(bob, "Hello", "How are you?")

bob.check_inbox()
bob.read_email(1)

Project goal

The main goal of this project was to practice Python OOP and understand how different classes can interact with each other.

Requirements
Python 3
Author

Created as a Python practice project.