

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self) -> None:
        """
        Function initializes Television objects
        Instance variables for power, mute, volume, and channel are initialized
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Function negates current power status when called, turning on or off the TV
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Function negates current mute status when called
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Function lowers channel by 1
        If TV is at maximum channel, function will set channel to minimum channel
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    def channel_down(self) -> None:
        """
        Function lowers channel by 1
        If TV is at minimum channel, function will set channel to maximum channel
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Function lowers volume by 1
        If maximum volume is reached, function will leave TV at maximum volume
        Function removes mute on TV when called
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if not(self.__volume == Television.MAX_VOLUME):
                self.__volume += 1
    def volume_down(self) -> None:
        """
        Function lowers volume by 1
        If minimum volume is reached, function will leave TV at minimum volume
        Function removes mute on TV when called
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if not(self.__volume == Television.MIN_VOLUME):
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Function changes the default str function to print the power status, current channel, and current volume
        :return: String
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


