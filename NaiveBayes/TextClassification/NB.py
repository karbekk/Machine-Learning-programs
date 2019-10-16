import pandas as pd
from urllib.request import urlopen
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator,BayesianEstimator

names = "A,B,C,D,E,F,G,H,I,J,K,L,M,RESULT"
names = names.split(",")
print(names)

data = pd.read_csv(urlopen("http://bit.do/heart-disease"),names=names)
data.head()

model = BayesianModel([("A","B"),("B","C"),("C","D"),("D","RESULT")])
model.fit(data,estimator=MaximumLikelihoodEstimator)

from pgmpy.inference import VariableElimination
infer = VariableElimination(model)
q = infer.query(variables=['RESULT'],evidence={"C":2})
print(q["RESULT"])
