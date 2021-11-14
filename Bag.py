from Item import Item
from Errors.Errors import *

class Bag(object):
    
    def __init__(self, max_capacity=70):
        ''' Bag initialization'''

        self.max_items_quantity = max_capacity
        self.item_list = []

    def upgrade_max_capacity_in_bag(self, added_max_capacity_value):
        '''Upgrade max capaicty in bag '''

        if not isinstance(added_max_capacity_value, int):
            raise TypeError(added_max_capacity_value)
        if added_max_capacity_value < 0:
            raise ValueError(added_max_capacity_value)
        self.max_items_quantity += added_max_capacity_value

    def add_item_in_bag(self, new_item):
        """
            Add an item to the bag
            If the item is existing, the quantity is updated
            else, the new item is added to the bag

            Raise a BagCapacityError if the bag max quantity is already matched
        """
        
        # Check item provided is an Item
        if not isinstance(new_item, Item):
            raise TypeError(new_item)
        
        available_space_in_bag = self.max_items_quantity - self.get_items_bag_quantity()  
        if available_space_in_bag <= 0:
            raise BagCapacityError('Bag item maximum quantity {} is reached'.format(self.max_items_quantity))

        # if the item quantity added to the current items is superior, remove what can't fit in the bag
        changed_quantity = available_space_in_bag - new_item.get_quantity()
        if changed_quantity < 0:
            new_item.add_or_substract_quantity(changed_quantity)

        # Add quantity to same item (if found)
        for item in self.item_list:
            if item.get_item_type() == new_item.get_item_type():
                item.add_or_substract_quantity(new_item.get_quantity())
                return True
        
        # Add bew item to list
        self.item_list.append(new_item)
        
        return True

    def remove_item_from_bag(self, old_item):
        """
            Remove an item quantity from the bag
            Checks if the asked quantity is available

            Raises an InsufficientItemError if not
        """
        if not isinstance(old_item, Item):
            raise TypeError(old_item)
        
        for item in self.item_list:
             if old_item.get_item_type() == item.get_item_type():
                if old_item.get_quantity() < item.get_quantity():
                    item.add_or_substract_quantity(old_item.get_quantity() * -1)
                    return True
                elif old_item.get_quantity() == item.get_quantity():
                    self.item_list.remove(item)
                    return True
                else:
                    raise InsufficientItemError("{} quantity is {}, needed is {}".format(old_item.get_item_type(), item.get_quantity(), old_item.get_quantity()))

        raise InsufficientItemError("{} item does exists in the bag".format(old_item.get_item_type()))

    def get_item_by_item_type(self, item_type):

        """
            Retreive item from bag based on item_type
        """
        item = [item for item in self.item_list if item_type in item.item_type]

        if len(item) == 0:
            return None
        else:
            return item[0]

    def get_items_bag_quantity(self):
        return sum([i.get_quantity() for i in self.item_list])