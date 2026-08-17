# Estudo de caso 1 - DSA AI Coder - Assistente de Programação Python

# módulo para interagir com o sistema operacional
import os

# Streamlit - interface web interativa
import streamlit as st
from click import prompt

# LLM
from groq import Groq
from groq.types.chat import chat_completion

# Configura a página do streamlit com título, ícone, leyout e estado inicial da sidebar
st.set_page_config(
    page_title="Professor Asy",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define um prompt de sistema que descreve as regras e comportamentos do assistente de IA
CUSTOM_PROMPT = """"
Você é o "Asy", um assistente de IA especialista em programação na linguagem python. Seu objetivo é auxiliar desenvolvedores iniciantes a aprender python e solucionar suas dúvidas.

Você deve sempre ser o mais objetivo, claro, didático e acessível.

Essas são suas regras de operação:
1. Foco em programação: responda apenas perguntas da área de tecnologia, levando sempre em consideração a linguagem python. Caso o usuário faça uma pergunta fora dessa área, você deve responder educadamente que você não entende sobre o assunto, mas que está disponível para perguntas sobre python.
2. Estrutura de Resposta: você sempre deve seguir a seguinte estrutura de resposta: explicação (explicação breve e didática que explica de maneira geral o tópico perguntado), exemplo de código (o código deve ser comentado linha a linha, explicando o que cada parte faz), detalhes do código (essa seção é opcional e deve ser adicionada quando forem perguntas complexas em que só os comentários do código não são suficientes para uma boa explicação), Exemplo (aqui você deve dar um exemplo do mundo real para tornar a resposta mais palpável e também para ajudar a fixar o conhecimento), documentação de referência (aqui você deve indicar através de links as referências usadas para responder a pergunta).
3. Clareza e precisão: use linguagem clara. Evite jargões. Suas respostas devem ser tecnicamente precisas. Sempre seja educado.
"""

# Criando o conteúdo da barra lateral no streamlit
with st.sidebar:
    # Define o título da barra lateral
    st.title("👋🏼Bem-Vindo, eu sou o Professor Asy")

    # Mostra um texto explicativo sobre o assistente
    st.markdown("Um assistente de IA focado em programação Python.")

    # campo para inserir a chave groq
    groq_api_key = st.text_input(
        label="Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("----")
    st.markdown(
        "Esse assistente foi desenvolvido para auxiliar em suas dúvidas de programação com a linugagem Python. Lembre-se que IAs podem cometer erros. Sempre verifique a corretude das respostas.")

    st.markdown("----")
    st.markdown("🔗Link para a documentação Python oficial: https://docs.python.org")
    st.link_button("✉️E-mail de suporte em caso de dúvidas sobre o assistente", "mailto:mollersoareslaura@gmail.com")

# Voltando a área principal da web, ou seja, saindo do side bar
st.title("Aprenda com o Professor Asy!")

# Subtítulo adicional
st.title("Seu assistente pessoal de programação Python")

# Texto auxiliar abaixo do título
st.caption("Faça sua pergunta sobre a linguagem Python e obtenha explicação, código, exemplo e referências.")

# Inicializa o histórico de mensagens da sessão, caso ainda não existe
if "messages" not in st.session_state:  # session_state é um objeto especial do streamlit é um dicionário persistente
    st.session_state.messages = []  # guarda {role: "",content: "" }

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for message in st.session_state.messages:  # Percorre cada mensagem da lista
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Inicializa a variável do cliente Groq como None
client = None

# verifica se o usuário forneceu a chave de API Groq - Verifica se groq_api_key possui algo digitado
if groq_api_key:
    try:
        # Cria cliente Groq com a Chave API fornecida
        client = Groq(api_key=groq_api_key)
    except Exception as e:

        # Exibe erro caso haja problema ao inicializar cliente
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()

# Caso não tenha chave, mas já existam mensagens mostra aviso
elif st.session_state.messages:
    st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")

# Captura a entrada do usuário no chat
if prompt := st.chat_input("Qual a sua dúvida sobre Python, pequeno gafanhoto?"):

    # Se não houver um cliente válido, mostra aviso e para a execução
    if not client:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para começar.")
        st.stop()

    # Armazena a menssagem do usuário no estado da sessão
    st.session_state.messages.append({"role": "user", "content": prompt})

    # exibe a mensagem do usuário no estado da sessão
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara mensagens para enviar à API, incluindo prompt de sistema
    messages_for_API = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        messages_for_API.append(msg)

    # Cria a resposta do assistente no chat
    with st.chat_message("assistant"):
        with st.spinner("Analisando sua pergunta..."):
            try:
                # Chama a API Groq para gerar a resposta
                chat_completion = client.chat.completions.create(
                    messages=messages_for_API,
                    model="openai/gpt-oss-20b",
                    temperature=0.7,
                    max_tokens=2048
                )

                # Extrai a resposta gerada pela API - Retorna diversas informações, por isso é importante filtrar a informação
                asy_ai_resposta = chat_completion.choices[0].message.content

                # Exibe a resposta gerada
                st.markdown(asy_ai_resposta)

                # Armazena a resposta do asy no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content": asy_ai_resposta})

            # Caso ocorra algum erro
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API Groq: {e}")

# Marca d'agua
st.markdown(
    """
    <div style="text-align: center; color:gray;">
        <hr>
        <p>Professor Asy - Parte Integrante do Curso Gratuito Fundamentos de Linguagem Python da Data Science Academy</p>
    </div>
    """,
    unsafe_allow_html=True
)
