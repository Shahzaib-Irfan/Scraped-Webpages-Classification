import pandas as pd
from sklearn.metrics import confusion_matrix
from kNN import predicted_labels

df = pd.read_csv('Webpages.csv')

test_documents = pd.concat([df.iloc[12: 15], df.iloc[27: 30], df.iloc[42: 45]])

true_labels = test_documents['Type'].tolist()

matrix = confusion_matrix(true_labels, predicted_labels)

print(matrix)