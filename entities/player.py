class Player:
    """An object of Player"""
    def __init__(self, name, level, friend_list):
        """
        Initialize a Player with the following attributes:
        name: String
        level: int
        friend_list: List[Player]
        """
        self.name = name
        self.level = level
        self.friend_list = friend_list

    def set_name(self, name):
        """Set name of player"""
        self.name = name

    def set_level(self, level):
        """Set level of player"""
        self.level = level

    def set_friend_list(self, friend_list):
        """"""
        self.friend_list = friend_list

    def get_name(self) -> String:
        """Return name of player"""
        return self.name

    def get_level(self) -> int:
        """Return level of player"""
        return self.level

    def get_friend_list(self) -> List[Player]:
        """Return Player's friend list"""
        return self.friend_list

# ToDo: Privatize appropriate attributes
