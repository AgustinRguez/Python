import os
import pandas as pd

def extract(url):
    fd = pd.read_csv(url)
    return fd

def transform_high_price(df):
    df['es_caro'] = df['Price'] >=150
    return df

def load_data(df, output):
    df.to_csv(output)
    print("Datos guardados aca: ", output)
    print("Ruta completa del archivo generado:", os.path.abspath(output))

def transform_date(df):
    df['Date'] = pd.to_datetime(df['Date'])
    today = pd.Timestamp.today() - pd.Timedelta(days=1200)
    df = df[df['Date'] >= today]
    return df


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/anyoneai/notebooks/main/customers_and_orders/data/orders.csv"
    raw_data = extract(url)
    #transformed_data = transform_date(raw_data)
    transformed_data = transform_high_price(raw_data)
    load_data(transformed_data, "orders_completed.csv")
