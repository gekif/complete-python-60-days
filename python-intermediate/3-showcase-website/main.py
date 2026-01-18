import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Dzulfikar Maulana")
    content = """
    Hello! I'm Dzulfikar Maulana, a passionate software developer with a keen interest in building innovative solutions. With a background in computer science, I specialize in web development and have experience working with various programming languages and frameworks. I'm always eager to learn new technologies and take on challenging projects. Let's connect and create something amazing together!
    """
    st.write(content)