import streamlit as st
'''from retangulo import Retangulo'''
from bhaskara import Bhaskara
import pandas as pd
import numpy as np

class InicioUI:
    def main():
        '''st.header("Cálculos com Retângulo")
        base = st.text_input("Base")
        altura = st.text_input("Altura")
        if st.button("Calcular"):
            r = Retangulo(float(base), float(altura))
            st.write(r.__str__())
            st.write(f"Área do Retângulo: {r.calc_area()}")
            st.write(f"Diagonal do Retângulo: {r.calc_diagonal()}")'''
        
        st.header("Equação do II Grau: y = ax**2 + bx + c")
        a = st.text_input("a")
        b = st.text_input("b")
        c = st.text_input("c")
        if st.button("Calcular Equação"):
            e = Bhaskara(float(a), float(b), float(c))
            st.write(e.delta())
            st.write(f"x1: {e.Raiz1()}")
            st.write(f"x2: {e.Raiz2()}")
            e.calc_p()
            grafico = pd.DataFrame(
             {
              "x": e.get_px(),
              "y": e.get_py(),
             }
            )
            

            st.line_chart(grafico, x="x", y="y")

