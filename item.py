class Item:
    """ Represents an individual product or item in the system
    Attributes:
        __item_id (str): Unique identifier for the item.
        __name (str): Name of the item.
        __description (str): Brief description of the item.
        __price (float): Unit price of the item.
        __stock (int): Available stock quantity """

    def __init__(self, item_id, name, description, price, stock):
        self.__item_id = item_id # Store the unique item ID
        self.__name = name # Store the item name
        self.__description = description # Store the item description
        self.__price = price # Store the item price
        self.__stock = stock # Store the available stock quantity
    
    # Setters and Getters
    def get_item_id(self): #Returns the item ID
        return self.__item_id
    
    def get_name(self): #Returns the item name
        return self.__name
    
    def get_description(self): #Returns the item description
        return self.__description
    
    def get_price(self): #Returns the item price
        return self.__price
    
    def get_stock(self): #Returns the available stock quantity
        return self.__stock
    
    def set_name(self, name): #Updates the item name
        self.__name = name
    
    def set_description(self, description): # Updates the item description
        self.__description = description
    
    def set_price(self, price): #Updates the item price
        self.__price = price
    
    def set_stock(self, stock): #Updates the available stock quantity
        self.__stock = stock
    
    # Example Stub Method
    def reduce_stock(self, quantity):
        """ Reduces the item's stock by the given quantity if enough stock is available """
        pass
    
    def __str__(self):
        """ Returns a basic string representation of the item """
        return (f"Item ID: {self.__item_id}, " f"Name: {self.__name}, " f"Price: AED {self.__price}, " f"Stock: {self.__stock}")