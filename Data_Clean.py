df = pd.read_csv("C:/Users/anujn/OneDrive/Desktop/Churn.csv")
df.sample(5)

df.drop('customerID', axis = 'columns', inplace = True)
df.dtypes

df[pd.to_numeric(df.TotalCharges, errors = 'coerce').isnull()]

df[pd.to_numeric(df.TotalCharges, errors = 'coerce').isnull()].shape

df1.replace('No internet service','No', inplace = True)
df1.replace('No phone service','No', inplace = True)

yes_no_columns = ['Partner','Dependents','PhoneService','MultipleLines','OnlineSecurity','OnlineBackup',
                  'DeviceProtection','TechSupport','StreamingTV','StreamingMovies','PaperlessBilling','Churn']
for col in yes_no_columns:
    df1[col].replace({'Yes': 1,'No': 0},inplace=True)
