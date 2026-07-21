import streamlit as st
from textwrap import dedent

st.set_page_config(
    page_title="Clubes de Ciencia",
    page_icon="🔬",
    layout="centered",
)

st.header("La IA solo es tan inteligente como sus datos")

st.write(
    "Esta página es un pequeño repositorio para guardar todos los materiales que veamos"
)

st.write("Este es el repositorio donde encontrarás todo, si quieres guardarlo")

st.link_button("Open in github", "https://github.com/ZaidDeAnda/CdeC2026-mty")

st.divider()

tabs = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Useful resources"])

tabs[0].subheader("Python crash course part 1")

tabs[0].markdown("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ZaidDeAnda/CdeC2026-mty/blob/main/notebooks/Python%20Crash%20Course.ipynb)")

tabs[1].write("WIP")

tabs[1].markdown("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ZaidDeAnda/CdeC2026-mty/blob/main/notebooks/ML-Practice.ipynb)")

tabs[2].write("WIP")

tabs[3].subheader("Perceptrones and neural networks")

tabs[3].write("WIP")

tabs[4].subheader("Convolutional neural networks")

tabs[4].write("WIP")

tabs[5].header("Books")

tabs[5].markdown(
    dedent("""
    ### Hands-On Machine Learning with Scikit-Learn and PyTorch

    by Aurelien Geron

    _O'Reilly editorial_
           
    Puedes encontrarlo aquí: https://ageron.github.io/
    """)
)

tabs[5].markdown(
    dedent("""
    ### Deep Learning with Python

    by Francois Chollet (creator of Keras)

    _Anaya editorial_
    """)
)

tabs[5].subheader("Videos")

tabs[5].markdown(
    dedent("""
    ### 3Blue1Brown

    https://www.youtube.com/c/3blue1brown

    Amazing videos about math.
    """)
)

tabs[5].markdown(
    dedent("""
    ### CodigoFacilito

    https://codigofacilito.com/cursos

    Useful platform for code courses.
    """)
)
