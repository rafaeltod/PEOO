import streamlit as st
from contato import Contato
from inicioUI import InicioUI

st.header("IF Agenda")
st.write("Olá mundo!")
nome = st.text_input("Nome")
email = st.text_input("E-mail")

if st.button("Clique Aqui"):
    c = Contato(nome, email)
    st.write("Bem-vindo ao StreamLit")
    st.write(c)

InicioUI.main()