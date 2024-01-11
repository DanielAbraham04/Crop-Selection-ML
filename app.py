from flask import Flask
from flask_socketio import SocketIO, send, join_room
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os
import re
import pandas as pd
import numpy as np
import sys
import csv
import preprocess as pr
import DTALG as DT
import RFALG as RF
import NBALG as NB
import prediction as pre
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

path="dataset.csv"
path1="static/results/data2.csv"
@app.route('/')
def index():
	message="Welcome"
	dataset=pd.read_csv(path).values
	data=dataset.tolist()
	data1=[]
	i=0
	for da in dataset:
		if i<500:
			data1.append(da)
			i=i+1
		
	return render_template('index.html',message=message,data=data1)
	
@app.route('/Preprocess')
def Preprocess():
	message="Preprocess Successfully Finshed"
	pr.process(path)	

	dataset=pd.read_csv(path1).values
	data=dataset.tolist()
	data1=[]
	i=0
	for da in dataset:
		if i<500:
			data1.append(da)
			i=i+1

	return render_template('preprocess.html',message=message,data=data1)


@app.route('/DecisionTree')
def DecisionTree():
	message="DecisionTree Successfully Finshed"
	DT.process(path1)	

	dataset=pd.read_csv(path1).values
	data=dataset.tolist()
	data1=[]
	i=0
	for da in dataset:
		if i<500:
			data1.append(da)
			i=i+1

	return render_template('DecisionTree.html',message=message,data=data1)

@app.route('/RandomForest')
def RandomForest():
	message="RandomForest Successfully Finshed"
	RF.process(path1)	

	dataset=pd.read_csv(path1).values
	data=dataset.tolist()
	data1=[]
	i=0
	for da in dataset:
		if i<500:
			data1.append(da)
			i=i+1

	return render_template('RandomForest.html',message=message,data=data1)


@app.route('/NaiveBayes')
def NaiveBayes():
	message="NaiveBayes Successfully Finshed"
	NB.process(path1)	

	dataset=pd.read_csv(path1).values
	data=dataset.tolist()
	data1=[]
	i=0
	for da in dataset:
		if i<500:
			data1.append(da)
			i=i+1

	return render_template('NaiveBayes.html',message=message,data=data1)

@app.route('/Prediction')
def Prediction():
	message="Prediction"
	#pre.process(path1)	

	dataset=pd.read_csv(path1).values
	data=dataset.tolist()
	data1=[]
	i=0
	for da in dataset:
		if i<500:
			data1.append(da)
			i=i+1

	return render_template('Prediction.html',message=message,data=data1)


@app.route('/Predict',methods=['POST'])
def Predict():
    	f1=request.form['f1']
    	f2=request.form['f2']
    	f3=request.form['f3']
    	f4=request.form['f4']
    	f5=request.form['f5']
    	print(f1,f2,f3,f4,f5)
    	x_test=[]
    	x_test.append(f1)
    	x_test.append(f2)
    	x_test.append(f3)
    	x_test.append(f4)
    	x_test.append(f5)
    	
    	print(x_test)

    	res=pre.process(path1,x_test)
    	print(res[0])
    	result=""
    	g=res[0]
    	Fertilizer="-----"
    	Tech="----"
    	
    	if g==0:
    		f="NO"
    		f = "Wheat"
    		Fertilizer="Super phosphate-155 kg/acre, Muriate of potash-20 kg/acre, Nitro phophate-125 kg/acre"
    	if g==1:
    		f = "Wheat"
    		Fertilizer="Super phosphate-155 kg/acre, Muriate of potash-20 kg/acre, Nitro phophate-125 kg/acre"
    	if g==2:
    		f = "Oats"
    		Fertilizer="Nitorgen-110 kg/acre, P2O5 20-30 kg/acre, K2O-17 kg/acre, Sulphur-10 kg/acre\n"
    	if g==3:
    		f = "Gram"
    		Fertilizer="Nitorgen-12.5 kg/acre ,P2O5-25 kg/acre,K2O-12.5 kg/acre,Sulphur-10 kg/acre,"
    	if g==4:
    		f = "Pea"
    		Fertilizer="Nitorgen-55 kg/acre,Phosphorus-20 kg/acre,Potash-40 kg/acre,"
    	if g==5:
    		f = "Tea"
    		Fertilizer="Ammonium phosphate-35 kg/acre,Potassium sulphate-15 kg/acre,MOP-12 kg/acre,Magnesium sulphate-15 kg/acre,Zinc sulphate-3 kg/acre \n"
    	if g==6:
    		f = "Rice"
    		Fertilizer="P2O5-35 kg/acre,K2O-50 kg/acre \n"
    	if g==7:
    		f = "Bajra"
    		Fertilizer="Nitrogen-80 kg/acre,Phosphorous-40 kg/acre,Photash-40 kg/acre \n"
    	if g==8:
    		f = "Maize"
    		Fertilizer="P2O5-24 kg/acre,K2O-12 kg/acre,"
    	if g==9:
    		f = "Cotton"
    		Fertilizer="Nitrogen-150 kg/acre,Phosphorous-60 kg/acre,Potassium-90 kg/acre \n"
    	if g==10:
    		f = "Groundnut"
    		Fertilizer="Nitrogen-25 kg/acre,Phosphorous-50 kg/acre,Potassium-75 kg/acre,Sulphur sludge-60 kg/acre \n"
    	if g==11:
    		f = "Jute"
    		Fertilizer="Urea-8 kg/acre,Nitrogen-10 kg/acre,N,P2O5 and K2O-20 kg/acre \n"
    	if g==12:
    		f = "Sugarcane"
    		Fertilizer="Zinc sulphate-37.5 kg/acre,Ferrous sulphate-100 kg/acre \n"
    		
    	if g==13:
    		f = "Turmeric"
    		Fertilizer="Nitrogen-120 kg/acre,P2O5-50 kg/acre,K2O-80 kg/acre \n"
    	if g==14:
    		f = "No Crop"
    		f = "Wheat"
    		Fertilizer="Super phosphate-155 kg/acre, Muriate of potash-20 kg/acre, Nitro phophate-125 kg/acre"
 
    	x_test.append(f)
    	
    	print(x_test)
    	
    	dataset=pd.read_csv(path1).values
    	data=dataset.tolist()
    	data1=[]
    	i=0
    	for da in dataset:
    		if i<500:
    			data1.append(da)
    			i=i+1
    	message="Prediction Class is  " + f
    	print(message)
    	return render_template('Prediction1.html',message=message,data=data1,result=x_test,Fertilizer=Fertilizer)

if __name__ == '__main__':
	app.run(debug = True)

