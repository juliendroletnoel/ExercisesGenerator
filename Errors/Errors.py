class BagCapacityError(ValueError):
    """
        Bag capacity is max out
    """
    pass

class InsufficientItemError(ValueError):
    """
        Item quantity is insuffisient
    """
    pass