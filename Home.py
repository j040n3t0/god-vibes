import streamlit as st
#from streamlit_extras.app_logo import add_logo
from components import Header
import random

## Running project
##### streamlit run Home.py --theme.base dark

def random_message(person_name):
    messages = ["VOCÊ É FODA!!!",
                "VOCÊ É IMPORTANTE PARA ALGUÉM!!!",
                "O SEU SORRISO MUDA O MUNDO!!!",
                "VOCÊ É IMPORTANTE PARA ALGUÉM!!!",
                "OLHA NO ESPELHO, LEVANTA O QUEIXO, PQ TU VEIO PARA VENCER!!",
                "SE LIGA, ENTRE MILHÕES TU JÁ VENCEU! POR ISSO TU NASCEU!!!"
                ]
    size_list = len(messages)
    number = random.randint(0,size_list-1)

    full_message = person_name.upper() + " " + messages[number]
    return full_message

Header.add_logo()

st.title("🙏 God Vibes 📿")
st.subheader("Digite seu nome")

person_name = st.text_input('')

if st.button("Clica aqui"):
    st.balloons()
    st.success(random_message(person_name), icon="✅")
else:
    st.write('')
