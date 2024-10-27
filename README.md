Selected Dataset: Titanic - Machine Learning from Disaster
The Titanic dataset has these key attributes:

PassengerId: Unique identifier
Survived: Survival (0 = No, 1 = Yes)
Pclass: Ticket class (1, 2, or 3)
Name: Passenger name
Sex: Gender
Age: Age in years
SibSp: Number of siblings/spouses aboard
Parch: Number of parents/children aboard
Ticket: Ticket number
Fare: Passenger fare
Cabin: Cabin number
Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)
Steps to Perform the Required Tasks
1. Data Cleaning
Remove missing or irrelevant data.
Handle NaN values in the Age and Embarked columns.
2. Statistical Analysis
Use .describe() to get summary statistics.
Use .corr() to find correlations between variables like Age, Fare, SibSp, and Parch.
3. Visualizations
Histogram: Show distribution of passenger ages.
Bar Chart: Survival rates by passenger class.
Scatter Plot: Relationship between fare and age.
Heatmap: Correlation matrix showing relationships between numeric features.
4. Code Implementation
I'll provide Python code for loading, cleaning, analyzing, and visualizing this dataset.
