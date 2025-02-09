import streamlit as st
import random
import os
import pandas as pd

questions_1 = [
    "Warm", "Well-intentioned", "Friendly",
    "Competent", "Skillful", "Intelligent", "Dominant",
    "Assertive", "Forceful"
]

questions_2 = ["This chatbot is accurate", "This chatbot is authentic", "This chatbot is believable"]

questions_4 = ["I would like to keep interacting with the chatbot in the future.", 
               "I would recommend this chatbot to my friends.",
               "I wish I had an agent such as this chatbot."]

def cache_response(response):
    # Display collected responses
    page_name = st.session_state.pages_name[st.session_state.page]
    st.session_state.responses[page_name] = response

def post_intro():
    st.write("""
    You have completed the Q&A session with the chatbot. 
             
    We will now ask you a few questions about your thoughts on this chatbot. Please answer honestly.
    """)

def post_page_1():
    # Define the survey questions and Likert scale labels
    response = {val: None for val in questions_1}

    slider_labels = [
        "1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"
    ]


    # Header
    st.write("**C2. In your opinion, how well does each of the following words describe this chatbot?**")

    # Render questions with select sliders
    if "rquestions_1" not in st.session_state:
        st.session_state.rquestions_1 = random.sample(questions_1, len(questions_1))
    questions = st.session_state.rquestions_1

    # for question in questions:
    #     st.write(f"> {question}")
    #     selected_value = st.pills(
    #         label=f"{question}",  # Hidden label for accessibility
    #         options=slider_labels,  # Custom labels
    #         default=None,  # Default to neutral 
    #         key=f"slider_{question}",
    #         label_visibility="collapsed"
    #     )

    # Render questions with radio buttons in a grid
    ra = 0.18
    rb = 0.105
    rc = 0.178
    rd = 1 - ra - rb - rc
    cols = st.columns([ra, rb, rc, rd])
    with cols[1]:
        st.markdown("<div style='text-align: center;'>Not</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; margin-top:-5px;'>at all</div>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown("<div style='text-align: center;'>Very</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; margin-top:-5px;'>well</div>", unsafe_allow_html=True)


    ra = 0.2275
    rb = 0.0231
    rc = 1 - ra - 7 * rb
    cols = st.columns([ra] + 7 * [rb] + [rc])           
    with cols[1]:
        st.write("1")
    with cols[2]:
        st.write("2")
    with cols[3]:
        st.write("3")
    with cols[4]:
        st.write("4")
    with cols[5]:
        st.write("5")
    with cols[6]:
        st.write("6")
    with cols[7]:
        st.write("7")

    for question in questions:
        cols = st.columns([2, 7])  # Adjusted ratio for better alignment
        with cols[0]:
            st.markdown(f"<div style='padding-top: 10px;'>{question}</div>", unsafe_allow_html=True)
            
        with cols[1]:
            selected_value = st.radio(
                label=question,
                options=["", "", "", "", "", "", ""],
                horizontal=True,
                key=f"radio_{question}",
                index=None,
                label_visibility="collapsed",
            )

            # Update session state
            if selected_value is not None:
                response[question] = selected_value
        # else:
        #     st.warning("You must select one")

    cache_response(response)

def post_page_2():
    # Define the survey questions and Likert scale labels
    response = {val: None for val in questions_2}

    slider_labels = [
        "1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"
    ]


    # Header
    st.write("**C3. To what extent do you agree with the following statements?**")

    if "rquestions_2" not in st.session_state:
        st.session_state.rquestions_2 = random.sample(questions_2, len(questions_2))
    rquestions_2 = st.session_state.rquestions_2

    for question in rquestions_2:
        st.write(f"> {question}")
        selected_value = st.pills(
            label=f"{question}",  # Hidden label for accessibility
            options=slider_labels,  # Custom labels
            default=None,  # Default to neutral 
            key=f"slider_{question}",
            label_visibility="collapsed"
        )

        # Update session state
        if selected_value is not None:
            response[question] = selected_value[0]
        # else:
        #     st.warning("You must select one")

    cache_response(response)

def post_page_3():
    question = "C4. In your opinion, how human-like is this chatbot?"
    # st.write(f"> **{question}**")
    # response = st.slider(
    #     label=f"{question}",
    #     min_value=0,           # Minimum value
    #     max_value=100,         # Maximum value
    #     value=0,              # Default value
    #     step=1,                 # Step size for continuous selection
    #     label_visibility="collapsed",
    #     disabled=False
    # )

    # Placeholder to display the slider value
    slider_placeholder = st.empty()
    col1, col2, col3 = st.columns([1, 7, 1])  # Adjust column widths for alignment
    with col1:
        st.write("0 = Not at all human-like")
    with col3:
        st.write("100 = Extremely human-like")
    # Create a slider with no initial value displayed
    response = st.slider(
        "Choose a value:",
        min_value=0,
        max_value=100,
        value=-1,  # Default value required by Streamlit
        key="slider_key",
        label_visibility="collapsed"
    )
    if response == -1:
        response = None
    # Logic to show the slider only after the user interacts
    if st.session_state.slider_key != 50:  # Check if the value has changed
        slider_placeholder.write(f"Selected value: {response}")
    else:
        slider_placeholder.write("No value selected yet.")

    cache_response({question: response})

def post_page_4():
    # Define the survey questions and Likert scale labels
    response = {val: None for val in questions_4}

    slider_labels = [
        "1 (Strongly disagree)", "2", "3", "4", "5", "6", "7 (Strongly agree)"
    ]


    # Header
    st.write("**To what extent do you agree with the following statements?**")

    if "rquestions_4" not in st.session_state:
        st.session_state.rquestions_4 = random.sample(questions_4, len(questions_4))
    rquestions_4 = st.session_state.rquestions_4

    for question in rquestions_4:
        st.write(f"> {question}")
        selected_value = st.pills(
            label=f"{question}",  # Hidden label for accessibility
            options=slider_labels,  # Custom labels
            default=None,  # Default to neutral 
            key=f"slider_{question}",
            label_visibility="collapsed"
        )

        # Update session state

        if selected_value is not None:
            response[question] = selected_value[0]
        # else:
        #     st.warning("You must select one")

    cache_response(response)

def debrief():
    st.title("Debriefing Statement")
    st.write("""
Thank you very much for participating in this study.

The research title presented to you before the study, “User perceptions of generative AI chatbots” was a false title used to ensure the reliability of the study. The actual purpose of this study is to understand how users respond to a chatbot’s expressions of certainty or uncertainty regarding inaccurate information. We used a false title, because revealing the true purpose of the study beforehand could have influenced your answers.

The chatbot you interacted with during the study was a simulated program created specifically for this experiment. Please note that all of the chatbot’s responses were intentionally false and inaccurate.

You are free to withdraw from this study at any time. If you choose to withdraw, your data will be permanently deleted. If you don’t want your responses to be used in the study, please contact us at jwp14812@snu.ac.kr. However, please be aware that in such cases, payment will not be provided.

Once again, thank you for your participation. 
    """)
    consent = st.radio("Do you agree to submit your response?", ["Agree", "Disagree"], index=1)
    
    if consent == "Agree":
        if st.button("Submit"):
            save_results()
    # if consent == "Disagree":
    #     st.warning("You must agree to make a final submission.")

def save_results():
    responses = st.session_state.responses
    experiments = st.session_state.experiments
    flattened_experiments = []
    for experiment in experiments:
        flattened_experiments += experiment

    flattened_responses = pd.json_normalize(responses)  # Flattened responses
    columns = []
    for i in range(13):
        columns += [f"question_{i+1}", f"suggested_confidence_{i+1}", f"user_feedback_{i+1}", f"question_index_{i+1}", f"confidence_sampling_group_index_{i+1}"]
    experiments_df = pd.DataFrame([flattened_experiments], columns=columns)
    data_to_save = pd.concat([flattened_responses, experiments_df], axis=1)
    
    # Filepath to save data
    csv_file_path = "responses.csv"

    # Save to CSV (append if exists)
    if os.path.exists(csv_file_path):
        data_to_save.to_csv(csv_file_path, mode='a', index=False, header=False)  # Append without headers
        print(f"Data appended to {csv_file_path}")
    else:
        data_to_save.to_csv(csv_file_path, mode='w', index=False, header=True)  # Write new file with headers
        print(f"New file created: {csv_file_path}")

    st.session_state.page += 1

    st.rerun()

def closing_page():
    st.write("Thank you for participating in this study. Your responses have been recorded.")
    st.write("You may now close this tab.")
    st.stop()