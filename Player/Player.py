# Player class
class Player:
    def __init__(self, full_name, nick_name, year_of_birth=0, player_identificator=0):
        if not type(year_of_birth) is int or year_of_birth < 0:
            raise TypeError(str(year_of_birth) + ' must be a positive integer')

        self.__player_full_name = full_name
        self.__player_year_of_birth = year_of_birth
        self.__player_nick_name = nick_name
        self.__player_identificator = player_identificator

    def display_player(self):
        print ('{} ({})'.format(self.__player_nick_name, self.__player_full_name))

    def get_player_full_name(self):
        return self.__player_full_name

    def get_player_identificator(self):
        return self.__player_identificator
