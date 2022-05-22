import streamlit as st


def get_session(*keys):
    session_data = tuple(st.session_state.get(key) for key in keys)
    return session_data

def set_session(**kwargs):
    for key, value in kwargs.items():
        st.session_state[key] = value
