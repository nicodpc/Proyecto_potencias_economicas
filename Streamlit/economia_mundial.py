#             Librerias             #
import streamlit as st 
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import pathlib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display
import streamlit.components.v1 as components



#             Librerias             #

#----------Configuracion de la pagina-------------#
# Tenemos dos opciones de Lyout, wide or centered 

st.set_page_config(page_title='Top 5 Economías Mundiales',page_icon=':globe_with_meridians:',layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)

#----------Configuracion de la pagina-------------#


#---------Cosas que vamos a usar en la app---------# 
df = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\df_original.csv')
df_cpi = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\inflacion.csv') # dataframe Inflación
df_pibt = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\pib_total.csv') # dataframe PIB total 
df_pibcr = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\pib_crecimiento.csv') # dataframe PIB crecimiento
df_pibpc = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\PIB_per_capita.csv') # dataframe PIB per capita
df_des = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\tasa_de_desempleo.csv') # dataframe tasa de desempleo
train_usa = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\train_usa.csv')
test_usa = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\test_usa.csv')
forecast_usa = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\forecast_usa.csv')
df_pib_mundial = pd.read_csv(r'C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\CSV\pib_mundial.csv')

#---------Cosas que vamos a usar en la app---------# 


#--------------------Titulo------------------------#
st.title('**Potencias Económicas Mundiales**')
 
#--------------------Titulo------------------------#


# ------------------ SIDE BAR----------------------#
st.sidebar.title ('Top 5 Economías Mundiales ')

# ------------------ SIDE BAR----------------------#

# ------------------ Menú SIDE BAR----------------------#
with st.sidebar:
    selected = option_menu(
        menu_title= "Menú" ,
        options= ['Introducción','Preprocesamiento de Datos','Análisis Exploratorio y Confirmatorio','Machine Learning','Conclusión'], 
        )
if selected == 'Introducción':
    st.image("imagenes\economia_mundial.jpeg",caption='',use_column_width=350)
    st.write("Fuente: https://www.cepal.org/es/subtemas/insercion-la-economia-mundial.")
    st.title('Introducción')

    col1 = st.columns(1)[0]
    with col1:
        st.write("""La economía es una ciencia social que estudia la forma de administrar los recursos disponibles para satisfacer 
                 las necesidades humanas. Analiza el comportamiento, las decisiones y las acciones de los humanos, es decir, 
                 estudia como las personas, empresas y gobiernos toman decisiones relacionadas con la producción, distribución y consumo. 
                 (Fuente: https://economipedia.com/definiciones/economia.html)""")
        st.markdown("""
                  Indicadores a tratar: """)
        st.markdown("1- PIB (Producto Interno Bruto)")
        st.write("""El PIB (Producto Interno Bruto) es el principal indicador de cualquier economía en el mundo ya que nos mide cuantos bienes 
                 y servicios se producen en un país durante un periodo que por lo regular se calcula anualmente.\\
                 Fuente: https://www.rankia.mx/blog/indicadores-economicos-mexico/3081815-importancia-pib-economia  """)
        st.markdown("2- Índice de precios al consumo (IPC)")
        st.write("""El índice de precios al consumo (IPC) es un indicador que mide la variación de los precios de una cesta de bienes y 
                 servicios en un lugar concreto durante un determinado periodo de tiempo.\\
                 Fuente: https://economipedia.com/definiciones/ipc-indice-precios-al-consumo.html  """)
        st.markdown("3- PIB per cápita")
        st.write("""El PIB per cápita es un indicador económico que mide la relación entre el nivel de ingresos de un país y 
                 cada uno de sus pobladores.\\
                 Fuente: https://www.significados.com/pib-per-capita/ """)
        st.markdown("4- Tasa de desempleo")
        st.write("""La tasa de desempleo, también conocida como tasa de paro, mide el nivel de desocupación en relación con la población activa\\
                 Fuente: https://economipedia.com/definiciones/tasa-de-desempleo-paro.html """)
      
        #image2 = Image.open('Info/foto_estambul.jpg')
        #st.image(image2, caption='',width=550)

    
    #st.subheader('')

