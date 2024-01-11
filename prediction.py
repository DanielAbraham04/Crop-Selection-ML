import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
def process(path,s):
	dataset=pd.read_csv(path).values
	x1 = dataset[:,0:5]
	y1 = dataset[:,5] # define the target variable (dependent variable) as y
	print(x1)
	print(y1)

	#x2=[4.75,0.0393005,57,80,7868.64,1387.36,31.1,43146.896]
	print(s)
	x2=s
	x=np.asarray(x2).reshape(1,-1)
	model2=RandomForestClassifier()
	model2.fit(x1, y1)
	pred = model2.predict(x)
	print(pred)
	return pred
	



