import streamlit as st
import time
import pandas as pd
import random

def read_hallucinations():
    df = pd.read_excel("contents/hallucinations.xlsx", sheet_name="Sheet1")
    questions = df[['Question', 'Hallucination']].values.tolist()
    random.shuffle(questions)
    return questions

def select_random_condition():
    conditions = {0: 13 * ["None"],
                  1: 4 * ["60%"] + 5 * ["80%"] + 4 * ["100%"],
                  2: 1 * ["60%"] + 11 * ["80%"] + 1 * ["100%"],
                  3: 4 * ["40%"] + 5 * ["60%"] + 4 * ["80%"],
                  4: 1 * ["40%"] + 11 * ["60%"] + 1 * ["80%"],
                  5: 4 * ["quite"] + 5 * ["highly"] + 4 * ["extremely"],
                  6: 1 * ["quite"] + 11 * ["highly"] + 1 * ["extremely"],
                  7: 1 * ["fairly"] + 11 * ["quite"] + 1 * ["highly"],
                  8: 1 * ["fairly"] + 11 * ["quite"] + 1 * ["highly"],
                  }
    idx = random.randint(0, 8)
    condition = conditions[idx]
    random.shuffle(condition)
    if idx > 0:
        return [f"Confidence: I am {c} confident" for c in condition], idx
    else:
        return condition, idx

def interaction_intro():
    st.write("""
    Now, you will interact with AI chatbot. 
    You will ask the chatbot some questions and it will respond. 
    Please read the instructions below carefully

    >
    > 1. On the next page, you will see a list of questions. `Select` one question and `ask` the chatbot.
    > 2. Carefully review the chatbot’s answer.
    > 3. Rate the accuracy of the answer. 
    >

    You will ask the chatbot a total of 13 different questions. Click `Next` if you are ready to begin.

    """)

