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
    rquestions_1 = st.session_state.rquestions_1

    for question in rquestions_1:
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
    st.write(f"> **{question}**")
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
            st.session_state.submission_consent = True
    if consent == "Disagree":
        if st.button("Next"):
            st.session_state.page += 1
            st.session_state.submission_consent = False


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
    



    # Call the function to send email
    send_results_email(data_to_save, "jwp14812@snu.ac.kr")



    st.session_state.page += 1

    st.rerun()

def closing_page():
    if st.session_state.submission_consent:
        st.write("Thank you for participating in this study.")
        st.write("Please click the link below to return to Prolific and complete your participation.")
        st.markdown("[https://app.prolific.com/submissions/complete?cc=C12E2UJG](https://app.prolific.com/submissions/complete?cc=C12E2UJG)")
        st.stop()
    else:
        st.write("Thank you for participating in this study. Your responses will not be submitted.")
        st.write("Please click the link below to exit the study.")
        st.markdown("[https://app.prolific.com/submissions/complete?cc=C1MT56Z4](https://app.prolific.com/submissions/complete?cc=C1MT56Z4)")
        st.stop()

def send_results_email(data_df, recipient_email):
    # Convert DataFrame to CSV string
    csv_data = data_df.to_csv(index=False)
    
    # Create email message with CSV attachment
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication
    
    msg = MIMEMultipart()
    msg['Subject'] = 'Study Results Data'
    msg['From'] = st.secrets["EMAIL"]
    msg['To'] = recipient_email
    
    # Attach CSV file
    attachment = MIMEApplication(csv_data)
    # Generate a unique filename using timestamp and random string
    from datetime import datetime
    import uuid
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    filename = f"study_results_{timestamp}_{unique_id}.csv"
    attachment['Content-Disposition'] = 'attachment; filename="study_results.csv"'
    msg.attach(attachment)
    
    # Send email
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(st.secrets["EMAIL"], st.secrets["EMAIL_PASSWORD"])
    smtp_server.send_message(msg)
    smtp_server.quit()