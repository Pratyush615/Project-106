import plotly.express as px
import csv
import numpy as np

#with open("cups of coffee vs hours of sleep.csv") as csv_file:
  #  df=csv.DictReader(csv_file)
 #   fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
# fig.show()

def getDataSource(data_path):
    coffee = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))
    return{"x":coffee,"y":hours_of_sleep}
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("The correlation between coffee and hours of sleep is ", correlation[0,1])

def main():
    data_path = "cups of coffee vs hours of sleep.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

main()
