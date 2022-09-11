import numpy as np
class FileIO:
    def __init__(self):
        self.filePath = "C:\\Users\\hamoo\\Desktop\\HelloWorldProject\\Project\\CalgaryWeather.csv"

    def read_File(self):
        self.dataTable = (np.loadtxt(self.filePath, delimiter= ',', skiprows=1,
            usecols=(0,1,2,3,4), dtype=np.float))
        return self.dataTable
        