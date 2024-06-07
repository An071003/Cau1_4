import streamlit as st

st.title('Playground')
st.text_area(label='Input prompt', value='')
st.button(label='Submit')
st.slider('Temperature', 0.00, 2.00, 1.00)
st.slider('TopP', 0.00, 1.00, 1.00)
st.slider('Maximum length', 1, 4000, 1)
st.checkbox('Show probabilities')
st.code("print('Hello world')", language= 'python', line_numbers=False)