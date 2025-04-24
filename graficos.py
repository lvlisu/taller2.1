import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("datos.csv")

st.title("Análisis de variables macroeconómicas")


st.header("Análisis gráfico")
fig, ax = plt.subplots(1,3, figsize = (10,4))
ax[0].hist(df["pibaño"])
ax[0].set_title("PIB año")
conteo = df["desempleo_total"].value_counts()
ax[1].bar(conteo.index, conteo.values)
ax[1].set_title("Desempleo total")
ax[2].hist(df["inflacion_taño"])
ax[2].set_title("Inflación total")
fig.tight_layout()

st.pyplot(fig)

fig,ax = plt.subplots(1,2, figsize= (10,4))
sns.scatterplot(data=df, x="Fecha", y="pibaño", ax=ax[0])
sns.boxplot(data=df, x="Fecha", y="politica_mfaño", ax=ax[1])
fig.tight_layout()

st.pyplot(fig)