if selected == 'Preprocesamiento de Datos':
    st.subheader('Preprocesamiento de Datos')
    tab1,tab2 = st.tabs(['**Dataframe CPI original**','**Dataframe CPI Final**'])

    with tab1 :
       st.dataframe(df)
    #code = '''col_drop = ['Unnamed__59','Unnamed__60','Unnamed__61','Unnamed__62','Unnamed__63']
              #df_cpi = df.drop(col_drop, axis=1).copy()'''
    #st.code(code,language='python')
    #-----------------------------------------------------------------------------------------------------#
    code = '''cpi_5 = ['China','Germany','India','Japan','United States','Spain']
df_cpi = df_cpi[df_cpi['Country'].isin(cpi_5)]'''
    st.code(code,language='python')   
    #-----------------------------------------------------------------------------------------------------#    
    code = '''df_cpi =  df_cpi[df_cpi.Series_Name.isin(['Headline Consumer Price Inflation'])]
df_cpi = df_cpi.drop(['Country_Code','IMF_Country_Code','Indicator_Type','Series_Name'], axis=1)
df_cpi.index.name = ''
df_cpi = df_cpi.T
df_cpi = df_cpi.reset_index()
df_cpi.rename(columns={'index':'Year'}, inplace=True)
df_cpi.drop(df_cpi.tail(1).index,inplace=True)
df_cpi ['Year'] = pd.to_datetime(df_cpi['Year'],format= "%Y")'''
    st.code(code,language='python')
    #-----------------------------------------------------------------------------------------------------#  
    with tab2 :
       st.dataframe(df_cpi)


if selected == 'Análisis Exploratorio y Confirmatorio':
    st.subheader('Análisis Exploratorio y Confirmatorio')
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['Comparación de países en relación del tiempo segun su PIB Total',
                                'Comparación de países en relacion del tiempo segun su crecimiento del PIB y PIB per capita',
                                'Comparación de países en relación del tiempo segun su inflación',
                                'Comparación de países en relación del tiempo segun su tasa de desempleo',
                                'Test de Correlación'])

    with tab1 :
       #fig_1 = px.line(df_pibt, x='Year', y=['Estados Unidos','China','Alemania','India','Japón'], title='PIB (US$)', template="plotly_dark") 
       #st.plotly_chart(fig_1)

       fig_11 = px.line(df_pib_mundial, x='Year', y=['Estados Unidos','China','Alemania','Japón','India','media_pib_mundial'], title='Crecimiento del PIB % por año ', template="plotly_dark")
       st.plotly_chart(fig_11)
       #imagen_1 = "C:\Users\nico_\Data\Proyecto_Final_nico\Streamlit\imagenes\grafia_pie.html"
       
       st.subheader('Representación del PIB de las 5 grandes economías a través del tiempo ')
       paises = ['Alemania','Estados Unidos','China','India','Japón']
       datos = {
                  1970: [2.158384e+11,1.073303e+12,9.260264e+10,6.242248e+10,2.126092e+11],
                  1980: [9.502909e+11,2.857307e+12,1.911492e+11,1.863253e+11,1.105386e+12],
                  1990: [1.771671e+12,5.963144e+12,3.608579e+11,3.209790e+11,3.132818e+12],
                  2000: [1.947982e+12,1.025095e+13,1.211332e+12,4.683949e+11,4.968359e+12],
                  2010: [3.3996e+12,1.504896e+13,6.087192e+12,1.675616e+12,5.759072e+12],
                  2020: [3.889669e+12,2.106047e+13,1.468774e+13,2.671595e+12,5.048790e+12],
                  2022: [4.072192e+12,2.546270e+13,1.796317e+13,3.385090e+12,4.231141e+12]
                  }
       colores_pibt = ['teal','navy','darkred','red']
       year =st.slider("Año",1970,2022,1970,step=10)

       fig_2 = go.FigureWidget(data=[go.Pie(labels=paises, values=datos[year], marker=dict(colors=colores_pibt))],
                     )

       st.plotly_chart(fig_2)

