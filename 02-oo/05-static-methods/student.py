class Duration:
    def __init__(self, seconds,minutes,hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours

    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def hours(self):
        return self.__hours

    @staticmethod
    def from_seconds(time):
        return Duration(time,time/60,time/3600)
    
    @staticmethod
    def from_minutes(time):
        return Duration(time*60,time,time/60)
    
    @staticmethod
    def from_hours(time):
        return Duration(time*3600,time*60,time)