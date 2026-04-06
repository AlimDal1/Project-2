def transform_data(df):
    df = df.drop_duplicates()
    df = df.fillna("Unknown")

    df.columns = df.columns.str.lower().str.replace(" ", "_")

    if "age" in df.columns:
        df["age"] = df["age"].replace("Unknown", 0).astype(int)
        df["age_group"] = df["age"].apply(
            lambda x: "Adult" if x >= 18 else "Child"
        )

    return df
