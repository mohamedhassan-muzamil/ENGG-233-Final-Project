import numpy as np
import matplotlib.pyplot as pyplot

def readFile(file_name):
    data = np.loadtxt(file_name, delimiter= ',', skiprows=1,
            usecols=(0,1,2,3,4), dtype=np.float)
    return data
def drawLineGraph(x,y,title,xlabel,ylabel):
    fig = pyplot.figure()
    pyplot.title(title)
    pyplot.ylabel(ylabel)
    pyplot.xlabel(xlabel)

    pyplot.plot(x,y,marker='o')
    pyplot.show()

Calgary_Weather = readFile("C:\\Users\\hamoo\\Desktop\\HelloWorldProject\\Project\\CalgaryWeather.csv")
AvgTempAnnual_List = []
j = 11
k = 0
for i in range (0,360,12):
            Temp_year = Calgary_Weather[i][0]
            AnnualTemp = []
            while k <= j:
                AnnualTemp.append((Calgary_Weather[k][2]+Calgary_Weather[k][3])/2)
                k += 1
                if k >= 359:
                    break
            AvgTemp = np.mean(AnnualTemp)
            AvgTempAnnual_List.append(str(Temp_year) + ":" + str(AvgTemp))
            j += 12
print(AvgTempAnnual_List)
# drawLineGraph(data_rainfall[:,0],data_rainfall[:,1],"rainfall info","year","rainfall")
# x = []
# y = []
# for i in range (121,132):
#     x.append(Calgary_Weather[i][1])
#     y.append(Calgary_Weather[i][3])
# drawLineGraph(x,y,"Temperatures in Calgary","Month","Temperatures")

