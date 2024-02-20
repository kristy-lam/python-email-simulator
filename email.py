"""
Module defining classes `Email` and `Inbox`
"""


class Email():

    """
    The class `Email` represents an email with attributes such as email
    address, subject line, email content, and a method to mark the email as
    read.
    """

    def __init__(self, email_address, subject_line, email_content):

        """
        This method initializes an email object with attributes such as email
        address, subject line, email content, and a flag indicating whether the
        email has been read.
        
        :param email_address: The `email_address` parameter in the `__init__`
        method is used to store the email address of the recipient to whom the
        email will be sent. This parameter will be initialized when creating an
        instance of the class that contains this method
        :param subject_line: The `subject_line` parameter in the `__init__`
        method of the class is used to store the subject line of an email. It is
        a string that represents the subject or title of the email message
        :param email_content: The `email_content` parameter in the `__init__`
        method of a class typically represents the content or body of an email
        message. It could include the main message that the email is conveying,
        any attachments, formatting, or any other relevant information that the
        email contains
        """

        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):

        """
        This method sets the `has_been_read` attribute to True.
        """

        self.has_been_read = True


class Inbox():

    """
    The `Inbox` class represents an email inbox with methods to
    populate, list, read, list unread, and read unread emails.
    """

    def __init__(self, inbox):

        """
        The `__init__` method initializes an object with an empty inbox
        attribute.
        
        :param inbox: In the `__init__` method, the `inbox` parameter is 
        being passed to the method, but then immediately overwritten with 
        an empty list `[]`. The `self.inbox` attribute is then set to 
        this empty list.
        """

        inbox = []
        self.inbox = inbox

    def populate_inbox(self):

        """
        The `populate_inbox` method creates 3 sample emails and adds them 
        to the Inbox list.
        """

        sample_email_1 = Email("email_address_1@gmail.com",
                               "Sample Email 1",
                               "Dear Luke,\nHello World!\nKind regards,\nKristy")

        sample_email_2 = Email("email_address_2@gmail.com",
                               "Sample Email 2",
                               "Dear Luke,\nWelcome home!\nKind regards,\nKristy")

        sample_email_3 = Email("email_address_3@gmail.com",
                               "Sample Email 3",
                               "Dear Luke,\nCome back again!\nKind regards,\nKristy")

        self.inbox.append(sample_email_1)
        self.inbox.append(sample_email_2)
        self.inbox.append(sample_email_3)

    def list_emails(self):

        """
        The method iterates through the inbox emails and prints each 
        email's subject line with a corresponding number.
        """

        for email_num, email in enumerate(self.inbox, 1):
            list_emails = f"Email no. {email_num} - {email.subject_line}"
            print(list_emails)

    def read_email(self):

        """
        This method reads and displays an email from an inbox based on 
        user input.
        """

        while True:

            email_choice = int(input("Enter the email no. (e.g. '1'): "))

            try:

                if len(self.inbox) >= email_choice > 0:

                    for email_num, email in enumerate(self.inbox, 1):

                        if email_choice == email_num:
                            read_email = "*" * 80 + "\n"
                            read_email += f"From: \t\t{email.email_address}\n\n"
                            read_email += f"Subject: \t{email.subject_line}\n\n"
                            read_email += f"{email.email_content}\n" + "*" * 80
                            print(read_email)
                            # Once displayed, call the class method to set its
                            # 'has_been_read' variable to True
                            email.mark_as_read()
                            break

                    break

                # Print error message if user's input is out of range
                else:
                    print("Incorrect input - no such email.")

            # Print error message if ValueError is caught
            except ValueError:
                print("Incorrect input - enter a number (e.g. '1').")

    def list_unread_emails(self):

        """
        This method iterates through the inbox and prints the subject 
        line of unread emails along with a corresponding number.
        """

        for email_num, email in enumerate(self.inbox, 1):
            if email.has_been_read is False:
                list_emails = f"Email no. {email_num} - {email.subject_line}"
                print(list_emails)

    def read_unread_email(self):

        """
        This method allows a user to select and display a specific
        unread email from an inbox.
        """

        while True:

            email_choice = int(input("Enter the email no. (e.g. '1'): "))

            try:

                if len(self.inbox) >= email_choice > 0:

                    for email_num, email in enumerate(self.inbox, 1):

                        if email_choice == email_num and email.has_been_read is False:
                            read_email = "*" * 80 + "\n"
                            read_email += f"From: \t\t{email.email_address}\n\n"
                            read_email += f"Subject: \t{email.subject_line}\n\n"
                            read_email += f"{email.email_content}\n" + "*" * 80
                            print(read_email)
                            # Once displayed, call the class method to set its
                            # 'has_been_read' variable to True.
                            email.mark_as_read()
                            break

                        elif email_choice == email_num and email.has_been_read is True:
                            print("Incorrect input - this email has been read.")

                    break

                # Print error message if user's input is out of range
                else:
                    print("Incorrect input - no such email.")

            # Print error message if ValueError is caught
            except ValueError:
                print("Incorrect input - enter a number (e.g. '1').")


"""
Module creating an instance of the `Inbox` class named `my_inbox`, and 
populating it with sample emails using the `populate_inbox` method.
"""

my_inbox = Inbox("my_inbox")
my_inbox.populate_inbox()

MENU = True

while True:

    try:

        user_choice = int(input('''\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: '''))

        if user_choice == 1:

            # Read an email
            my_inbox.list_emails()
            my_inbox.read_email()

        elif user_choice == 2:

            # View unread emails
            my_inbox.list_unread_emails()
            my_inbox.read_unread_email()

        elif user_choice == 3:

            # Quit appplication
            print("Goodbye!")
            exit()

        else:
            print("Oops - incorrect input.")

    except ValueError:
        print("Incorrect input - please enter a number.")