#------------------------------------------------------------------------------------------------------------------------------------#

       fig_3 = px.bar(df_pibt, x='Year', y='Estados Unidos', template="plotly_dark",color='Estados Unidos',labels={'Estados Unidos':'PIB US $'},title='PIB de Estados Unidos')
       st.plotly_chart(fig_3)
       
       fig_4 = px.bar(df_pibt, x='Year', y='China', template="plotly_dark",color='China',labels={'China':'PIB US $'},title='PIB de China')
       st.plotly_chart(fig_4)

       st.write("Estados Unidos tardo 15 años en pasar de 10T a 18T en su PIB")
       st.write("China tardo tan solo 8 años en pasar de 10T a casi 18T (17.9T) en su PIB")
    

    with tab2 :
       fig_8 = px.line(df_pibcr, x='Year', y=['Estados Unidos','China','Alemania','Japón','India'], title='Crecimiento del PIB % por año ', template="plotly_dark") 
       st.plotly_chart(fig_8) # crecimiento del PIB %
    
       fig_9 = px.line(df_pibpc, x='Year', y=['Estados Unidos','China','Alemania','Japón','India'], title='Crecimiento del PIB per capita por año', template="plotly_dark") 
       st.plotly_chart(fig_9) # crecimiento PIB per capita
    
    with tab3 :
       fig_5 = px.line(df_cpi, x='Year', y=['United States','China','India','Japan','Germany'], title='CPI año tras año', template="plotly_dark") 
       st.plotly_chart(fig_5)

       fig_6 = px.box(df_cpi, y="United States", template="plotly_dark",color_discrete_sequence=['blue'])
       st.plotly_chart(fig_6)

       fig_7 = px.box(df_cpi, y="China", template="plotly_dark",color_discrete_sequence=['darkred'])
       st.plotly_chart(fig_7)

    with tab4 :
       fig_10 = px.line(df_des, x='Year', y=['Estados Unidos','China','Alemania','Japón','India'], title='Tasa de Desempleo año tras año', template="plotly_dark")
       st.plotly_chart(fig_10)

    with tab5 :
       st.subheader('Test de Normalidad')
      
       code = '''data_pib_china = [9.570471e+12,1.047562e+13, 1.106157e+13, 1.123331e+13, 1.231049e+13, 1.389491e+13, 1.427997e+13, 1.468774e+13, 1.782046e+13, 1.796317e+13 ]
stat, p = normaltest(data_pib_china)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('No podemos rechazar que siga una distribución Gaussiana')
else:
	print('No sigue una distribución Gaussiana')'''
       st.code(code,language='python')        
       st.write("stat=0.965, p=0.617 ")  
       st.write("No podemos rechazar que siga una distribución Gaussiana")

       code = '''data_cpi_china = [2.62, 1.92, 1.44, 2.0, 1.56, 2.07, 2.9, 2.42,  0.9, 1.97]
stat, p = normaltest(data_cpi_china)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('No podemos rechazar que siga una distribución Gaussiana')
else:
	print('No sigue una distribución Gaussiana') '''
       st.code(code,language='python')        
       st.write("stat=0.214, p=0.899 ")  
       st.write("No podemos rechazar que siga una distribución Gaussiana")
