import pandas as pd
from sqlalchemy import MetaData, Table, Column, String, Integer, Float
from app.db import engine

CSV_PATH = "data.csv"
TABLE_NAME = "sales"

def infer_sqlalchemy_type(value):
    if isinstance(value, int):
        return Integer
    if isinstance(value, float):
        return Float
    return String

def load_csv():
    df = pd.read_csv(CSV_PATH)
    metadata = MetaData()

    columns = []
    sample_row = df.iloc[0]

    for col in df.columns:
        dtype = infer_sqlalchemy_type(sample_row[col])
        columns.append(Column(col, dtype))

    table = Table(TABLE_NAME, metadata, *columns)
    metadata.drop_all(engine, [table], checkfirst=True)
    metadata.create_all(engine)

    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)
    print(f"✅ Loaded {len(df)} rows into {TABLE_NAME}")

if __name__ == "__main__":
    load_csv()
