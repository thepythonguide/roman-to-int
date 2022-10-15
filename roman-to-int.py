import streamlit as st

VALUE_DICT = {  'I':1, "V":5, "X":10, "L":50, 
                "C":100, "D":500, "M":1000}

# Convert Roman numeral string to integer value
def roman_to_int(roman_val):
    int_val = 0
    i = 0
    try:
        while len(roman_val) > i + 1:
            cur_char_val = VALUE_DICT[roman_val[i]]
            next_char_val = VALUE_DICT[roman_val[i + 1]]

            # if Roman numeral is in non-descending order
            if cur_char_val < next_char_val:
                int_val -= cur_char_val
            else:
                int_val += cur_char_val
            i += 1

        # last character
        int_val += VALUE_DICT[roman_val[i]]
    except:
        st.error('Invalid Roman Numeral')
    return int_val

st.title('Roman Numeral to Integer')
roman_val = st.text_input(label='Roman Numeral Value', value='VI')
st.info(roman_to_int(roman_val))



st.write('[The Python Guide .com](https://thepythonguide.com)')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
