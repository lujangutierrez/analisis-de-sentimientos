import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#from scipy import stats
#from sklearn.preprocessing import standardscaler
#from scipy import norm
df_deaths = pd.read_csv('cause_of_deaths.csv', header=0)
#print(df_deaths.shape) #nos muestra cuántas filas y cuántas columnas hay en el df
#print(df_deaths['Meningitis']) nos muestra el largo de una columna
#print(df_deaths[['Meningitis', 'Drugs']]) nos muestra dos columnas
#print(df_deaths['Meningitis'].mean()) #nos trae  el promedio de 
#print(df_death.describe) # nos trae todo el df
#print(sns.displot(df_deaths['Year'])) #ESTO NO FUNCIONAAAAAAA
#print(df_deaths['Meningitis'].kurt)
#print(df_deaths['Meningitis'].skew)
pais = 'Country/Territory'
anio = 'Year' 
data = pd.concat([df_deaths['Year'],df_deaths[pais]], axis=1) #me lo va a traer a en el eje 1
print(data.head(20)) #de la variable data me trae las primeras 20
plt.show()