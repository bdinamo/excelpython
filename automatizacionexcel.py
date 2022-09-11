
import pandas as pd
import sys
#import 

df = pd.read_excel("C:\\Users\\brian\\OneDrive\\Escritorio\\ExcelPython\\Test.xlsx")
bd = ["Acetoclor","Diclorvos","Diquat"]
salida = []

column = df.columns[1]
print(column)
print("-" * len(column))

for index, row in df.iterrows():
    if row[column] in bd:
        print("Se encontró el ",row[column])
    else:
        print("No se encontró el ensayo",row[column])
        salida.append(row[column])

print("El/Los que no se encontraron son \n", salida)
dict = {'Ensayo no encontrado': salida} 
df = pd.DataFrame(dict) 
df.to_csv("C:\\Users\\brian\\OneDrive\\Escritorio\\ExcelPython\\NoEncontrados.xlsx")
    


""" def main():
    raw_df = read_files()
    filtered_df = filters(raw_df)
    create_csv(filtered_df)
    print("\tFinalizado")
    


def read_files():
    print("Leyendo archivo")
    filename = "C:\\Users\\brian\\OneDrive\\Escritorio\\ExcelPython\\Test.xlsx"
    #filename = input("Ingrese el nombre del archivo: ") + '.xlsx'
    df = pd.read_excel(filename, sheet_name='Prueba', header=0)
    column_df = ["Columna1","Columna2"]
    df = df[column_df]
    return df

def filters(raw_df):
    print("Filtrando resultados")
    #df = raw_df[raw_df.Columna2 == 'Hola']
    df = raw_df[raw_df["Columna2"] == 'Hola']
    return df

def create_csv(df):
    print("Creando archivo csv")
    df.to_csv("archivo_salida.csv", sep = ',' , header = True, index = False)

if __name__ == '__main__':
    main() """
 

