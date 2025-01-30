import streamlit as st
import random
# Function to display survey page

questions_2 = [
    "Acts like a leader", "Has leadership abilities", "Strong personality",
    "Dominant", "Makes decisions easily", "Defends own beliefs",
]

questions_3 = [
    "Objective", "Error-free", "Neutral",
    "Accurate", "Cooperative", "Sociable", "Friendly",
    "Warm", "Knowledgeable", "Conscious", "Capable", "Reliable"
]

def cache_response(response):
    # Display collected responses
    page_name = st.session_state.pages_name[st.session_state.page]
    st.session_state.responses[page_name] = response

def survey_page_1():
    # Embedded Survey Questions
    questions = {
        "1": "What is your current age?",
        "2": "What is your gender?",
        "3": "What is your racial/ethnic category? (You can choose the closest one)",
        "4": "What is the highest degree or level of school you have completed? If currently enrolled, pick the highest degree you have received.",
        "5": "Currently, what is your total annual household income?",
        "6": "Are you a native English speaker?",
        "7": "How will you rate your English proficiency on a 5-point scale? Here, 1 means elementary proficiency and 5 means full-bilingual proficiency."
    }

    response = {}

    # Dictionary to store responses
    select_responses = {"2": ["Male", "Female", "Non-binary", "Prefer not to answer"],
                 "3": ["American Indian or Alaskan Native", "Asian", "Black or African American", "Hispanic or Latinx", "White or Caucasian", "Other", "Prefer not to answer"],
                 "4": ["No schooling completed", "High school graduate, diploma or the equivalent (for example: GED)", "Bachelor's degree", "Master's degree", "Doctorate degree", "Other", "Prefer not to answer"],
                 "5": ['\$0 ~ $15,000', "\$15,001 ~ $25,000", "\$25,001 ~ $35,000", "\$35,001 ~ $50,000", "\$50,001 ~ $75,000", "\$75,001 ~ $100,000", "\$100,001 ~ $200,000", "More than \$200,000", "Prefer not to answer"],
                 "6": ["Yes", "No"],
                 "7": ["1 (Elementary proficiency)", "2 (Limited working proficiency)", "3 (Professional working proficiency)", "4 (Full professional proficiency)", "5 (Full bilingual proficiency)"]}


    for i, (qkey, question) in enumerate(questions.items()):
        if qkey in select_responses.keys():
            st.write(f"> **{qkey}. {question}**")
            response[question] = st.radio(f"**{question}**", [*select_responses[qkey]], key=f"select_{i}", label_visibility="collapsed", index=None)
        else:
            st.write(f"> **{qkey}. {question}**")
            response[question] = st.text_input(f"**{question}**", key=f"text_{i}", label_visibility="collapsed", value=None)
    
    cache_response(response)

def survey_page_2():
    # Define the survey questions and Likert scale labels
    response = {val: None for val in questions_2}

    slider_labels = [
        "1 \n (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"
    ]

    # Shuffle the list once and store it in session state
    if "shuffled_questions_survey_page_2" not in st.session_state:
        st.session_state.shuffled_questions_survey_page_2 = random.sample(questions_2, len(questions_2))


    # Store responses in session state
    questions = st.session_state.shuffled_questions_survey_page_2

    # Header
    st.write("**8. How well does each of the following words describe you?**")

    # Render questions with select sliders


    for question in questions:
        st.write(f"> **{question}**")
        selected_value = st.pills(
            label=question,  # Hidden label for accessibility
            options=slider_labels,  # Custom labels
            default=None,  # Default to neutral 
            key=f"slider_{question}",
            label_visibility="collapsed"
        )

        # Update session state
        if selected_value is not None:
            response[question] = selected_value[0]
        # else:
            # st.warning("You must select one")

    cache_response(response)

def survey_page_3_intro():
    st.write("**In the next section, we will ask you some questions about artificial intelligence (AI). Please answer honestly.**")
def survey_page_3():
    # Define the survey questions and Likert scale labels
    response = {val: None for val in questions_3}

    slider_labels = [
        "1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"
    ]


    # Shuffle the list once and store it in session state
    if "shuffled_questions_survey_page_3" not in st.session_state:
        st.session_state.shuffled_questions_survey_page_3 = random.sample(questions_3, len(questions_3))


    # Store responses in session state
    questions = st.session_state.shuffled_questions_survey_page_3

    # Header
    st.write("**9. In your opinion, how well does each of the following words describe artificial intelligence (AI)?**")

    # Render questions with select sliders


    for question in questions:
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
            # st.warning("You must select one")

    cache_response(response)

def survey_page_4():
    st.write("""
    There are AI chatbots that can produce text and images in response to the things people ask them for. 
    Sometimes called generative AI, these chatbots review large amounts of information to come up with their responses.
    """)

    questions = ["How well-informed do you consider yourself about generative AI chatbots (like ChatGPT, Claude, Gemini, Perplexity AI, etc.)?",
    "How often do you use generative AI chatbots?",
    "What do you use these AI chatbots for? (Choose all that apply)"]

    response = {}

    slider_labels = [
        "1 (Not informed at all)", "2", "3", "4", "5", "6", "7 (Very well-informed)"
    ]

    st.write(f"> **10. {questions[0]}**")
    selected_value = st.pills(
        label="10",  # Hidden label for accessibility
        options=slider_labels,  # Custom labels
        default=None,  # Default to neutral 
        key=f"slider_{questions[0]}",
        label_visibility="collapsed"
        )
    if selected_value is not None:
        response[questions[0]] = selected_value[0]
    # else:
        # st.warning("You must select one")

    options_11 = ["Never", "Used once or twice", "Use sometimes", "Use regularly"]
    st.write(f"> **11. {questions[1]}**")
    response[questions[1]] = st.radio(f"11. **{questions[1]}**", options_11, key="select_11", label_visibility="collapsed", index=None)

    if response[questions[1]] in ["Used once or twice", "Use sometimes", "Use regularly"]:


        st.write(f"> **12. {questions[2]}**")
        # options_12 = ["For entertainment", "To find new information related to my hobbies or interests", "For work", "For education and self-development", "Other"]
        a_a = st.checkbox('For entertainment')
        a_b = st.checkbox('To find new information related to my hobbies or interests')
        a_c = st.checkbox('For work')
        a_d = st.checkbox('For education and self-development')
        a_e = st.checkbox('Other')
        answers = [a_a, a_b, a_c, a_d, a_e]
        answers_templates = ["For entertainment", "To find new information related to my hobbies or interests", "For work", "For education and self-development", "Other"]
        # check if all answers are False
        if a_a is False and a_b is False and a_c is False and a_d is False and a_e is False:
            response[questions[2]] = None
        else:
            response[questions[2]] = [answers_templates[i] for i in range(len(answers)) if answers[i]]

        # response[questions[2]] = st.multiselect(questions[2], options_12, key="multiselect_10", label_visibility="collapsed")
    else:
        response[questions[2]] = "N/A"
    
    cache_response(response)