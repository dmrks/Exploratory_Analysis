import codecademylib3
import pandas as pd
import numpy as np

# 2 Load
diabetes_data = pd.read_csv("diabetes.csv")
print(diabetes_data.head())

#3 + 4 768 rows/entries // 9 columns in total
print(diabetes_data.info())

# 5 Do any of the columns in the data contain null (missing) values? No they aren't at first sight

missing_values = diabetes_data[diabetes_data.isnull().any(axis= 1)]
print(missing_values)

# 6 + 7 + 8 BMI= 0? // BloodPressure 0? - Outliers: Pregnancies 17?
print(diabetes_data.describe())

#9
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

#10
print(diabetes_data.isnull().sum())

#11 - Insulin is almost everywhere not measured
missing_values = diabetes_data[diabetes_data.isnull().any(axis= 1)]
print(missing_values)

#13
print(diabetes_data.dtypes)

#14 Replace O with 0 + Switch type to int64
print(diabetes_data.Outcome.unique())
diabetes_data.Outcome = diabetes_data.Outcome.replace("O","0")
print(diabetes_data.Outcome.unique())

diabetes_data.Outcome = diabetes_data.Outcome.astype("int64")
print(diabetes_data.dtypes)

