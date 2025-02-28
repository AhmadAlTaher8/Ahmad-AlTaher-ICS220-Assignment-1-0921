class Customer:
    """ Represents a customer in the delivery management system.
    Attributes:
        __customer_id (str): Unique identifier for the customer
        __name (str): Full name of the customer
        __email (str): Email address for notifications
        __address (str): Shipping address for deliveries
        __phone (str): Contact phone number """

    def __init__(self, customer_id, name, email, address, phone): # Creates a new customer with their ID, name, email, address, and phone number
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__address = address
        self.__phone = phone
    
    # Setters and Getters
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone


    def set_name(self, name): # Updates the customer's name
        self.__name = name
    
    def set_email(self, email): # Updates the customer's email address
        self.__email = email
    
    def set_address(self, address): # Updates the customer's address
        self.__address = address
    
    def set_phone(self, phone): # Updates the customer's phone number
        self.__phone = phone
    
    # Example Stub Method
    def validate_contact_details(self):
        """ Validates the customer's contact details

        Possible implementation:
        1. Check if email contains '@' and a valid domain.
        2. Check if phone is numeric and has a valid length.
        3. Return True if valid, otherwise False. """
        pass

    def __str__(self):
        """ Return a user-friendly string representation of the customer """
        return (
            f"Name: {self.__name}\n"
            f"Email: {self.__email}\n"
            f"Address: {self.__address}\n"
            f"Phone: {self.__phone}"
        )
