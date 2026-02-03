import pandas as pd

dataset = pd.read_csv('IMDB-Movie-Data.csv')
print(dataset.head(5))
print(dataset.info())
dataset = dataset.drop(columns=[ "Title","Description","Director","Actors","Rank"])
print(dataset.head())

print(dataset.isnull().sum())
dataset["Revenue (Millions)"] = dataset["Revenue (Millions)"].fillna(
    dataset["Revenue (Millions)"].mean()
)

dataset["Metascore"] = dataset["Metascore"].fillna(
    dataset["Metascore"].mean()
)

print(dataset.isnull().sum())

dataset["label"] = dataset["Rating"].apply(lambda x: 1 if x>=7.0 else 0)
print(dataset.head())

genre_dummy=dataset["Genre"].str.get_dummies(sep=',')
dataset=pd.concat([dataset,genre_dummy],axis=1)
dataset.drop(columns=["Genre"], inplace=True)
print(dataset.head())
X = dataset.drop(columns=["Rating", "label", "Year"])
y = dataset["label"]
import matplotlib.pyplot as plt
import seaborn as sns

plt.plot(dataset['Votes'], dataset['Revenue (Millions)'], 'o')
plt.xlabel('Votes')
plt.ylabel('Revenue (Millions)')
plt.title('Votes vs Revenue')
plt.show()

# STEP 6: Train–Test Split (80% Train, 20% Test)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining set size:", X_train.shape)
print("Testing set size:", X_test.shape)


# STEP 7: Train Logistic Regression Model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# STEP 8: Model Evaluation
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# STEP 9: Interpretation & Insights
print("\nINSIGHTS:")
print("1. Movies with higher votes tend to have higher ratings.")
print("2. Metascore is a strong indicator of IMDb rating.")
print("3. Revenue alone does not guarantee a high rating.")
