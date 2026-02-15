#1. import the required python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#2. load the dataset into dataframe
customer_data = pd.read_csv('Customer Purchasing Behaviors.csv')

#3. display the number of rows and columns in the dataset
print("Number of rows and columns in the dataset:", customer_data.shape)

#4. print column names of the dataset
print("Column names of the dataset:", customer_data.columns)

#5. dispaly the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(customer_data.head())

#6. check the datatype of each column
print("Data types of each column:")
print(customer_data.dtypes)

#7. identify the number of missing values in each column
print("Number of missing values in each column:")
print(customer_data.isnull().sum())

#8. fill missing values in numerical columns with mean value
numerical_cols = customer_data.select_dtypes(include=[np.number]).columns
customer_data[numerical_cols] = customer_data[numerical_cols].fillna(customer_data[numerical_cols].mean())

#9. fill missing values in categorical columns with mode value
categorical_cols = customer_data.select_dtypes(include=[object]).columns
customer_data[categorical_cols] = customer_data[categorical_cols].fillna(customer_data[categorical_cols].mode().iloc[0])

#10. verify that there are no missing values remaining
print(customer_data.info())

#11. calculate the mean for all numerical columns
mean = customer_data[numerical_cols].mean()
print("Mean values for numerical columns:")
print(mean)

#12. calculate the median for all numerical columns
median = customer_data[numerical_cols].median()
print("Median values for numerical columns:")
print(median)

#13. calculate the standard deviation for all numerical columns
std_dev = customer_data[numerical_cols].std()
print("Standard deviation for numerical columns:")
print(std_dev)

#14. find the minimum and maximum values for numerical columns
minimum = customer_data.agg([min,max])

#15. generate a summary using describe()
print("The summary using describe(): ")
print(customer_data.describe())

#16. Create a histogram for the purchase amount column
plt.hist(customer_data['purchase_amount'], bins=20)
plt.title('Distribution of Purchase Amount')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.show()

#17. Create a bar chart showing the count of customers by purchase_amount
sns.countplot(x=customer_data['purchase_amount'])
plt.title('Count of Customers by Purchase Amount')
plt.xlabel('Purchase Amount')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

#18. Create a box plot for the purchase amount column
sns.boxplot(x=customer_data['purchase_amount'])
plt.title('Boxplot of Purchase Amount')
plt.xlabel('Purchase Amount')
plt.xticks(rotation=45)
plt.show()

#19. Create a scatter plot between age and purchase amount
sns.scatterplot(x=customer_data['age'],y=customer_data['purchase_amount'])
plt.title('Scatter Plot of Age vs Purchase Amount')
plt.xlabel('Age')
plt.ylabel('Purchase Amount')
plt.show()

#20. Display a correlation heatmap for numerical columns.
plt.figure(figsize=(10, 8))
sns.heatmap(customer_data[numerical_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


