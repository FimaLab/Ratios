import pandas as pd
import streamlit as st
from io import BytesIO
from function_ratio import calculate_metabolite_ratios,calculate_metabolite_ratios_zebra
from constants import *
from utils import *

st.title("Метаболитные соотношения")

panel = main_radio_button_study()

if panel == "Человек":
   # Служебная информация — в боковой панели
   with st.sidebar:
        st.sidebar.selectbox("Доступные соотношения (поиск)", all_possible_ratios)

        # Вывод количества соотношений
        st.sidebar.metric(label="Общее количество соотношений", value=len(all_possible_ratios))

   uploaded_file = st.file_uploader("Выберите файл Excel", type=["xlsx"],key="human_uploader")

else:
   # Служебная информация — в боковой панели
   with st.sidebar:
        st.sidebar.selectbox("Доступные соотношения (поиск)", all_possible_ratios_zebra)

        # Вывод количества соотношений
        st.sidebar.metric(label="Общее количество соотношений", value=len(all_possible_ratios_zebra))

   uploaded_file = st.file_uploader("Выберите файл Excel", type=["xlsx"],key="zebra_uploader")

if uploaded_file is not None:
    try:
        # Чтение листа "метаболиты"
        data = pd.read_excel(uploaded_file)
        
        if panel == "Человек":
           # Расчет соотношений
           output_data, ratios_data, missing_cols, skipped_ratios, calculated_ratios,successful_ratios = calculate_metabolite_ratios(data)
        else:
           output_data, ratios_data, missing_cols, skipped_ratios, calculated_ratios,successful_ratios = calculate_metabolite_ratios_zebra(data)

        # Отображение данных в табах
        tab1, tab2 = st.tabs(["🧬 Метаболиты", "📈 Соотношения"])

        with tab1:
            st.subheader("Метаболиты")
            st.dataframe(output_data)

        with tab2:
            st.subheader("Соотношения")
            st.dataframe(ratios_data)

        with st.sidebar:
             st.header("📊 Статус расчётов")

             if missing_cols or skipped_ratios:
                 with st.expander("⚠️ Проблемы с расчётами"):

                     if missing_cols:
                         st.markdown("**❌ Отсутствующие колонки:**")
                         selected_col = st.selectbox(
                             "Выберите колонку",
                             options=missing_cols,
                             format_func=lambda x: f"🧩 {x}"
                         )
                         st.caption(f"Колонка `{selected_col}` отсутствует в данных.")

                     if skipped_ratios:
                         st.markdown("**🔁 Пропущенные соотношения:**")
                         ratio_options = [f"{r} (не хватает: {', '.join(m)})" for r, m in skipped_ratios]
                         selected_ratio = st.selectbox(
                             "Выберите соотношение",
                             options=ratio_options,
                             format_func=lambda x: f"📉 {x}"
                         )
                         st.caption(f"Подробности: {selected_ratio}")

             if calculated_ratios:
                 with st.expander("✅ Успешно рассчитанные"):

                     ratio_options = [f"{r} (использовались: {', '.join(m)})" for r, m in successful_ratios]
                     selected_ratio = st.selectbox(
                         "Выберите соотношение",
                         options=ratio_options,
                         format_func=lambda x: f"📉 {x}"
                     )
                     st.caption(f"Подробности: {selected_ratio}")

        # Радиокнопка для выбора формата сохранения
        sheet_option = st.radio(
            "Как сохранить данные?",
            ('На один лист', 'На разные листы')
        )

        # Кнопка для скачивания файла
        if st.button("Скачать Excel"):
            excel_buffer = BytesIO()

            with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
                if sheet_option == 'На один лист':
                    # Объединяем таблицы по горизонтали
                    combined_df = pd.concat([output_data, ratios_data], axis=1)
                    combined_df.to_excel(writer, index=False, sheet_name='Результаты')
                else:
                    output_data.to_excel(writer, index=False, sheet_name='Метаболиты')
                    ratios_data.to_excel(writer, index=False, sheet_name='Соотношения')

            excel_bytes = excel_buffer.getvalue()

            st.download_button(
                label="Скачать Excel файл",
                data=excel_bytes,
                file_name="результаты.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:
        st.error(f"Произошла ошибка при обработке файла: {e}")
else:
    st.info("Пожалуйста, загрузите Excel-файл.")
