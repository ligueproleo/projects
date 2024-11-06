import streamlit as st
import openai

# Configuração da API do OpenAI
openai.api_key = "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"

# Lista para armazenar o histórico da conversa
conversation_history = []

# Função para interagir com a LLM ChatGPT3+
def interact_with_chatbot(question):
    conversation_history.append(f"Usuário: {question}")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="\n".join(conversation_history),
        max_tokens=50
    )
    conversation_history.append(f"Psicólogo Virtual: {response.choices[0].text.strip()}")
    return response.choices[0].text.strip()

# Interface do Streamlit
def main():
    st.title("Dr. Crazy Jung - Consulta Psicológica Virtual")
    st.image("static/crazy_jung.png", use_column_width=True)
    st.write("Bem-vindo! Eu sou o Dr. Crazy Jung, um psicólogo Junguiano. O risco de ser atendido por mim é todo seu.")

    # Entrada de texto do usuário
    user_input = st.text_input("Faça sua pergunta (estilo psicologia de Carl Jung):")

    if st.button("Enviar"):
        if user_input.strip():
            response = interact_with_chatbot(user_input)
            st.text_area("Resposta do Psicólogo Virtual:", response, height=100)

    st.text("Conversa:")
    for msg in conversation_history:
        st.write(msg)

if __name__ == "__main__":
    main()
