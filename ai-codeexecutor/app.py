# app.py
from api.api import execute_gpt_code
import streamlit as st

def main():
    st.title("AI-Powered Code Executor")

    # User input for code execution
    code_input = st.text_area("Enter Python Code Here:")

    if st.button("Execute"):
        # Call the API to execute the code
        execution_result = execute_gpt_code(code_input)
        st.write("Execution Result:")
        st.code(execution_result)

if __name__ == "__main__":
    main()
