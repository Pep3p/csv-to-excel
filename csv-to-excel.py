import os
import pandas as pd

def convert_csv_to_excel(csv_file, excel_file):
  """
  Convierte un archivo CSV a Excel.

  Args:
    csv_file: La ruta del archivo CSV.
    excel_file: La ruta del archivo Excel de salida.
  """

  df = pd.read_csv(csv_file)

  # Rellenar los valores None con una cadena vacía.
  df["Risk"] = df["Risk"].fillna("")

  df.to_excel(excel_file, index=False)

def main():
  """
  Programa principal.
  """

  # Obtener la ruta de la carpeta con los archivos CSV.
  folder_path = input("Ingrese la ruta de la carpeta con los archivos CSV: ")

  # Obtener la ruta de la carpeta de salida.
  output_folder_path = input("Ingrese la ruta de la carpeta de salida: ")

  # Listar los archivos CSV de la carpeta.
  csv_files = os.listdir(folder_path)

  # Iterar sobre los archivos CSV.
  for csv_file in csv_files:
    # Obtener el nombre del archivo sin la extensión.
    excel_file_name = os.path.splitext(csv_file)[0] + ".xlsx"

    # Obtener la ruta del archivo Excel de salida.
    excel_file_path = os.path.join(output_folder_path, excel_file_name)

    # Convertir el archivo CSV a Excel.
    convert_csv_to_excel(os.path.join(folder_path, csv_file), excel_file_path)

if __name__ == "__main__":
  main()
