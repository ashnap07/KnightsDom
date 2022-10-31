import streamlit as st
import Kdom as kd

header = st.container()
input = st.container()
result=st.container()

@st.cache # 👈 This function will be cached
def Search(s):
    return kd.kights_dom(s)
with header:
    st.title("Knights Domination Generlized Problem ♟")

with input:
    s=st.text_input("Enter the chessboard dimension:")
    
    try:
        s=int(s)
    except ValueError:
        s=0
with result:
    st.header("Searching result for chessboard of size "+str(s)+"X"+str(s)+" :")
    r1,r2,r3="","",""
    try:
        r1,r2,r3=Search(s)
    except ValueError:
        r1,r2,r3=0,0,0
    st.subheader("Chessboard After 10 itreations:")
    st.text(r1)

    st.subheader("Chessboard After 100 itreations:")
    st.text(r2)

    st.subheader("Chessboard After 1000 itreations:")
    st.text(r3)
    
