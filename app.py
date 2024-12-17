import streamlit as st
def wide_space_default():
    st.set_page_config(layout="wide")
wide_space_default()

import pandas as pd
from io import BytesIO

from contents.consent import consent_page, thanks_page, intro_page
from contents.survey import *
from contents.interaction import *
from contents.post_interaction import *

# Initialize the page state in session_state
if "page" not in st.session_state:
    st.session_state.page = 0
# Agree flag
if "agree" not in st.session_state:
    st.session_state.agree = False


# Function to handle page changes
def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1



# Main function to control the flow
def main():
    pages = [intro_page, consent_page, thanks_page, 
             survey_page_1, survey_page_2, survey_page_3_intro, survey_page_3, survey_page_4, 
             interaction_intro, interaction_page,
             post_intro, post_page_1, post_page_2, post_page_3, post_page_4, debrief, closing_page]
    st.session_state.pages_name = [f.__name__ for f in pages]
    if "interaction_done" not in st.session_state:
        st.session_state.interaction_done= False
    if "all_done" not in st.session_state:
        st.session_state.all_done = False

    # Set up responses state
    if "responses" not in st.session_state:
        st.session_state.responses = {}
    # Display the current page
    pages[st.session_state.page]()

    col1, _, _, _, col2 = st.columns(5)
    with col1:
        if st.session_state.page > 0 and not st.session_state.all_done:
            st.button("Previous", on_click=prev_page)

    with col2:
        if st.session_state.page == 0 or st.session_state["agree"]:
            if not (st.session_state.page == st.session_state.pages_name.index("interaction_page") and not st.session_state.interaction_done):
                if st.session_state.page < (len(pages)-2):
                    st.button("Next", on_click=next_page)

if __name__ == "__main__":
    main()