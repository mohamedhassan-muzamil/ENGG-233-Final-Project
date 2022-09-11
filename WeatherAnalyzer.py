import numpy as np
import matplotlib.pyplot as pyplot

class WeatherAnalyzer:
    def __init__(self,tempData_obj_list):
        self.tempData_obj_list = tempData_obj_list

    def getMinTemp(self):
        minList = []
        for i in range(30):
            minList.append(np.min(self.tempData_obj_list[i]))
        minTemp = np.min(minList)
        return minTemp

    def getMinTempAnnually(self):
        AnnualMinTemp_List = []
        for i in range (30):
                AnnualMinTemp_List.append(np.min(self.tempData_obj_list[i]))
        return AnnualMinTemp_List
               

    def getMaxTemp(self):
        maxList = []
        for i in range(30):
            maxList.append(np.max(self.tempData_obj_list[i]))
        maxTemp = np.max(maxList)
        return maxTemp

    def getMaxTempAnnually(self):
        AnnualMaxTemp_List = []
        for i in range (30):
                AnnualMaxTemp_List.append(np.max(self.tempData_obj_list[i]))
        return AnnualMaxTemp_List

    def getAvgSnowFallAnnually(self):
        AvgSnowFallAnual_List = []
        for i in range (30):
                AvgSnowFallAnual_List.append(np.mean(self.tempData_obj_list[i]))
        return AvgSnowFallAnual_List

    def getAvgTempAnnually(self,other):
        AvgTempAnnualy_List = []
        for i in range (30):
            AvgTemp = ((self.tempData_obj_list[i]+other[i])/2)
            AvgTempAnnualy_List.append(np.mean(AvgTemp))
        return AvgTempAnnualy_List