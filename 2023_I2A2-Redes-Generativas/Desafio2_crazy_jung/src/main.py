import streamlit as st
import openai

# Lendo a chave da API da OpenAI a partir do arquivo externo
def get_openai_key():
    try:
        with open("secrets/openai_key.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        st.error("Arquivo de chave da API não encontrado. Verifique o caminho do arquivo.")

# Configuração da chave da API da OpenAI
openai.api_key = get_openai_key()

# Função para interagir com o modelo GPT-3
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"Ocorreu um erro ao gerar a resposta. Detalhes do erro: {str(e)}"

# Interface do Streamlit
def main():
    st.set_page_config(
        page_title="Consulta Psicológica Virtual",
        page_icon=":brain:",
        layout="wide",
        initial_sidebar_state="expanded" # expande a barra lateral
    )

    st.markdown(
        """
        <style>
        /* Alteração na cor de fundo */
        body {
            background-color: black;
        }
        .stApp {
            max-width: 1350px;
        }
        .st-bd {
            background-color: black;
        }
        .st-em {
            font-size: 2.5rem;
        }
        .st-logo {
            width: 2cm;
            height: 2cm;
            object-fit: contain;
        }
        /* Alteração nas cores das fontes das mensagens */
        .stTextInput, .stTextArea, .stMarkdown, .stText p, .stText h1, .stText h2, .stText h3, .stText h4, .stText h5, .stText h6 {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Dr. Crazy Jung")
    st.image("images/logo.png", use_column_width=200, output_format="PNG", caption="Consulta Psicológica Virtual")

    st.write("Dr. Crazy Jung está ao seu dispor. Em que posso ajudá-lo?")

    user_input = st.text_area("Faça sua pergunta:", height=150)

    if st.button("Enviar"):
        if user_input:
            st.text_area("Sua Pergunta:", user_input[:300], height=150)  # Limitando a exibição
            response = generate_response(user_input)
            if response:
                st.text_area("Resposta de Dr. Crazy Jung:", response[:500], height=150)  # Limitando a exibição
            else:
                st.warning("A resposta da OpenAI está vazia.")
        else:
            st.warning("Por favor, insira uma pergunta antes de enviar.")

if __name__ == "__main__":
    main()
