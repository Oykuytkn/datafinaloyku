import pandas
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy
# Load dataset
url = "mock_viewer_data.csv"
df = pandas.read_csv(url)

X = df.values[:, 0:5]
Y = df.values[:, 5]


X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)
dt_clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,max_depth=5, min_samples_leaf=5)
dt_clf_gini.fit(X_train, y_train)
y_pred_gini = dt_clf_gini.predict(X_test)

print ("Desicion Tree using Gini Index\nAccuracy is ", accuracy_score(y_test,y_pred_gini)*100 )

#creating and training a model
#serializing our model to a file called model.pkl
import pickle
pickle.dump(dt_clf_gini, open("model.pkl","wb"))

