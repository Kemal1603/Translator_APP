import pandas

data = pandas.read_csv("language.csv")
a = [i for i in data['Turkish']]
print(a)
