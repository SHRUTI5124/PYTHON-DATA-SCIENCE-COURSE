import streamlit as st

st.title("Demo App 😊")

n1=st.number_input("Enter no.:")
n2=st.number_input("Enter another no.:")
name=st.text_input("Enter your name:")
c1,c2,c3,c4,c5,c6,c7=st.columns(7)
add=c1.button("Add")
sub=c2.button("Subtract")
mul=c3.button("Multiply")
div=c4.button("Division")
exp=c5.button("Exponent")
mod=c6.button("Modulus")
floor=c7.button("Floor division")
if add:
    r=int(n1)+int(n2)
    st.success(r)
if sub:
    r=int(n1)-int(n2)
    st.success(r)
if mul:
    r=int(n1)*int(n2)
    st.success(r)
if div:
    r=int(n1)/int(n2)
    st.success(r)
if exp:
    r=int(n1)**int(n2)
    st.success(r)
if mod:
    r=int(n1)%int(n2)
    st.success(r)
if floor:
    r=int(n1)**int(n2)
    st.success(r)