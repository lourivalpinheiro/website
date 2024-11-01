import streamlit as st
import pandas as pd
import plotly_express as px

# Setting up data

course_list = {
    "nome": ["BPO Financeiro", "Certificação Lean Six Sigma: white belt", "Simplifica Excel Express", "Python - Mundo 1", "Python: noções introdutórias", "Iniciação Contábil", "Plano de Contas Contábil", "Git e Github", "Inteligência Emocional 4.0", "Controladoria", "Demonstrações Contábeis"],
    "mes": ["Maio", "Maio", "Junho", "Junho", "Junho", "Agosto", "Agosto", "Outubro", "Outubro", "Outubro", "Outubro"],
    "carga_horaria": [1, 8, 10, 40, 5, 5, 2, 20, 10, 6, 5]
}

df1 = pd.DataFrame(course_list)

programmed_budget = {
    "categoria": ["Anhaguera", "Cebrac", "Cefis"],
    "valor": [1880.40, 1794.00, 132.00]
}

df2 = pd.DataFrame(programmed_budget)

curso_mes = {
    "mes": ["Maio", "Junho", "Agosto", "Outubro"],
    "quantidade": [2, 3, 2, 4]
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
    st.set_page_config("Currículo", layout="wide")
    st.markdown("# Lourival Teixeira Pinheiro Neto")
    st.markdown("## Educação")
    st.divider()
    st.markdown(
       """1. Ciências Contábeis - Anhaguera - 2028;
          2. Aux. Administrativo Financeiro - Cebrac - 2025;
          3. Exchange student - MountainView High School - New Zealand."""
    )

    st.markdown("## Experiência")
    st.divider()
    st.markdown("- Aux. Administrativo - Team Contabilidade (junho de 2024 - o momento).")
    st.markdown("## Trabalho Voluntário")
    st.divider()
    st.markdown("- Auxiliar Administrativo - RConsult (abril de 2024 - maio de 2024).")

    st.markdown("## Cursos extra-curriculares:")
    st.divider()
    st.table(df1)

    st.markdown("## Idiomas:")
    st.markdown('- Inglês: C2 Proficiency level (EF SET CERTIFICATE).')



def knowledge():
    st.markdown("# Cursos extra-curriculares:")
    st.table(df1)

    st.markdown("## Quantidade de horas estudadas:")
    fig1 = px.bar(df1, x="mes", y="carga_horaria", title="Horas estudadas")
    st.plotly_chart(fig1)

    st.markdown("## Quantidade de cursos por mês")
    fig2 = px.bar(df3, x="mes", y="quantidade", title="Cursos por mês")
    st.plotly_chart(fig2)

    st.markdown("## Orçamento para educação no 2º Semestre de 2024:")
    st.divider()
    fig3 = px.box(df2, y="valor", title="Planejado")
    st.plotly_chart(fig3)

def articles():
    st.markdown("# Artigos")
    st.divider()
    st.markdown("## Aprendizado Contínuo: a chave para o sucesso profissional no século XXI")
    st.divider()
    st.markdown("""
    ### Introdução
    ---
    Em um mundo em constante transformação, a educação tradicional muitas vezes se mostra insuficiente. No Brasil, dados recentes revelam que um número alarmante de jovens não concluem a educação básica, comprometendo seu futuro profissional. 

    ### Life-long learning
    ---
    Aprendizado contínuo é a prática ou filosofia que visa adquirir novos conhecimentos e habilidades ao longo de toda a vida, seja através de cursos, leituras, experiências práticas ou interações com outras pessoas. Em uma perspectiva focada no trabalho, o que faz dessa filosofia uma ferramenta tão poderosa para aqueles que usufruem dela é o irrefutável fato de que profissionais que não se atualizam tendem a ficar obsoletos frente aos correntes no mercado de trabalho.

    A importância e benefícios do Aprendizado Contínuo
    Você já se perguntou por que algumas pessoas se destacam em suas carreiras, enquanto outras parecem estagnar? A resposta pode estar na busca constante por conhecimento. Uma das habilidades mais valorizadas pelo mercado de trabalho é a resolução de problemas. Por buscarem conhecimento de diferentes áreas, pessoas que colocam em prática essa ideia tendem a ter um arsenal mais preparado para lidar com desafios, quando eles aparecem. Com o tempo, como qualquer bom ativo, esses conhecimentos são aprofundados e criam conexões por pontos comuns entre si, tornando o aprendiz cada vez mais capaz de unir conceitos e utilizá-los no dia a dia, além de perceber os seguintes benefícios:

    1. Adaptabilidade: Os aprendizes contínuos são mais adaptáveis às mudanças do mercado de trabalho, pois estão sempre atualizados sobre as últimas tendências e tecnologias;
    2. Inovação: A busca por novos conhecimentos estimula a criatividade e a capacidade de pensar fora da caixa, gerando novas ideias e soluções;
    Satisfação pessoal: Além dos benefícios profissionais, o aprendizado contínuo contribui para o desenvolvimento pessoal, aumentando a autoestima e o bem-estar.

    ### Aprendizado Contínuo não é "generalismo"
    ---
    Lifelong learners não são generalistas. Embora o aprendizado contínuo abranja diversas áreas, é fundamental ter uma especialização em um determinado campo. A combinação de conhecimento profundo, amplitude e humildade para saber que é necessário obter conhecimento de diferentes áreas para resolver questões é o que diferencia um profissional de sucesso.

    ### Conclusão 
    ---
    Pense em um médico que busca se atualizar sobre as últimas pesquisas em sua área, ou um programador que aprende uma nova linguagem de programação. Esses são exemplos de profissionais que investem em seu desenvolvimento contínuo. Quanto mais avançamos, mais vai ficando clara a percepção de que precisamos de pessoas dispostas a ir além de seus conhecimentos atuais para resolverem problemas que nos impactam como sociedade. O futuro pertence aos eternos aprendizes. Mudamos o mundo ao transformar as nossas mentes. 
    """)
    st.divider()

    st.markdown("## Liderança: como líderes surgem?")
    st.divider()
    st.markdown("""
    ### Introdução
    ---
    Um dos principais estereótipos implicados na figura de um líder é que ele, ou ela, nasceram com as habilidades técnicas e emocionais necessárias para estarem na atual posição. Que tal conversarmos sob uma perspectiva diferente?

    ### Liderança é mais que mera hierarquia
    ---
    Mais de que um cargo, liderança é um comportamento que pode ser desenvolvido e melhorado ao longo do tempo. A crença limitante e infundada de que líderes foram destinados a ocuparem seus cargos é mera especulação. Então, como explicar tendências? 
    
    **Tendências:** um abrupto aumento na capacidade de pessoas que possuem uma boa desenvoltura em habilidades fundamentais para a execução de uma boa liderança como, por exemplo: 

    2. Inteligência emocional: saber gerir emoções a fim de melhor executar as funções que nos foram atribuídas;
    Comunicação: capacidade de comunicar e receber direcionamentos diferentes, além de compartilhar informações importantes à resolução de determinado problema.

    Tendências, talvez a melhor palavra para descrever o "destino", dentro de uma perspectiva mais realista, provém de diferentes vivências, principalmente na fase da infância e adolescência, onde o indivíduo tende a atingir determinado grau de desenvolvimento das habilidades anteriormente citadas. A boa notícia para aqueles que talvez pensem que a liderança não é para eles é o fato de que todas as habilidades necessárias para produzir um comportamento de liderança podem ser treinadas. Tal processo dura toda uma vida. 

    ### E a política? 
    ---
    Muitos líderes jamais surgirão pelo simples fato de não conseguirem lidar com um fator determinante que irá ditar a possibilidade de efetivamente chegarem a liderar pessoas: a política.   Como bem sabemos, bons profissionais não são ditados apenas por seus conhecimentos técnicos, mas também pelos emocionais. Porém, iremos além, adicionando uma nova camada: a capacidade política. Saber influenciar pessoas e estabelecer conexões, além de mantê-las e transitar entre elas, muitas das vezes, é "palavra final" à ascensão como líder. Afinal, somos seres sociais e, por isso, vivemos constantemente criando relações de poder, e essas ditam muito de nossa carreira profissional.

    ### Comece por você
    ---
    Um desengano muito comum que geralmente afasta pessoas da liderança é acharem que para liderar é preciso ter uma multidão que os seguirá e os darão o devido reconhecimento. Na verdade, a primeira pessoa a qual lideramos somos nós mesmos. É sensato pensar que se não conseguirmos liderar as diferentes áreas de nossa vida, provavelmente não conseguiremos liderar outras pessoas. Cabe a nós, então, buscarmos aperfeiçoar nossas habilidades e crescer na liderança de nossas próprias vidas a fim de nos prepararmos para quando a oportunidade vier.

    ### Conclusão
    ---
    Liderança é um comportamento a ser desenvolvido e bons líderes surgem de uma boa liderança mediante eles mesmos. Em um paralelo com "O mito da caverna" de Platão, convido você a sair da caverna. Não deixe que o líder em você morra mergulhado pelas sombras das dúvidas que sua mente insiste em pregar. Lidere a si mesmo!
    """)



# Setting up the navigation bar

## Pages

pages = {
    "Menu Principal": [st.Page(main_menu, title='Blog')],
    "Conhecimento": [st.Page(articles, title="Artigos"), st.Page(knowledge, title="Cursos")],
    "Sobre mim": [st.Page(curriculum, title="Currículo")],
}
    
nav = st.navigation(pages)
nav.run()

