# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_csv('Data/train.csv')

# Data Cleaning
df = df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Encoding
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Statistical Analysis
summary_stats = df.describe()
correlation_matrix = df.corr()

# Display Summary Statistics and Correlation Matrix
print("Summary Statistics:\n", summary_stats)
print("\nCorrelation Matrix:\n", correlation_matrix)


# Visualization---------------------------------------------

# 1. Histogram of Ages
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True, color='skyblue')
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Frequency')
# plt.show()
plt.savefig("Histogram.png", dpi=300, bbox_inches='tight')
plt.close()

# 2. Bar Chart of Survival Rates of passangers
plt.figure(figsize=(8, 5))
sns.barplot(x='Pclass', y='Survived', data=df, ci=None, palette="muted")
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
# plt.show()
plt.savefig("Bar_chart.png", dpi=300, bbox_inches='tight')
plt.close()

# 3. Scatter Plot of Fare VS Age
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df, palette='coolwarm', alpha=0.6)
plt.title('Fare vs Age with Survival Indicator')
plt.xlabel('Age')
plt.ylabel('Fare')
# plt.show()
plt.savefig("Scatter_plot.png", dpi=300, bbox_inches='tight')
plt.close()

# 4. Heatmap of Correlation_Matrix
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Titanic Dataset')
# plt.show()
plt.savefig("correlation_matrix_heatmap.png", dpi=300, bbox_inches='tight')
plt.close()