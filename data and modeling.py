import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_df = pd.read_csv("music.csv")     # Storage csv file into a variable

X = music_df.drop(columns=["genre"])    # X is the info we´ll use as INPUT
y = music_df["genre"]   # y is the outcome we want to predict

# Here we get training and testing data and assign it to the four variables
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# This is just one of plenty training models existing
my_model = DecisionTreeClassifier()
my_model.fit(x_train, y_train)  # We train the model, so it is ready to make predictions
predictions = my_model.predict(x_test)
score = accuracy_score(y_test, predictions)     # it tells us the accuracy of our model

print(f"My predictions: {predictions}")
print(f"Accuracy: {score}")
