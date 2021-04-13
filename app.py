# streamlit option
import streamlit as st
import pandas as pd
from admin.func import first_func, second_func, third_func, fourth_func, fifth_func


def main():
    # function definition - these are used at interface
    f1 = first_func()
    f2 = second_func()
    f3 = third_func()
    f4 = fourth_func()
    f5 = fifth_func()

    # little bit of styling
    st.header("Basic Functions")
    st.markdown(
        "**Input an expression/equation with the following functions: f1, f2, f3, f4, f5**"
    )
    st.markdown("**eg. (f1 + f2) * 5**")

    # caching option - not uber sophisticated
    @st.cache(allow_output_mutation=True)
    def get_data():
        return []

    # user input
    equation = st.text_input("Expression/equation")

    # empty input handling
    if not equation:
        st.warning("Please input an expression/equation")
        st.stop()

    # output and error handling
    try:
        st.write("Output", eval(equation))
        get_data().append({"Expression": equation, "Output": eval(equation)})
        st.write(pd.DataFrame(get_data()))
    except:
        st.write("User input error - try again")


if __name__ == "__main__":
    main()
