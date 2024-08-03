import streamlit as st 
from chains import load_normal_chain
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

# Page Background settings
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: linear-gradient(to bottom, #2c2c42, #2a2b43, #272b45, #242a46, #202a48, #1d2948, #1a2748, #172648, #152346, #141f45, #131c43, #131841);}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
[data-testid="stSidebar"]{
background-image: linear-gradient(to bottom, #27274a, #2a2d53, #2c345c, #2e3a66, #30416f, #304271, #314474, #314576, #314171, #313d6c, #313967, #303562);}
</style>
"""

def load_chain(chat_history):
    return load_normal_chain(chat_history)

def clear_send_input():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""

def set_send_input():
    st.session_state.send_input = True
    clear_send_input()

def main():
    st.set_page_config(page_icon="💬", page_title="ChatMosaic", layout='centered')
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title("💬 Welcome to ChatMosaic : Your local chat-bot")

    chat_container = st.container()
    chat_history = StreamlitChatMessageHistory(key="history")
    llm_chain = load_chain(chat_history)

    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""
        
    st.sidebar.info('''**ChatMosaic** is a local chatbot application built with Streamlit. It enables you to start and manage multiple chat sessions, 
        providing a seamless and interactive experience. Whether you're chatting with the bot for fun, getting assistance with queries, 
        or exploring the capabilities of language models, ChatMosaic offers an intuitive interface to interact with your AI assistant.''')
    st.sidebar.divider()
    st.sidebar.markdown("Developed by : Ayush Saini")
    user_input = st.text_input("Message ChatMosaic", key="user_input" ,on_change=set_send_input)
    send_button = st.button("Send", key="send_button")

    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
            with chat_container:
                llm_response = llm_chain.run(st.session_state.user_question)
                st.session_state.user_question = ""

    if chat_history.messages != []:
        with chat_container:
            st.write("Chat history")
            for message in chat_history.messages:
                st.chat_message(message.type).write(message.content)

if __name__ == "__main__":
    main()
