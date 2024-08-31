import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\adith\\OneDrive\\Desktop\\ML\\data\\EnjoySport.csv",header=None)
print(data,"n")

d = np.array(data)[:,:-1]
print("n The attributes are: ",d)

target = np.array(data)[:,-1]
print("n The target is: ",target)

def train(c,t):
    for i,val in enumerate(t):
        if val=="Yes":
            specific_hypothesis=c[i].copy()
        break

    for i,val in enumerate(c):
        if t[i]=="Yes":
            for x in range(len(specific_hypothesis)):
                if val[x]!=specific_hypothesis[x]:
                    specific_hypothesis[x]="?"
                else:
                    pass
    return specific_hypothesis

print("The final hypothesis is: ",train(d,target))
