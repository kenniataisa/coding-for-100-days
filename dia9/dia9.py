import pandas as pd
import numpy as np

def dataframe():
    
    df = pd.read_csv(r"C:\Users\Kennia Taisa\Documents\python\Projeto-de-Segmentação-de-Clientes\olist-dataset\olist_order_items_dataset.csv")         
    media = df['price'].mean()
    mediana = df['price'].median()
    desvio_padrao = df['price'].std()
    maximo = df['price'].max()
    minimo = df['price'].min()

    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desvio Padrao: {desvio_padrao:.2f}")
    print(f"Maximo: {maximo:.2f}")
    print(f"Minimo: {minimo:.2f}")

def main():
    dataframe()

if __name__ == "__main__":
    main()        

