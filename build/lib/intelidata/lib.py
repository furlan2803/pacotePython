import pandas as pd
import csv
    
def load_data(path_to_file):
    df = pd.read_csv(path_to_file)
    return df

def clean_data(data):
    cleaned_data = data.fillna("null")
    return cleaned_data

def check_for_duplicates(cleaned_df):
    duplicates = cleaned_df[cleaned_df.duplicated()]
    return duplicates

def load_data_with_encoding(file_path, encodings=['utf-8', 'latin1']):
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df
        except UnicodeDecodeError:
            print(f"Erro ao tentar ler o arquivo com a codificação {encoding}. Tentando outra codificação.")
    return None

def check_csv_file(csv_path):
    with open(csv_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)

        num_fields = len(header) if header else 0

        line_number = 1
        for row in reader:
            line_number += 1
            if len(row) != num_fields:
                print(f"Erro na linha {line_number}: Número de campos incorreto. Esperado {num_fields}, encontrado {len(row)}")