def main():
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
    main()