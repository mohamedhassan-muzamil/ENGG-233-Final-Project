import numpy as np
class TemperatureData:
    def __init__(self,date_obj,maxTemperature,minTemperature,Snowfall):
        self.date_obj = date_obj
        self.maxTemperature = maxTemperature
        self.minTemperature = minTemperature
        self.Snowfall = Snowfall
        