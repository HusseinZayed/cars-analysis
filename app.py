import streamlit as st

st.markdown("Enter car information to predict price")

st.markdown("---")


year = st.number_input(
        "Year",
        min_value=int(df["year"].min()),
        max_value=int(df["year"].max()),
        value=2018
    )


mileage = st.number_input(
        "Mileage",
        min_value=0,
        value=50000
    )

