import pandas as pd
import numpy as np

def dataframe():
  dados_uv = {
    'Localidade': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Curitiba', 'Fortaleza', 'Manaus'],
    'Intensidade': [8.5, 10.2, 9.0, 7.4, 11.0, 9.9],
    'Índice UV': ['Alto', 'Muito Alto', 'Alto', 'Moderado', 'Extremo', 'Alto']
}


  df_uv = pd.DataFrame(dados_uv)
  return df_uv



def filtragem_maiores_indices_uv(df_uv):

    print("------ Cidades com Maiores Índices de Radiação UV ------")
    print("")
    df_filtrado = df_uv[df_uv["Índice UV"] == "Alto"]
    print(df_filtrado)
    return df_filtrado
    
    
def media_uv (df_filtrado):

    print("")
    print("---------- Média de Radiação UV ---------")
    media = df_filtrado["Intensidade"].mean()
    print(f"A media de radiação das cidades com indice\n UV mais alto é de: {media:.2f}")
    print("")

def main():
     
     df_uv = dataframe()
     filtragem_maiores_indices_uv(df_uv)
     media_uv(df_uv)

if __name__ == "__main__":
    main()