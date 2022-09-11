import numpy as np
import matplotlib.pyplot as pyplot
from FileIO import *
from Date import *
from TemperatureData import *
from WeatherAnalyzer import *

def main():
    Calgary_Weather = FileIO()
    Calgary_Weather_Data = Calgary_Weather.read_File()
    List_of_Years = []
    List_of_Months = []
    List_of_MaxTemp = []
    List_of_MinTemp = []
    List_of_Snowfall = []
    List_of_AvgTemp = []
    for i in range(359):
        Date_obj = Date(Calgary_Weather_Data[i][0],Calgary_Weather_Data[i][1])
        Tempdata_obj = TemperatureData(Date_obj,Calgary_Weather_Data[i][2],Calgary_Weather_Data[i][3],Calgary_Weather_Data[i][4])
        List_of_Years.append(Tempdata_obj.date_obj.Year)
        List_of_Months.append(Tempdata_obj.date_obj.Month)
        List_of_MaxTemp.append(Tempdata_obj.maxTemperature)
        List_of_MinTemp.append(Tempdata_obj.minTemperature)
        List_of_Snowfall.append(Tempdata_obj.Snowfall)
        List_of_AvgTemp.append((Tempdata_obj.minTemperature + Tempdata_obj.maxTemperature)/2)
    # List_of_MaxTemp = np.array_split(List_of_MaxTemp,30)
    List_of_MinTemp = np.array_split(List_of_MinTemp,30)
    List_of_Years = np.array_split(List_of_Years,30)
    List_of_Snowfall = np.array_split(List_of_Snowfall,30)
    List_of_AvgTemp = np.array_split(List_of_AvgTemp,30)
    np.set_printoptions(suppress=True)
    MaxTempData = WeatherAnalyzer(List_of_MaxTemp)
    MinTempData = WeatherAnalyzer(List_of_MinTemp)
    SnowfallData = WeatherAnalyzer(List_of_Snowfall)
    AvgTempData = WeatherAnalyzer(List_of_AvgTemp)
    # List_of_tempdata_obj = (List_of_Years,List_of_Months,List_of_MaxTemp,List_of_MinTemp,List_of_Snowfall)
    # List_of_tempdata_obj = np.vstack(List_of_tempdata_obj)
    # List_of_tempdata_obj = np.transpose(List_of_tempdata_obj)
    # np.set_printoptions(suppress=True)
    # weather_data = WeatherAnalyzer(List_of_tempdata_obj)
    while True:
        print("1- Get Minimum Temprature of 1990-2019")
        print("2- Get Maximum Temprature of 1990-2019")
        print("3- Get Minimum Temprature of 1990-2019 Annually")
        print("4- Get Maximum Temprature of 1990-2019 Annually")
        print("5- Get Average Snowfall between 1990-2019 Annually")
        print("Type exit to leave")
        x = input("Enter a number from 1 - 5 to select one of the options above: ")
        if x == "1":
            print(MinTempData.getMinTemp())
        elif x == "2":
            print(MaxTempData.getMaxTemp())
        elif x == "3":
            print(MinTempData.getMinTempAnnually())
        elif x == "4":
            print(MaxTempData.getMaxTempAnnually())
        elif x == "5":
            print(SnowfallData.getAvgSnowFallAnnually())
        elif x == "exit":
            break
        else:
            print("Invalid input")
main()
