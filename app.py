import streamlit as st

def test_deploy():
    return "Testing depoy using Docker"

def main():
    st.write(test_deploy())

if __name__ == "__main__":
    main()