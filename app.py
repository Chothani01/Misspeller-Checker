import streamlit as st
from model import process

def main():
    st.header("Mispeller tool")
    st.caption("This model is not 100% accurate!!")
    text = st.text_area("Enter text")
    if st.button("Correct"):
        corrected_text, error_list = process(text)
        misspelled_output = f"Misspelled words:{error_list}"
        st.code(corrected_text, language='text')
        st.code(misspelled_output, language='text')

if __name__=="__main__":
    main()