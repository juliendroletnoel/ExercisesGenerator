from ItemType import ItemType

class Item:

    def __init__(self, itemType, quantity):
        
        if not isinstance(itemType, ItemType):
            raise TypeError(itemType)

        if not isinstance(quantity, int):
            raise TypeError(quantity)
        
        if quantity <= 0:
            raise ValueError(quantity)
        
        self.item_type = type(itemType)
        self.quantity = quantity

    def get_item_type(self):
        return self.item_type
    
    def get_quantity(self):
        return self.quantity

    def add_or_substract_quantity(self, quantity):
        """
        Add or substract an item quantity (can't be set to a negative quantity)
        """
        if not isinstance(quantity, int):
            raise TypeError(quantity)
        if self.quantity - quantity < 0 :
            raise ValueError('{} quanity can''t be negative'.format(self.item_type), quantity)

        self.quantity += quantity