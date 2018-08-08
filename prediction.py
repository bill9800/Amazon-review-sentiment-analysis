import time
tic = time.time()
from sklearn.externals import joblib
import sys
import numpy as np

# load data
file = open(sys.argv[2])
sentence = file.read()
file.close()

# preprocess X
X = [sentence]
word_bag = joblib.load('word_bag.pkl')
X = word_bag.transform(X)


#####################################
# load pre_train random_forest model
with open('ensemble_model.pkl','rb') as f:
    clf = joblib.load(f)
#####################################
# predict
y_pred = clf.predict(X)
y_pred = y_pred.tolist()
output = str(y_pred).strip('[]')

# output
with open('output.txt','w') as f:
    f.write(output)

tac = time.time()
print ("running time:",tac-tic)