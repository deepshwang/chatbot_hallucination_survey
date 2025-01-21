import streamlit as st

def intro_page():
    st.title("User perceptions of generative AI chatbots")
    text = """
Hello, thank you for your interest in this study. 

Please read the following instructions carefully. 

The study will begin only after you agree to participate. Participation is completely voluntary.
"""
    st.write(text)
def consent_page():
    st.title("Instruction and Consent for a Research Participant")
    
    consent_text = """
> **Title of study: User perceptions of generative AI chatbots**

> **Principal Investigator: Eun-Ju Lee (Professor, Seoul National University)**

We are conducting a study to explore how people perceive generative artificial intelligence (AI) chatbots. You are invited to participate because you are 18 or older, can read and understand basic information, and are comfortable sharing your opinions. Jin Won Park, a research assistant at Seoul National University, will provide details about the study. Participation is entirely voluntary, so please take your time to review the information below and decide if you'd like to join. Feel free to discuss this with family or friends, and let us know if you have any questions.

### **1. Why is this study being conducted?**

This study aims to explore your opinions and experiences when interacting with generative AI chatbots. You’ll engage in a simple Q&A session with a chatbot online and then answer some questions about your experience.

### **2. How many people will participate in the study?**

A total of 1,800 individuals aged 18 or older will take part in this study.

### **3. How will the study proceed?**

Once you review these instructions and agree to participate, the study will proceed as follows:
1)	First, we will ask you some questions about yourself (age, gender, race, education, income etc) and your general views on AI.
2)	Next, you’ll participate in a brief Q&A session with a generative AI chatbot.
3)	Afterward, you will answer some questions about your experience with the chatbot. 
You can participate from any location where you feel comfortable and able to focus, but please access the study using a PC rather than a smartphone. 

### **4. How long will the study take?**

The study will take about 15 to 20 minutes to complete.

### **5. Can I stop participating after the study has begun?**

Yes, you can stop participating at any time without penalty. If you choose to withdraw, simply stop responding and close the browser window. Your answers will not be saved if you exit the study early. However, please note that you will not receive payment in this case. 

### **6. Are there any side effects or risks associated with this study?**

There are no known risks or side effects associated with participating in this study.

### **7. Are there any advantages to participating in the study?**

You will not receive any direct benefits from participating. However, the information you provide will contribute to a better understanding of user interactions with AI chatbots.

### **8. Are there any disadvantages to participating in the study?**

Participation is entirely voluntary, and there are no disadvantages if you choose not to participate.
   
### **9. Is the data collected during the study secure?**

Our principal investigator, Professor Eun-Ju Lee (+82-2-880-6469) at Seoul National University is in charge of managing all personal information collected in this study. Personal information collected in this study includes age, gender, race, education, and income. This information is only allowed access by Professor Eun-Ju Lee (Seoul National University), Professor Sukyoung Choi (Yonsei University), and research assistant Jin Won Park (Seoul National University). All data will be stored on a password-protected computer in Professor Eun-Ju Lee’s office at the Department of Communication, Seoul National University. The consent form will be stored for three years in accordance with the relevant laws and then discarded. The study data will be kept for as long as necessary, in line with Seoul National University’s Research Ethics Guidelines. All possible measures will be taken to secure and protect any personal information collected during the study. Your personal information will not be disclosed when the study is published in an academic journal or presented at a conference, unless required by law. Additionally, the Seoul National University Institutional Review Board may access the study data, within the scope of relevant regulations, to verify that personal information has been protected and to ensure the reliability of the study. By signing this consent form, you acknowledge that you have been informed of all necessary information related to the study and that you agree to participate. 

### **10. How much will participants be paid?**

You will be paid approximately $2.70 (rate: $8 per hour) for completing the study. 

### **11. If I have any questions about the study, whom can I contact?**

If you have any questions, concerns, or issues related to the study, please feel free to contact our research assistant.

***Name: Jin Won Park***	    

***Contact: jwp14812@snu.ac.kr***

If you have any questions related to your rights as a study participant, please contact the Seoul National University Institutional Review Board as shown below.  

Seoul National University Institutional Review Board (SNUIRB)

Phone: +82-2-880-5153

E-mail: irb@snu.ac.kr

# Consent Form

> **Title of study: User perceptions of generative AI chatbots**

> **Principal Investigator: Eun-Ju Lee (Professor, Seoul National University)**

1.	I have read the instructions above thoroughly and discussed them with the investigator. 
2.	I have been made aware of the potential risks and benefits of participating in the study, and I have received satisfactory answers to all my queries. 
3.	I voluntarily agree to participate in the study. 
4.	I agree to collection and processing of any personal information gathered during the study within the bounds of the existing legislation and regulations of the Institutional Review Board.
5.	I agree that my personal information, which will be otherwise kept secured by the investigator(s), may be accessed by government institutions prescribed by laws and regulations and the SNU Institutional Review Board for auditing purposes.
6.	I understand that I can withdraw participation in the study whenever I want without any risk to me. 


    """

    st.write(consent_text)
    
    
    consent = st.radio("**Do you agree to the terms outlined above and wish to participate in the study?**", ["Agree", "Disagree"], index=1)
    
    if consent == "Agree":
        st.session_state["agree"] = True
    if consent == "Disagree":
        st.session_state["agree"] = False 
        st.warning("You must agree to participate to proceed.")

def thanks_page():
    st.title("Thank you!")
    thanks_text = """
Thank you for agreeing to participate. We will now begin the study. 

**Please avoid refreshing or closing the page during the study, as it may cause errors and affect your payment**.
"""
    st.write(thanks_text)