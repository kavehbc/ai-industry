import streamlit as st
import requests
import os


def main():
    num_1 = st.number_input("Enter first number", value=0)
    num_2 = st.number_input("Enter second number", value=0)

    btn_calculate = st.button("Calculate")
    if btn_calculate:
        # Call the API to perform addition
        api_url = os.getenv("API_URL", "http://api:8000") # alternative: os.environ["API_URL"]
        
        url = f"{api_url}/{num_1}/{num_2}"
        response = requests.get(url)

        if response.status_code == 200:
            result = response.json().get("result")
            st.success(f"The result is: **{result}**")
        else:
            st.error("Error occurred while calculating.")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Dashboard",
        page_icon=":bar_chart:",
        layout="wide",
    )

    st.title("My Dashboard")
    main()