def interaction_page():
    # Initialize session state variables for interaction box, responses, and AI thinking state
    if "interaction_box" not in st.session_state:
        st.session_state.interaction_box = ""  # For input box
    if "h_responses" not in st.session_state:
        st.session_state.h_responses= []  # To store chat interactions
    if "ai_thinking" not in st.session_state:
        st.session_state.ai_thinking = False  # To track AI thinking state
    if "last_response" not in st.session_state:
        st.session_state.last_response = None # To store last AI response
    if "questions" not in st.session_state and "answers" not in st.session_state:
        hallucinations = read_hallucinations()
        st.session_state.questions = [data[0] for data in hallucinations]
        st.session_state.original_questions= [data[0] for data in hallucinations]
        st.session_state.answers = {item[0]: item[1] for item in hallucinations}
    if "confidence" not in st.session_state:
        st.session_state.confidence, st.session_state.cfd_idx = select_random_condition()
    if "experiments" not in st.session_state:
        st.session_state.experiments = []
    if 'cfd' not in st.session_state:
        st.session_state.cfd = "None"

    # Instructions
    st.write("### :blue[Intructions]")
    st.markdown(f"""
    **:blue[1. Choose a question from the list below, then click submit.]**  
    **:blue[2. The question will appear in the chat box.]**  
    **:blue[3. Click the arrow button to ask your question and see the chatbot's response.]**  
    
    ### **:red[Your task: {len(st.session_state.confidence)}/13 questions remaining.]**
    """)

    # Layout with two columns
    col1, col2 = st.columns([1, 1])

    # Left column: Question list with auto-paste feature
    with col1:
        st.write("### Question List")
        selected_question = st.radio(
            "Click a question:",
            options=st.session_state.questions,
            index=None,
            label_visibility="collapsed"
        )
        if selected_question:
            st.session_state.interaction_box = selected_question  # Auto-paste to input box

    # Right column: Chat window and interaction box
    with col2:
        st.write("### Chat Box")
        
        # Display chat history (all user questions, AI responses, and thinking messages)
        for interaction in st.session_state.h_responses:
            st.markdown(interaction, unsafe_allow_html=True)

        # Interaction box below the chat window
        st.write("---")
        st.write("### Type your question here")
        st.write("*(select one of the questions from the left)*")
        user_input = st.text_input(
            label="Type your question here *(select one of the questions from the left)*:",
            value=st.session_state.interaction_box,
            key="input_box",
            label_visibility="collapsed"
        )
        # Submit button to send the question
        if st.session_state.last_response is None:
            if st.button("⏎", key="Ask_button"):
                user_question = user_input.strip()
                st.session_state.user_question = user_question
                if user_question:
                    # Add user's question to chat history
                    user_message = f"""
                    <div style="
                        background-color: #e3d8d8; 
                        padding: 10px; 
                        border-radius: 10px; 
                        color: black; 
                        width: fit-content; 
                        font-size: 16px;
                        margin-bottom: 5px;
                        margin-left: auto;
                        margin-right: 0;">
                        {user_question}
                    </div>
                    """
                    st.session_state.h_responses.append(user_message)
                    if user_question in st.session_state.questions:
                        st.session_state.question_idx = st.session_state.original_questions.index(user_question)
                        st.session_state.questions.remove(user_question)

                    # Add "thinking" message to chat history
                    thinking_message = """
                    <div style="
                        background-color: #f5f0f0; 
                        padding: 10px; 
                        border-radius: 10px; 
                        color: grey; 
                        width: fit-content; 
                        font-size: 16px;
                        margin-bottom: 5px;">
                        ֎🇦🇮 is thinking...
                    </div>
                    """
                    st.session_state.h_responses.append(thinking_message)
                    st.session_state.ai_thinking = True  # Set AI thinking state
                    st.session_state.interaction_box = ""  # Clear interaction box
                    st.rerun()  # Rerun to show "thinking" message first

    # Handle AI response after "thinking"
    if st.session_state.ai_thinking:
        time.sleep(2)  # Simulate AI "thinking" delay
        fail_msg = "Sorry, I don't know the answer to that question. You may ask the question from the list!"
        ai_response_text = st.session_state.answers.get(st.session_state.user_question, fail_msg)
        fail = ai_response_text == fail_msg
        ai_message = f"""
        <div style="
            background-color: #f5f0f0; 
            padding: 10px; 
            border-radius: 10px; 
            color: black; 
            width: fit-content; 
            font-size: 16px;
            margin-bottom: 5px;">
            ֎🇦🇮: {ai_response_text}
        </div>
        <div></div>
        """
        if not fail:
            st.session_state.cfd = st.session_state.confidence.pop()
        else:
            st.session_state.cfd = "None"
        
        if st.session_state.cfd != "None":
            ai_message = f"""
            <div style="
                background-color: #f5f0f0; 
                padding: 10px; 
                border-radius: 10px; 
                color: black; 
                width: fit-content; 
                font-size: 16px;
                margin-bottom: 5px;">
                ֎🇦🇮: {ai_response_text}
            </div>
            <div style="
                background-color: #f5f0f0; 
                padding: 10px; 
                border-radius: 10px; 
                color: black; 
                width: fit-content; 
                font-size: 24px;
                margin-bottom: 5px;
                font-weight: bold;">
                {st.session_state.cfd}
            </div>            
            """
        if fail:
            st.session_state.last_response = None
        else:
            st.session_state.last_response = ai_response_text
        
        # Replace "thinking" message with the actual response
        st.session_state.h_responses[-1] = ai_message
        st.session_state.ai_thinking = False  # Reset AI thinking state
        st.rerun()

    # After conversation, collect user feedback
    with col2:
        if st.session_state.last_response:
            st.write("---")
            st.write("### :red[In your opinion, how accurate is this response?]")
            st.write("***You must answer to proceed!!***")
            feedback = st.pills(
                "C1. In your opinion, how accurate is this response?",
                options=["1 (Not at all accurate)", "2", "3", "4", "5", "6", "7 (Very accurate)"],
                label_visibility="collapsed"
            )
            if feedback is not None:
                if len(st.session_state.confidence) > 0:
                    if st.button("Next Question", key="Next Question"):
                        st.session_state.h_responses = []
                        st.session_state.last_response = None
                        st.session_state.experiments.append([st.session_state.user_question, st.session_state.cfd, feedback, st.session_state.question_idx, st.session_state.cfd_idx])
                        st.rerun()
                else:
                    st.write("### Done! Please proceed")
                    if not st.session_state.interaction_done:
                        st.session_state.experiments.append([st.session_state.user_question, st.session_state.cfd, feedback, st.session_state.question_idx, st.session_state.cfd_idx])
                    st.session_state.interaction_done = True