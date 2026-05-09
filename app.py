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

    if st.button("Predict Price"):

        input_df = pd.DataFrame({
            "brand": [brand],
            "model": [model],
            "year": [year],
            "title_status": [title_status],
            "mileage": [mileage],
            "color": [color],
            "state": [state],
            "country": [country],
            "condition": [condition]
        })

        predicted_price = model_pipeline.predict(input_df)[0]

        st.success(f"Predicted Car Price: ${predicted_price:,.2f}")

        st.balloons()