#-----------------------------------------------------------------------------------------------------------------------------------------#
      
       code = '''data_pib_usa = [1.684319e+13, 1.755068e+13, 1.820602e+13, 1.869511e+13, 1.947734e+13, 2.053306e+13, 2.138098e+13, 2.106047e+13, 2.331508e+13, 2.546270e+13]
stat, p = normaltest(data_pib_usa)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('No podemos rechazar que siga una distribución Gaussiana')
else:
	print('No sigue una distribución Gaussiana')'''
       st.code(code,language='python')        
       st.write("stat=1.211, p=0.546 ") 
       st.write("No podemos rechazar que siga una distribución Gaussiana")

       code = '''data_cpi_usa = [1.46, 1.62, 0.12, 1.26, 2.14, 2.44, 1.81, 1.23, 4.7, 8.0]
stat, p = normaltest(data_cpi_usa)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('No podemos rechazar que siga una distribución Gaussiana')
else:
print('No sigue una distribución Gaussiana') '''
       st.code(code,language='python')        
       st.write("stat=11.650, p=0.003 ") 
       st.write("No sigue una distribución Gaussiana")
      
#-----------------------------------------------------------------------------------------------------------------------------------------------#
       
       st.subheader('Test de Correlación')
       
       code = '''data_pib_china = [9.570471e+12,1.047562e+13, 1.106157e+13, 1.123331e+13, 1.231049e+13, 1.389491e+13, 1.427997e+13, 1.468774e+13, 1.782046e+13, 1.796317e+13 ]
data_cpi_china = [2.62, 1.92, 1.44, 2.0, 1.56, 2.07, 2.9, 2.42,  0.9, 1.97]
stat, p = pearsonr(data_pib_china, data_cpi_china)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probablemente independientes')
else:
	print('Probablemente dependientes')'''
       st.code(code,language='python')  
       st.write("stat=-0.258, p=0.472 ")
       st.write("Probablemente independientes")

       code = '''data_pib_usa = [1.684319e+13, 1.755068e+13, 1.820602e+13, 1.869511e+13, 1.947734e+13, 2.053306e+13, 2.138098e+13, 2.106047e+13, 2.331508e+13, 2.546270e+13]
data_cpi_usa = [1.46, 1.62, 0.12, 1.26, 2.14, 2.44, 1.81, 1.23, 4.7, 8.0]
stat, p = spearmanr(data_pib_usa, data_cpi_usa)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probablemente independientes')
else:
	print('Probablemente dependientes')'''
       st.code(code,language='python')  
       st.write("stat=0.636, p=0.048 ")
       st.write("Probablemente dependientes")
#----------------------------------------------------------------------------------------------------------------------------------------------#


if selected == 'Machine Learning':
   st.subheader('Series Temporales')

   st.subheader('Dataframe de entrenamiento')
   code = '''df_pibt_usa['Year'] = df_pibt_usa.index
train = df_pibt_usa[df_pibt_usa['Year'] < pd.to_datetime("2017-01-01", format='%Y-%m-%d')] # Separamos train hasta el agosto de 1960
train['train'] = train['Estados Unidos']
del train['Year']
del train['Estados Unidos']'''
   st.code(code,language='python')  
   
   st.subheader('Modelo ARIMA (busqueda de los mejores hiperparámetros)')
   code = '''model = auto_arima(train, trace=True, error_action='ignore', suppress_warnings=True)
model.fit(train) 
forecast = model.predict(n_periods=len(test))
forecast = pd.DataFrame(forecast,index = test.index,columns=['Prediction'])'''
   st.code(code,language='python') 
   st.write('Best model:  ARIMA(2,2,2)')

   st.image('imagenes/grafica_usa.png')

if selected == 'Conclusión':
   st.title('Conclusión')
   st.image("imagenes\images_conclu.jpeg",caption='',use_column_width=350)
   st.write("Fuente: https://segurosnews.com/news/credito-y-caucion-cree-que-la-economia-mundial-esta-al-borde-de-la-recesion")
   st.markdown("- Comportamiento de estas Economías")
   st.markdown("- Crisis Mundiales y tiempo de recuperación")
   st.markdown("- Crecimiento abrupto de China ")
 

   
   