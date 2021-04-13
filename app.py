# streamlit option
import streamlit as st
from admin.func import first_func, second_func, third_func, fourth_func, fifth_func


def main():

    f1 = first_func()
    f2 = second_func()
    f3 = third_func()
    f4 = fourth_func()
    f5 = fifth_func()

    # prepare variables for user input
    equation = ""

    st.header("Basic Functions")
    st.markdown(
        "**Input an expression/equation with the following functions: f1, f2, f3, f4, f5**"
    )
    st.markdown("**eg. (f1 + f2) * 5**")

    # user input
    equation = st.text_input("Expression/equation")

    if not equation:
        st.warning("Please input an expression/equation")
        st.stop()

    try:
        st.write("Output", eval(equation))
    except:
        st.write("User input error - try again")


if __name__ == "__main__":
    main()
