def validate_data(df):
    if df.empty:
        raise ValueError("DataFrame is empty!")

    if df.isnull().sum().sum() > 0:
        print("Warning: Missing values still exist.")

    return True
