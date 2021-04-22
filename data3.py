import csv
import pandas as pd
import plotly.figure_factory as pf
import plotly.graph_objects as go
import statistics
import random

#Data Sample 1
file1 = pd.read_csv('studentMarks.csv')
fileList1 = file1["Math_score"].tolist()

figure2 = pf.create_distplot([fileList1], ['Data Sample Math scores - 3'], show_hist=False)
#figure2.show()

mean1 = statistics.mean(fileList1)
print('Mean of data sample 3: ', mean1)

sd1 = statistics.stdev(fileList1)
print('Standard Deviation of data sample 3: ', sd1)

meanList = []

def randomSetOfMeans(counter):
	data = []
	for i in range(0, counter):
		randomIndex = random.randint(0, len(fileList1) - 1)
		value = fileList1[randomIndex]
		data.append(value)
	mean = statistics.mean(data)
	return mean

for i in range(0, 1000):
	setOfMeans = randomSetOfMeans(100)
	meanList.append(setOfMeans)

firstSdStart, firstSdEnd = mean1 - sd1, mean1 + sd1
secondSdStart, secondSdEnd = mean1 - 2*sd1, mean1 + 2*sd1
thirdSdStart, thirdSdEnd = mean1 - 3*sd1, mean1 + 3*sd1

data3File = pd.read_csv("data3.csv")
data3FileList = data3File["Math_score"].tolist()

meanSample3 = statistics.mean(data3FileList)

fig = pf.create_distplot([meanList], ['Student Marks'], show_hist = False)

fig.add_trace(go.Scatter(x=[mean1, mean1], y=[0, 0.17], mode="lines", name="Mean"))

#fig.add_trace(go.Scatter(x=[firstSdStart, firstSdStart], y=[0, 0.17], mode="lines", name="First Standard Deviation Start - Data Sample"))
#fig.add_trace(go.Scatter(x=[firstSdEnd, firstSdEnd], y=[0, 0.17], mode="lines", name="First Standard Deviation End - Data Sample"))

fig.add_trace(go.Scatter(x=[meanSample3, meanSample3], y=[0, 0.17], mode="lines", name="Workshops"))

fig.add_trace(go.Scatter(x=[secondSdStart, secondSdStart], y=[0, 0.17], mode="lines", name="Second Standard Deviation Start - Data Sample"))
fig.add_trace(go.Scatter(x=[secondSdEnd, secondSdEnd], y=[0, 0.17], mode="lines", name="Second Standard Deviation End - Data Sample"))

fig.add_trace(go.Scatter(x=[thirdSdStart, thirdSdStart], y=[0, 0.17], mode="lines", name="Third Standard Deviation Start - Data Sample"))
fig.add_trace(go.Scatter(x=[thirdSdEnd, thirdSdEnd], y=[0, 0.17], mode="lines", name="Third Standard Deviation End - Data Sample"))

fig.show()


zscore = (meanSample3 -mean1)/sd1
print(zscore)