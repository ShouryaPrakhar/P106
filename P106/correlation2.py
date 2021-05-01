import numpy as np 
import plotly.express as px
import csv
def getDataSource(data_path):
    MarksInPercentage = []
    DaysPresent = []
    with open(data_path) as csvFiles:
        csv_reader = csv.DictReader(csvFiles)
        for row in csv_reader:
            MarksInPercentage.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))
    return {"x":MarksInPercentage,"y":DaysPresent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"] , datasource["y"])
    print("Correlation:", correlation[0,1])

def setup():
    data_path = "data3.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()                   
