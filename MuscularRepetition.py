class MuscularRepetition(object):
    def __init__(self, name, min_reps_number, max_reps_number):
        """
            Number of repetion range for the muscular exercises
        """

        if not isinstance(min_reps_number, int):
            raise TypeError(min_reps_number)

        if not isinstance(max_reps_number, int):
            raise TypeError(max_reps_number)

        if min_reps_number < 0:
            raise ValueError(min_reps_number)

        if max_reps_number < max_reps_number:
            raise ValueError(max_reps_number)

        self.min_reps_number = min_reps_number
        self.max_reps_number = max_reps_number
        self.name = name