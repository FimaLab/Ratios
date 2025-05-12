import pandas as pd
import numpy as np
import streamlit as st
from io import BytesIO
import xlsxwriter
def calculate_metabolite_ratios(data):
  data['Arg/Orn+Cit']=data['Arginine']/(data['Ornitine']+data['Citrulline'])
  data['Arg/Orn']=data['Arginine']/data['Ornitine']
  data["Arg/ADMA"]=data['Arginine']/data['ADMA']
  data['(Arg+HomoArg)/ADMA']=(data['Arginine']+data['Homoarginine'])/data['ADMA']
  #Acylcarnitines
  data['C0/(C16+C18)']=data['C0']/(data['C16']+data['C18'])
  data['(C16+C18)/C2']=(data['C16']+data['C18'])/data['C2']
  data['(C6+C8+C10)/C2']=(data['C6']+data['C8']+data['C10'])/data['C2']
  data['C3/C2']=data['C3']/data['C2']
  #Tryptophan metabolism
  data['Trp/Kyn']=data['Tryptophan']/data['Kynurenine']
  data['Trp/(Kyn+QA)']=data['Tryptophan']/(data['Kynurenine']+data['Quinolinic acid'])
  data['Kyn/Quin']=data['Kynurenine']/data['Quinolinic acid']
  data['Quin/HIAA']=data['Quinolinic acid']/data['HIAA']
  #Amino acids
  data['Aspartate/Asparagine']=data['Aspartic acid']/data['Asparagine']
  data['Glutamine/Glutamate']=data['Glutamine']/data['Glutamic acid']
  data['Glycine/Serine']=data['Glycine']/data['Serine']
  data['GSG_index']=data['Glutamic acid']/(data['Serine']+data['Glycine'])

  data['Phe/Tyr']=data['Phenylalanine']/data['Tyrosin']
  data['Phe+Tyr']=data['Phenylalanine']+data['Tyrosin']
  data['BCAA']=data['Summ Leu-Ile']+data['Valine']
  data['BCAA/AAA']=(data['Valine']+data['Summ Leu-Ile'])/(data['Phenylalanine']+data['Tyrosin'])
  #Betaine_choline metabolism
  data['Betaine/choline']=data['Betaine']/data['Choline']
  data['Kyn/Trp']=data['Kynurenine']/data['Tryptophan']
  data['СДК']=data['C14']+data['C14-1']+data['C14-2']+data['C14-OH']+data['C16']+data['C16-1']+data['C16-1-OH']+data['C16-OH']+data['C18']+data['C18-1']+data['C18-1-OH']+data['C18-2']+data['C18-OH']
  data['Alanine / Valine']=data['Alanine']/data['Valine']
  data['Tryptamine / IAA']=data['Tryptamine']/data['Indole-3-acetic acid']
  data['С2/С0']=data['С2']/data['С0']
  data['(C2+C3)/C0']=(data['С2']+data['С3'])/data['С0']
  data['Kynurenic acid / Kynurenine']=data['Kynurenic acid']/data['Kynurenine']
  data['Methionine + Taurine']=data['Methionine']+data['Taurine']
  data['Valine / Alanine']=data['Valine']/data['Alanine']
  data['Riboflavin / Pantothenic']=data['Riboflavin']/data['Pantothenic']
  data['ADMA / NMMA']=data['ADMA']/data['NMMA']
  data['DMG / Choline']=data['DMG']/data['Choline']
  data['TMAO Synthesis']=data['TMAO']/(data['Betaine']+data['C0']+data['Choline'])
  data['TMAO Synthesis (direct)']=data['TMAO']/data['Choline']
  data['DLD (NBS)']=data['Proline']/data['Phenylalanine']
  data['MTHFR Deficiency (NBS)']=data['Methionine']/data['Phenylalanine']
  data['Ratio of Non-Essential to Essential AAs']=(data['Alanine']+data['Arginine']+
                                                   data['Asparagine']+data['Aspartic acid']+data['Glutamine']+data['Glutamic acid']+data['Glycine']+data['Proline']+
                                                   data['Serine']+data['Tyrosine'])/(data['Histidine']+data['Summ Leu-Ile']+data['Lysine']+data['Methionine']+
                                                   data['Phenylalanine']+data['Threonine']+data['Tryptophan']+data['Valine'])
  data['Ratio of Pro to Cit']=data['Proline']/data['Citrulline']
  data['Sum of AAs']=data['Alanine']+data['Arginine']+data['Asparagine']+data['Aspartic acid']+data['Glutamine']+data['Glutamic acid']+data['Glycine']+data['Proline']+data['Serine']+data['Tyrosine']+data['Histidine']+data['Summ Leu-Ile']+data['Lysine']+data['Methionine']+data['Phenylalanine']+data['Threonine']+data['Tryptophan']+data['Valine']                                      
  data['Sum of Essential Aas']=data['Histidine']+data['Summ Leu-Ile']+data['Lysine']+data['Methionine']+data['Phenylalanine']+data['Threonine']+data['Tryptophan']+data['Valine']
                                                   
  data['Sum of Non-Essential AAs']=data['Alanine']+data['Arginine']+data['Asparagine']+data['Aspartic acid']+data['Glutamine']+data['Glutamic acid']+data['Glycine']+data['Proline']+ data['Serine']+data['Tyrosine']                                               
  data['Sum of Solely Glucogenic AAs']=data['Alanine']+data['Arginine']+data['Asparagine']+data['Aspartic acid']+data['Glutamine']+data['Glutamic acid']+data['Glycine']+data['Histidine']+data['Methionine']+data['Proline']+data['Serine']+data['Threonine']+data['Valine']                                                    
  data['Sum of Solely Ketogenic AAs']=data['Summ Leu-Ile']+data['Lysine']
  data['Valinemia (NBS)']=data['Valine']/data['Phenylalanine']
  data['Carnosine Synthesis']=data['Carnosine']/data['Histidine']
  data['Cit Synthesis']=data['Citrulline']/data['Ornitine']
  data['CPS Deficiency (NBS)']=data['Citrulline']/data['Phenylalanine']
  data['HomoArg Synthesis']=data['Homoarginine']/(data['Arginine']+data['Lysine'])
  data['Met Oxidation']=data['Methionine-Sulfoxide']/data['Methionine']
  data['NO-Synthase Activity']=data['Citrulline']/data['Arginine']
  data['Orn Synthesis']=data['Ornitine']/data['Arginine']
  data['OTC Deficiency (NBS)']=data['Ornitine']/data['Citrulline']
  data['Ratio of HArg to ADMA']=data['Homoarginine']/data['ADMA']
  data['Ratio of HArg to SDMA']=data['Homoarginine']/data['TotalDMA (SDMA)']
  data['Sum of Asym. and Sym. Arg Methylation']=(data['TotalDMA (SDMA)']+data['ADMA'])/data['Arginine']
  data['Symmetrical Arg Methylation']=data['TotalDMA (SDMA)']
  data['Histamine Synthesis']=data['Histamine']/data['Histidine']
  data['TMAO Synthesis']=data['TMAO']/(data['Betaine']+data['C0']+data['Choline'])
  data['TMAO Synthesis (direct)']=data['TMAO']/data['Choline']
  data['DLD (NBS)']=data['Proline']/data['Phenylalanine']
  data['MTHFR Deficiency (NBS)']=data['Methionine']/data['Phenylalanine']
  data['Ratio of Non-Essential to Essential AAs']=(data['Alanine']+data['Arginine']+
                                                      data['Asparagine']+data['Aspartic acid']+data['Glutamine']+data['Glutamic acid']+data['Glycine']+data['Proline']+data['Serine']+data['Tyrosin'])/(data['Histidine']+data['Summ Leu-Ile']+data['Lysine']+data['Methionine']+data['Phenylalanine']+data['Threonine']+data['Tryptophan']+data['Valine'])                                                 
  data['Ratio of Pro to Cit']=data['Proline']/data['Citrulline']
  data['Sum of AAs']=data['Alanine']+data['Arginine']+data['Asparagine']+data['Aspartic acid']+data['Glutamine']+data['Glutamic acid']+data['Glycine']+data['Proline']+data['Serine']+data['Tyrosin']+data['Histidine']+data['Summ Leu-Ile']+data['Lysine']+data['Methionine']+data['Phenylalanine']+data['Threonine']+data['Tryptophan']+data['Valine']
  data['Sum of Essential Aas']=data['Histidine']+data['Summ Leu-Ile']+data['Lysine']+data['Methionine']+data['Phenylalanine']+data['Threonine']+data['Tryptophan']+data['Valine']                                                   
  data['Sum of Non-Essential AAs']=data['Alanine']+data['Arginine']+data['Asparagine']+data['Aspartic acid']+data['Glutamine']+data['Glutamic acid']+data['Glycine']+data['Proline']+data['Serine']+data['Tyrosin']
                                                      
                                                          
                                                      
  data['Sum of Solely Glucogenic AAs']=data['Alanine']+data['Arginine']+data['Asparagine']+data['Aspartic acid']+data['Glutamine']+data['Glutamic acid']+data['Glycine']+data['Histidine']+data['Methionine']+data['Proline']+data['Serine']+data['Threonine']+data['Valine']
  data['Sum of Solely Ketogenic AAs']=data['Summ Leu-Ile']+data['Lysine']
  data['Valinemia (NBS)']=data['Valine']/data['Phenylalanine']
  data['Carnosine Synthesis']=data['Carnosine']/data['Histidine']
  data['Cit Synthesis']=data['Citrulline']/data['Ornitine']
  data['CPS Deficiency (NBS)']=data['Citrulline']/data['Phenylalanine']
  data['HomoArg Synthesis']=data['Homoarginine']/(data['Arginine']+data['Lysine'])
  data['Met Oxidation']=data['Methionine-Sulfoxide']/data['Methionine']
  data['NO-Synthase Activity']=data['Citrulline']/data['Arginine']
  data['Orn Synthesis']=data['Ornitine']/data['Arginine']
  data['OTC Deficiency (NBS)']=data['Ornitine']/data['Citrulline']
  data['Ratio of HArg to ADMA']=data['Homoarginine']/data['ADMA']
  data['Ratio of HArg to SDMA']=data['Homoarginine']/data['TotalDMA (SDMA)']
  data['Sum of Asym. and Sym. Arg Methylation']=(data['TotalDMA (SDMA)']+data['ADMA'])/data['Arginine']
  data['Symmetrical Arg Methylation']=data['TotalDMA (SDMA)']
  data['Histamine Synthesis']=data['Histamine']/data['Histidine']
  #carnitines
    
  data['2MBG (NBS)']=data['C5']/data['C3']
  data['Carnitine Uptake Defect (NBS)']=(data['C0']+data['C2']+data['C3']+data['C16']+data['C18']+data['C18-1'])/data['Citrulline']                                           
  data['CPT-2 Deficiency (NBS)']=(data['C16']+data['C18-1'])/data['C2']
  data['EMA (NBS)']=data['C4']/data['C8']
  #data['HMG-CoA Lyase Deficiency (NBS)']=
  data['IBD Deficiency (NBS)']=data['C4']/data['C2']
  data['IVA (NBS)']=data['C5']/data['C2']
  data['LCHAD Deficiency (NBS)']=data['C16-OH']/data['C16']
  data['MA (NBS)']=data['C3']/data['C2']
  data['MC Deficiency (NBS)']=data['C16']/data['C3']
  data['MCAD Deficiency (NBS)']=data['C8']/data['C2']
  data['MCKAT Deficiency (NBS)']=data['C8']/data['C10']
  data['MMA (NBS)']=data['C3']/data['C0']
  data['PA (NBS)']=data['C3']/data['C16']
  data['Ratio of Acetylcarnitine to Carnitine']=data['C2']/data['C0']
  data['Ratio of AC-OHs to ACs']=(data['C5-OH']+data['C14-OH']+data['C16-1-OH']+data['C16-OH']+data['C18-1-OH']+data['C18-OH'])/(data['C0']+ data['C10']+ data['C10-1'] +data['C10-2']+data['C12']+data['C12-1']+data['C14']+ data['C14-1']+ data['C14-2']+data['C16']+data['C16-1']+data['C18']+data['C18-1']+ data['C18-2']+data['C2']+data['C3']+data['C4']+data['C5']+ data['C5-1']+ data['C5-DC']+ data['C6']+data['C6-DC']+data['C8'] + data['C8-1'])
  data['SBCAD Deficiency (NBS)']=data['C5']/data['C0']
  data['SCAD Deficiency (NBS)']=data['C4']/data['C3']
  data['Sum of ACs']=data['C5-OH']+data['C14-OH']+data['C16-OH']+data['C18-1-OH']+data['C18-OH']+data['C0']+ data['C10']+ data['C10-1'] +data['C10-2']+data['C12']+data['C12-1']+data['C14']+ data['C14-1']+ data['C14-2']+data['C16']+data['C16-1']+data['C18']+data['C18-1']+ data['C18-2']+data['C2']+data['C3']+data['C4']+data['C5']+ data['C5-1']+ data['C5-DC']+ data['C6']+data['C6-DC']+data['C8'] + data['C8-1']                                                                                                                         
  data['Sum of MUFA-ACs']=data['C16-1-OH']+data['C18-1-OH']+data['C10-1'] +data['C12-1']+data['C14-1']+ data['C16-1']+ data['C18-1']+data['C8-1'] + data['C5-1']                                                
  data['Sum of PUFA-ACs']=data['C10-2']+data['C14-2']+data['C18-2']
  #data['Sum of SFA-ACs']=
  #data['Sum of Short-Chain Acs']=
  data['TFP Deficiency (NBS)']=data['C16']/data['C16-OH']
  data['VLCAD Deficiency (NBS)']=data['C14-1']/data['C16']
  #data['w-Oxidation']=

    return data

# Streamlit app
st.title("Метаболитные соотношения")

# Загрузка файла Excel
uploaded_file = st.file_uploader("Выберите файл Excel", type=["xlsx"])

if uploaded_file is not None:
    # Чтение данных из Excel
    data = pd.read_excel(uploaded_file)

    # Вывод исходного DataFrame
    st.subheader("Исходные данные")
    st.dataframe(data)

    output_data = calculate_metabolite_ratios(data)

    st.subheader("Обновленные данные с метаболитными соотношениями")
    st.dataframe(output_data)
  
    excel_buffer = BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        output_data.to_excel(writer, index=False, sheet_name='Результаты')
    excel_bytes = excel_buffer.getvalue()

    # Кнопка для скачивания
    st.download_button(
        label="Скачать Excel",
        data=excel_bytes,
        file_name="метаболиты_результаты.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Запуск приложения
if __name__ == "__main__":
    st.write("Загрузите файл")
