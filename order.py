class Order:
    """ Represents an order placed by a customer
        Attributes:
        __order_id (str): Unique identifier for the order.
        __customer (Customer): Reference to the customer who placed the order.
        __items (dict): A dictionary of items in the order, where each key is an item_id and the value is another dict with description, quantity, and unit_price
        __status (str): Current status of the order like Pending, Paid, Delivered
        __total_weight (float): Total weight of all items in the order
        __package_dimensions (str): Dimensions of the package """

    def __init__(self, order_id, customer, items,
                 status="Pending", total_weight=0.0,
                 package_dimensions="30x20x10 cm"):
        self.__order_id = order_id # Store order ID
        self.__customer = customer # Store customer details
        self.__items = items  # Store order items for example ITM001: (description: Widget, quantity: 2, unit_price: 50.0)
        self.__status = status # Order status default: Pending and such stuff
        self.__total_weight = total_weight # Store total package weight
        self.__package_dimensions = package_dimensions # store package size
    
    # Setters and Getters
    def get_order_id(self): #Returns the order ID
        return self.__order_id
    
    def get_customer(self): #Returns the customer who placed the order
        return self.__customer
    
    def get_items(self): #Returns the items in the order
        return self.__items
    
    def get_status(self): #Returns the current order status
        return self.__status

    def get_total_weight(self): #Returns the total weight of the package
        return self.__total_weight
    
    def get_package_dimensions(self): #Returns the package size
        return self.__package_dimensions
    
    def set_status(self, status): #Updates the order status
        self.__status = status

    def set_total_weight(self, weight): #Updates the total weight of the package
        self.__total_weight = weight
    
    def set_package_dimensions(self, dimensions): #Updates the package size 
        self.__package_dimensions = dimensions
    
    def calculate_subtotal(self): # Calculates the subtotal by summing quantity * unit_price for all items
        return sum(item["quantity"] * item["unit_price"] for item in self.__items.values())

    def calculate_taxes_and_fees(self, tax_rate=0.05): #Calculates taxes/fees based on the given tax rate default 5%
        return self.calculate_subtotal() * tax_rate

    def calculate_total_price(self): #Calculates the total price by adding the subtotal and the taxes/fees
        return self.calculate_subtotal() + self.calculate_taxes_and_fees()

    def update_order_status(self, new_status): #Updates the order status in a real system you'd validate logical transitions like Pending - Paid - Delivered
        self.__status = new_status
    
    def __str__(self): #Returns a formatted string summarizing the order and its items
        items_str = []         # Format each item in a table view
        header = f"{'ItemCode'.ljust(10)} {'Description'.ljust(20)} {'Qty'.ljust(5)} {'UnitPrice'.ljust(10)} {'Total'.ljust(10)}"
        divider = "-" * 60
        for code, item_data in self.__items.items():
            line = (f"{code.ljust(10)} " f"{item_data['description'].ljust(20)} " f"{str(item_data['quantity']).ljust(5)} " f"{str(item_data['unit_price']).ljust(10)} " f"{str(item_data['quantity'] * item_data['unit_price']).ljust(10)}" )
            items_str.append(line)
        
        items_joined = "\n".join(items_str)
        return ( f"Order ID: {self.__order_id}\n" f"Customer: {self.__customer.get_name()} (#{self.__customer.get_customer_id()})\n" f"Status: {self.__status}\n" f"Package Dimensions: {self.__package_dimensions}\n" f"Total Weight: {self.__total_weight} kg\n\n" f"Items in Order:\n{header}\n{divider}\n{items_joined}\n" f"{divider}\n" f"Subtotal: AED {self.calculate_subtotal():.2f}\n" f"Taxes & Fees: AED {self.calculate_taxes_and_fees():.2f}\n" f"Total: AED {self.calculate_total_price():.2f}\n" )