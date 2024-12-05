import streamlit as st
import pandas as pd
import plotly_express as px

# Setting up data

course_list = {
    "nome": ["BPO Financeiro", "Certificação Lean Six Sigma: white belt", "Simplifica Excel Express", "Python - Mundo 1", "Python: noções introdutórias", "Iniciação Contábil", "Plano de Contas Contábil", "Git e Github", "Inteligência Emocional 4.0", "Controladoria", "Demonstrações Contábeis", "MEG: Modelo de Excelência em Gestão", "Perfil Comportamental"],
    "mes": ["Maio", "Maio", "Junho", "Junho", "Junho", "Agosto", "Agosto", "Outubro", "Outubro", "Outubro", "Outubro", "Novembro", "Novembro"],
    "carga_horaria": [1, 8, 10, 40, 5, 5, 2, 20, 10, 6, 5, 1, 2]
}


df1 = pd.DataFrame(course_list)

programmed_budget = {
    "categoria": ["Anhaguera", "Cebrac", "Cefis"],
    "valor": [1880.40, 1794.00, 132.00]
}

df2 = pd.DataFrame(programmed_budget)

curso_mes = {
    "mes": ["Maio", "Junho", "Agosto", "Outubro", "Novembro"],
    "quantidade": [2, 3, 2, 4, 2]
}

df3 = pd.DataFrame(curso_mes)



# Pages

## Setting up the functions

def main_menu():
    st.markdown("# Blog")
    st.markdown("### Destaques")
    st.divider()
    c1, c2 = st.columns(2, gap="small")
    with c1:
        st.link_button("Liderança: como líderes surgem?", icon="🎙", url="https://www.linkedin.com/pulse/lideran%C3%A7a-como-l%C3%ADderes-surgem-lourival-pinheiro-tlhvf/")
    with c2:
        st.link_button("Aprendizado Contínuo: a chave para o sucesso profissional no século XXI", icon="🧠", url="https://www.linkedin.com/pulse/aprendizado-cont%C3%ADnuo-chave-para-o-sucesso-s%C3%A9culo-xxi-pinheiro-lb1nf/")

def curriculum():
    st.set_page_config("Currículo", layout="wide", page_icon= 'favicon.ico')
    st.markdown("# Lourival Teixeira Pinheiro Neto")
    st.markdown("## Educação")
    st.divider()
    st.markdown("1. Ciências Contábeis - Anhaguera - 2028;")
    st.markdown("2. Aux. Administrativo Financeiro - Cebrac - 2025;")
    st.markdown("3. Exchange student - MountainView High School - New Zealand.")

    st.markdown("## Experiência")
    st.divider()
    st.markdown("- Aux. Administrativo - Team Contabilidade (junho de 2024 - o momento).")
    st.markdown("## Trabalho Voluntário")
    st.divider()
    st.markdown("- Auxiliar Administrativo - RConsult (abril de 2024 - maio de 2024).")

    st.markdown("## Idiomas:")
    st.markdown('- Inglês: C2 Proficiency level (EF SET CERTIFICATE).')



def knowledge():
    st.markdown("# Cursos extra-curriculares:")
    st.caption("Planejando meus estudos para 2025.")


# Setting up the navigation bar

## Pages

pages = {
    "Menu Principal": [st.Page(main_menu, title='Blog')],
    "Conhecimento": [st.Page(knowledge, title="Cursos")],
    "Sobre mim": [st.Page(curriculum, title="Currículo")],
}
    
nav = st.navigation(pages)
nav.run()

