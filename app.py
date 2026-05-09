import streamlit as st

st.markdown("Enter car information to predict price")

st.markdown("---")

    # INPUTS
brand = st.selectbox(
        "Brand",
        sorted(df["brand"].unique())
    )

model = st.selectbox(
        "Model",
        sorted(df["model"].unique())
    )

year = st.number_input(
        "Year",
        min_value=int(df["year"].min()),
        max_value=int(df["year"].max()),
        value=2018
    )

title_status = st.selectbox(
        "Title Status",
        sorted(df["title_status"].unique())
    )

mileage = st.number_input(
        "Mileage",
        min_value=0,
        value=50000
    )

color = st.selectbox(
        "Color",
        sorted(df["color"].unique())
    )

state = st.selectbox(
        "State",
        sorted(df["state"].unique())
    )

country = st.selectbox(
        "Country",
        sorted(df["country"].unique())
    )

condition = st.selectbox(
        "Condition",
        sorted(df["condition"].unique())
    )
