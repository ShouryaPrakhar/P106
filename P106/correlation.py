import numpy as np 
import plotly.express as px
import csv
def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csvFiles:
        csv_reader = csv.DictReader(csvFiles)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x":coffee,"y":sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"] , datasource["y"])
    print("Correlation:", correlation[0,1])

def setup():
    data_path = "data1.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()                   
