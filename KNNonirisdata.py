import pandas as pd
from pandas import DataFrame

df_irsibd=pd.read_csv("C:\\Users\\adith\\OneDrive\\Desktop\\ML\\data\\iris.data",header=None,index_col=None)
print(df_irsibd)

X=df_irsibd.iloc[:,:-1].values
y=df_irsibd.iloc[:,4].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8,random_state=100)
print(y_test)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

predicted=model.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predicted))
print(classification_report(y_test,predicted))