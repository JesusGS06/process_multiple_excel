import streamlit as st
import pandas as pd
from bulk_helper import insert_rooms_and_employees_in_bulk

def process_files(first_file, second_file):

    try:
        df1 = pd.read_excel(first_file)
        df2 = pd.read_excel(second_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return []
    
    st.write("DATA FROM FIRST EXCEL")
    st.dataframe(df1)
    st.write("DATA FROM SECOND EXCEL")
    st.dataframe(df2)

    df_combinado = pd.concat([df1, df2], axis=1)
    df_combinado = df_combinado.rename(columns={
    'Tipo': 'type',
    'Tarifa': 'price',
    'Estado': 'status',
    'Nombre': 'name',
    'Cargo': 'occupation',
    'Salario': 'salary',
    'Fecha_contratacion': 'date_of_entry',
    })

    df_combinado['date_of_entry'] = df_combinado['date_of_entry'].dt.strftime('%Y/%m/%d')
    df_combinado['salary'] = df_combinado['salary'].astype(float)
    df_combinado['price'] = df_combinado['price'].astype(float)

    insert_rooms_and_employees_in_bulk(df_combinado)
          
st.title('PROCESSING TWO EXCEL FILES')

upload_first_file = st.file_uploader("Upload the first excel file", type=["xls", "xlsx"])
upload_second_file = st.file_uploader("Upload the second excel file", type=["xls", "xlsx"])

if st.button("SUBMIT"):
    if upload_first_file is not None and upload_second_file is not None:
        process_files(upload_first_file, upload_second_file )
        st.toast('DATA SUCCESFULLY LOADED')
    else:
        st.write("Error processing the files, remember to upload two files!")