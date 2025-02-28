class DeliveryNote:
    """ Represents a delivery note or receipt for an order.
        Attributes:
        __note_id (str): Unique identifier for the note
        __order (Order): The order associated with this delivery note
        __delivery_date (str): Scheduled or actual delivery date
        __recipient_signature (str): Name or signature of the recipient
        __delivery_method (str): its Optional like Courier, Express if needed """

    def __init__(self, note_id, order, delivery_date, recipient_signature, delivery_method="Courier"):
        self.__note_id = note_id
        self.__order = order
        self.__delivery_date = delivery_date
        self.__recipient_signature = recipient_signature
        self.__delivery_method = delivery_method  # Additional attribute to reach 5 total

    # Setters and Getters
    def get_note_id(self): # Returns the delivery note ID
        return self.__note_id

    def get_order(self): # Returns the order linked to this delivery note
        return self.__order

    def get_delivery_date(self):
        return self.__delivery_date

    def get_recipient_signature(self):
        return self.__recipient_signature

    def get_delivery_method(self):
        return self.__delivery_method

    def set_delivery_date(self, date): # Updates the delivery date
        self.__delivery_date = date

    def set_recipient_signature(self, signature):  # Updates the recipient's signature
        self.__recipient_signature = signature

    def set_delivery_method(self, method):
        self.__delivery_method = method

    # Example 
    def generate_note_details(self):
        """ Returns a string with the relevant delivery note details """
        pass

    def __str__(self):
        """ Return a string that closely matches the sample delivery note layout """
        # Pull data from the order and customer
        customer = self.__order.get_customer()
        subtotal = self.__order.calculate_subtotal()
        taxes = self.__order.calculate_taxes_and_fees(0.05)
        total = self.__order.calculate_total_price()  # or (subtotal + taxes)

        # Build item details like a small table
        item_lines = []
        for code, data in self.__order.get_items().items():
            line = (
                f"{code}\t{data['description']}\t"
                f"{data['quantity']}\t"
                f"{data['unit_price']:.2f}\t"
                f"{data['quantity'] * data['unit_price']:.2f}"
            )
            item_lines.append(line)
        items_joined = "\n".join(item_lines)

        return (
            "Delivery Note\n"
            "Thank you for using our delivery service! Please print your delivery receipt and "
            "present it upon receiving your items.\n\n"

            f"Recipient Details:\n"
            f"Name: {customer.get_name()}\n"
            f"Contact: {customer.get_email()}\n"
            f"Delivery Address: {customer.get_address()}\n\n"

            "Delivery Information:\n"
            f"Order Number: {self.__order.get_order_id()}\n"
            f"Reference Number: {self.__note_id}\n"
            f"Delivery Date: {self.__delivery_date}\n"
            f"Delivery Method: {self.__delivery_method}\n"
            f"Package Dimensions: {self.__order.get_package_dimensions()}\n"
            f"Total Weight: {self.__order.get_total_weight()} kg\n\n"

            "Summary of Items Delivered:\n"
            "Item Code\tDescription\tQuantity\tUnit Price (AED)\tTotal Price (AED)\n"
            "---------------------------------------------------------------------\n"
            f"{items_joined}\n\n"
            f"Subtotal: AED {subtotal:.2f}\n"
            f"Taxes and Fees: AED {taxes:.2f}\n"
            f"Total Charges: AED {total:.2f}" )