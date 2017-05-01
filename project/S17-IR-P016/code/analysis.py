
import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("//opt/predict/data/Customer_Data2.csv")
a="//opt/predict/data/"


def plot5(a):
    df.PaymentMethod.value_counts().plot(kind='bar')
    plt.savefig(a+"Count.png")
    plt.clf()


def plot6(a):
    df.boxplot(column="MonthlyCharges", by="Churn")
    plt.savefig(a+"Boxplot1.png")
    plt.clf()


def plot7(a):
    df.boxplot(column="MonthlyCharges", by="gender")
    plt.savefig(a+"Boxplot2.png")
    plt.clf()

def plot8(a):
    plt.scatter(df.tenure,df.MonthlyCharges)
    plt.savefig(a+"scatterplot.png")
    plt.clf()


plot5(a)
plot6(a)
plot7(a)
plot8(a)
