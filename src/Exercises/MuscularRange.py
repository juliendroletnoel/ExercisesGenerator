class MuscularRange (object):
    """
        Muscular Range defines the range of reps desired

        Bulky means less reps, higher weight
        Leans means more reps, lower weight

        Min and max of ranges must not overlap of leave gap

        ex:
        1 to 3
        4 to 9
        10 to 1000
    """
    def __init__(self):
        self.__muscular_types = []

    def add_muscular_range(self, name, min_reps, max_reps):
        """
            Add new muscular range
            if ranges overlap or leave gaps, range is not added
        """
        for muscular_type in self.__muscular_types:
            type_min_reps, type_max_reps = muscular_type.get_min_max_reps()
            if min_reps >= type_min_reps and min_reps <= type_max_reps or \
               max_reps >= type_min_reps and max_reps <= type_max_reps:
                raise ValueError("given range {} - {}, existing range {} - {}".format(min_reps, max_reps, type_min_reps, type_max_reps))

        self.__muscular_types.append(MuscularRep(name, min_reps, max_reps))

    def get_muscular_range(self, number_of_reps):
        """
            Returns the muscular type name based on range
            Returns False if not range match given number of reps
        """
        if not isinstance(number_of_reps, int):
            raise TypeError(number_of_reps)

        if number_of_reps < 0:
            raise ValueError(number_of_reps)

        for muscular_type in self.__muscular_types:
            type_min_reps, type_max_reps = muscular_type.get_min_max_reps()

            if type_min_reps <= number_of_reps or type_max_reps >= number_of_reps:
                return muscular_type.get_muscular_type_name()
        
        return False

    def get_muscular_ranges(self):
        ((e.get_muscular_type_name(), e.get_min_max_reps()) for e in self.__muscular_types)

class MuscularRep (object):
    def __init__(self, name, min_reps, max_reps):

        if not isinstance(name, str):
            raise TypeError(name)

        if not isinstance(min_reps, int):
            raise TypeError(min_reps)

        if not isinstance(max_reps, int):
            raise TypeError(max_reps)

        if min_reps < 0:
            raise ValueError(min_reps)

        if max_reps < 0 or max_reps < min_reps:
            raise ValueError(max_reps)

        self.__name = name.lower()
        self.__min_reps = min_reps
        self.__max_reps = max_reps

    def get_muscular_type_name(self):
        return self.__name

    def get_min_max_reps(self):
        return (self.__min_reps, self.__max_reps)
