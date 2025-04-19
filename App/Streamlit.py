import streamlit as st
import os
from dotenv import load_dotenv
import sys
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)


from PROMPT.prompts import (DEFENSE_SYSTEM, PROSECUTION_SYSTEM, DEFENDANT_PROMPT, PLAINTIFF_PROMPT, JUDGE_PROMPT)
from Agents.Lawyer_Agent import LawyerAgent
from Agents.Defendent_Agent import DefendantAgent
from Agents.Plantiff_Agent import PlaintiffAgent
from Agents.Judge_Agent import JudgeAgent
from Agents.EyeWitness_Agent import EyewitnessAgent

load_dotenv()
token = os.getenv("HF_API_TOKEN")
model = "microsoft/Phi-3-mini-4k-instruct"



# give case background and eye witness details
case_background = st.text_area(
    "Case Background",
    value="The State alleges that John Doe stole proprietary algorithms from his former employer and used them at a competitor. The charge is felony theft of trade secrets. No physical evidence shows direct copying, but server logs indicate large downloads two days before Doe resigned."
)
eyewitness_details = st.text_area(
    "Eyewitness Details (optional)",
    value="I noticed unusual activity on the server two days before John Doe resigned. His account accessed and downloaded several proprietary algorithm files. He wasn't authorized to work with those files at that time. I reported the incident to my supervisor immediately."
)

if st.button("Run Trial"):
    # Initialize agents
    defense = LawyerAgent("Defense", DEFENSE_SYSTEM)
    prosecution = LawyerAgent("Prosecution", PROSECUTION_SYSTEM)
    defendant = DefendantAgent(model=model, token=token, system_prompt=DEFENDANT_PROMPT)
    plaintiff = PlaintiffAgent(model=model, token=token, system_prompt=PLAINTIFF_PROMPT)
    judge = JudgeAgent(model=model, token=token, system_prompt=JUDGE_PROMPT)
    st.subheader("Opening Statements")
    st.markdown(f"**Prosecution:** {prosecution.respond(f'Opening statement:{case_background}')}")
    st.markdown(f"**Defense:** {defense.respond('Opening statement responding to prosecution')}")

    st.subheader("Plaintiff Testimony")
    st.markdown(f"**Plaintiff:** {plaintiff.statement()}")
    if eyewitness_details.strip():
        eyewitness = EyewitnessAgent("Witness", eyewitness_details, model, token)
        st.subheader("Eyewitness Testimony")
        st.markdown(f"**Eyewitness:** {eyewitness.testify()}")

    st.subheader("Defendant Testimony")
    st.markdown(f"**Defendant:** {defendant.testify('Explain your side of the case')}")

    st.subheader("Closing Statements")
    st.markdown(f"**Prosecution:** {prosecution.respond('Final closing argument')}")
    st.markdown(f"**Defense:** {defense.respond('Final closing argument')}")

    st.subheader("Judge's Verdict")
    st.markdown(f"**Judge:** {judge.verdict()}")

st.info("Edit the case background or eyewitness details and click 'Run Trial' to simulate a new scenario.")

