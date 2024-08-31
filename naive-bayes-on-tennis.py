import pandas as pd
import random as rd
from sklearn.metrics import confusion_matrix
import math

lut=dict()
label_attribute="PlayTennis"
labels=["No","Yes"]

df=pd.read_csv("C:\\Users\\adith\\OneDrive\\Desktop\\ML\\data\\tennis.csv")
print(df)
total=len(df)

attribute_name=df.columns.tolist()
attribute_name.remove(label_attribute)
ldf=df.pivot_table(index=[label_attribute],columns=[label_attribute],aggfunc='size')
print(ldf)
lut[label_attribute]=ldf

for attribute in attribute_name:
    lut[attribute]=df.pivot_table(index=["PlayTennis"],columns=[attribute],aggfunc='size')
    lut[attribute].fillna(0,inplace=True)

target=list()
prediction=list()

for index,row in df.iterrows():
    if rd.random()>0.5:
        result=list()
        for label in labels:
            posteriorProb=math.log(lut[label_attribute][label][label]/total)
            for attribute in attribute_name:
                value=row[attribute]
                posteriorProb=posteriorProb+math.log(lut[attribute][value][label]/lut[label_attribute][label][label]+1)

            result.append(posteriorProb)
        
        target.append(row[label_attribute])
        print(result)
        maxindex=result.index(max(result))
        prediction.append(labels[maxindex])

print(confusion_matrix(target,prediction))
print(target)
print(prediction)