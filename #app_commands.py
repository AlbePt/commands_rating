#app_commands.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Функция для загрузки данных из опубликованной Google Таблицы
def load_data_from_google_sheet():
    # Постоянная ссылка на CSV-файл из Google Таблицы
    sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRrBjE7FGC1cQJ5ue4Xj_oP1oVUEV5M-uiRAZPGXS2zbmCMtMGPg4mMuYrVxDqoGw/pubhtml'
    # Чтение данных напрямую из ссылки на CSV
    data = pd.read_csv(sheet_url)
    return data

# Основная функция приложения
def main():
    st.title('Рейтинг команд')

    if st.button('Обновить'):
        try:
            # Загрузка данных из Google Таблицы
            data = load_data_from_google_sheet()
            
            # Создаем диаграмму бабла
           # Нормализуем значения 'Балл' от 0 до 1
            data['Прозрачность'] = data['Балл'] / data['Балл'].max()

            fig = px.scatter(
                data, 
                x='Команда', 
                y='Балл', 
                size='Размер', 
                color='Цвет', 
                text='Балл',
                labels={'Команда': '', 'Балл': ''},
                hover_name='Команда',
                color_discrete_map='identity',
                size_max=50
            )
            
            # Включаем отображение текста внутри баблов
            fig.update_traces(
                marker=dict(opacity=data['Прозрачность']/2),
                textposition='middle center', 
                textfont_size=12
            )
            
            st.plotly_chart(fig)
            st.header('Дополнительные задания')
            col1, col2 = st.columns(2)

            #with col1:

                
            
            #with col2:

                
                
        except Exception as e:
            st.error(f'Ошибка загрузки данных: {e}')

if __name__ == '__main__':
    main()
