import pandas as pd

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)
    df['transformed_column'] = df['some_column'].apply(lambda x: x * 2)  # Example transformation
    return df

if __name__ == "__main__":
    raw_data = [{'some_column': 1}, {'some_column': 2}]
    transformed_data = transform_data(raw_data)
    print(transformed_data)
