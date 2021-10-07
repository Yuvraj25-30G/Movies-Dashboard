import io
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import streamlit as st




st.set_page_config(page_title="Top Movies Dashboard",
                    layout="wide",
)

st.title("Welcome to Movies Infopedia")
st.subheader("An analysis of top 1000 IMDB Movies")

st.header("The Dataset")
df = pd.read_csv("topmov.csv")
df.drop('Poster_Link',axis=1,inplace=True)
df.drop('Overview',axis=1,inplace=True)
# df.drop('Star1',axis=1,inplace=True)
df.drop('Star2',axis=1,inplace=True)
df.drop('Star3',axis=1,inplace=True)
df.drop('Star4',axis=1,inplace=True)



df_byYear=df.sort_values(["Released_Year"],
                    axis=0,
                    ascending=[False],
                    inplace=True
                    )


# df.sort_values(["IMDB_Rating"],
#                     axis=0,
#                     ascending=[False],
#                     inplace=True)

# df.sort_values(["Gross"],
#                     axis=0,
#                     ascending=[False],
#                     inplace=True)

st.dataframe(df)

st.sidebar.header("Filter options")
year = st.sidebar.multiselect(
    "Select by Year of Release",
    options = df["Released_Year"].unique(),
)

Runtime = st.sidebar.multiselect(
    "Select by Runtime",
    options = df["Runtime"].unique(),
)

x = st.sidebar.slider('Select by Rating')



# Mainpage
