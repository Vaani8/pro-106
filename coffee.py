import csv
import numpy as np
import plotly.express as px

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hour = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hour.append(float(row["sleep in hours"]))

    return {"x" : coffee_in_ml, "y": sleep_in_hour}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee( in ml ) and sleep ( in hour ) :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data2.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
