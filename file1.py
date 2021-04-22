import csv
import pandas as pd
import plotly.figure_factory as pf
import plotly.graph_objects as go
import statistics
import random

#Original Data
orgfile = pd.read_csv('studentMarks.csv')
orgfileList = orgfile["Math_score"].tolist()

figure1 = pf.create_distplot([orgfileList], ['Math scores of Original Data'], show_hist=False)
#figure1.show()

mean1 = statistics.mean(orgfileList)
print('Mean of math scores: ', mean1)

sd1 = statistics.stdev(orgfileList)
print('Standard Deviation of math scores: ', sd1)

meanList = []

def randomSetOfMeans(counter):
	data = []
	for i in range(0, counter):
		randomIndex = random.randint(0, len(orgfileList) - 1)
		value = orgfileList[randomIndex]
		data.append(value)
	mean = statistics.mean(data)
	return mean

for i in range(0, 1000):
	setOfMeans = randomSetOfMeans(100)
	meanList.append(setOfMeans)

firstSdStart, firstSdEnd = mean1 - sd1, mean1 + sd1
secondSdStart, secondSdEnd = mean1 - 2*sd1, mean1 + 2*sd1
thirdSdStart, thirdSdEnd = mean1 - 3*sd1, mean1 + 3*sd1

fig = pf.create_distplot([meanList], ['Student Marks'], show_hist = False)

fig.add_trace(go.Scatter(x=[mean1, mean1], y=[0, 0.17], mode="lines", name="Mean"))

fig.add_trace(go.Scatter(x=[firstSdStart, firstSdStart], y=[0, 0.17], mode="lines", name="First Standard Deviation Start"))
fig.add_trace(go.Scatter(x=[firstSdEnd, firstSdEnd], y=[0, 0.17], mode="lines", name="First Standard Deviation End"))

fig.add_trace(go.Scatter(x=[secondSdStart, secondSdStart], y=[0, 0.17], mode="lines", name="Second Standard Deviation Start"))
fig.add_trace(go.Scatter(x=[secondSdEnd, secondSdEnd], y=[0, 0.17], mode="lines", name="Second Standard Deviation End"))

fig.add_trace(go.Scatter(x=[thirdSdStart, thirdSdStart], y=[0, 0.17], mode="lines", name="Third Standard Deviation Start"))
fig.add_trace(go.Scatter(x=[thirdSdEnd, thirdSdEnd], y=[0, 0.17], mode="lines", name="Third Standard Deviation End"))

fig.show()




#Data Sample 1
file1 = pd.read_csv('data1.csv')
fileList1 = file1["Math_score"].tolist()

figure2 = pf.create_distplot([fileList1], ['Data Sample Math scores - 1'], show_hist=False)
#figure2.show()

mean2 = statistics.mean(fileList1)
print('Mean of data sample 1: ', mean2)

sd2 = statistics.stdev(fileList1)
print('Standard Deviation of data sample 1: ', sd2)


#Data Sample 2
file2 = pd.read_csv('data2.csv')
fileList2 = file2["Math_score"].tolist()

figure3 = pf.create_distplot([fileList2], ['Data Sample Math scores - 2'], show_hist=False)
#figure3.show()

mean3 = statistics.mean(fileList2)
print('Mean of data sample 2: ', mean3)

sd3 = statistics.stdev(fileList2)
print('Standard Deviation of data sample 2: ', sd3)






#Data Sample 3
file3 = pd.read_csv('data3.csv')
fileList3 = file3["Math_score"].tolist()

figure4 = pf.create_distplot([fileList2], ['Data Sample Math scores - 3'], show_hist=False)
#figure4.show()

mean4 = statistics.mean(fileList3)
print('Mean of data sample 2: ', mean4)

sd4 = statistics.stdev(fileList3)
print('Standard Deviation of data sample 2: ', sd4)