import streamlit as st

st.title("Oil Spill Predictor")

st.write("""### Enter required inputs""")

def show_predict_page():
    number = st.number_input('Insert weight(in tonns)')
    #st.write('Weight is ', number)


    input_2 = (
        "string_1",
        "string_2",
        "string_3",
        "string_4"
    )

    input_2 = st.selectbox("Input2", input_2)


    ok = st.button("Predict")
    if ok:
        st.write("Oil spill will happen")
