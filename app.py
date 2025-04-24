import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("graficador_series.xlsx")
df

#estructura de datos
df = df.rename(columns={"Tasa de política monetaria(Dato diario)":"politica_mndia",
                        "Tasa de política monetaria(Dato fin de semana)":"politica_mfsemana",
                        "Tasa de política monetaria(Dato mes)":"politica_mmes",
                        "Tasa de política monetaria(Dato fin de mes)":"politica_mfmes",
                        "Tasa de política monetaria(Dato fin de trimestre)":"politica_mftrimes",
                        "Tasa de política monetaria(Dato fin de semestre)":"politica_mfsem",
                        "Tasa de política monetaria(Dato fin de año)":"politica_mfaño",
                        "Tasa de política monetaria(Dato semanal)":"politica_msem",
                        "Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Dato fin de trimestre)":"pibtri",
                        "Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Variación porcentual  trimestral)":"pibtriporcentaje",
                        "Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Variación porcentual  año corrido)":"pibaño",
                        "Tasa de desempleo - total nacional(Dato fin de mes)":"desempleo_total",
                        "Inflación total, anual(Dato fin de año)":"inflacion_taño"})

df = df.drop(columns=["politica_mndia", "politica_mfsemana","politica_mmes","politica_mfmes","politica_mftrimes","politica_mfsem","politica_msem"],
             index=[0,9247])

df.info()

df = df.replace("-","")

col =["politica_mfaño","pibtri","pibtriporcentaje","pibaño","desempleo_total","inflacion_taño"]
for i in col:
    df[i] = df[i].str.replace(".","")
    df[i] = df[i].str.replace(",",".")
    df[i] = pd.to_numeric(df[i])

df["Fecha"] = pd.to_datetime(df["Fecha"],format = "%d/%m/%Y")

df.set_index("Fecha")["politica_mfaño"].dropna().plot()
plt.plot(df.set_index("Fecha")["politica_mfaño"].dropna())
plt.show()

df.to_csv("datos.csv", index=False)


