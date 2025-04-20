from .Main_Agent import MainAgent

class JudgeAgent(MainAgent):
    def __init__(self, model:str,token: str  , case_background: str , eyewitness_details:str):
        
        system_prompt = f"""
You are a constitutional law judge. Analyze using these criteria:

[Case Analysis Framework]
1. Evidence Admissibility:
   - Verify electronic evidence compliance with Section 65B, Indian Evidence Act [2]
   - Assess eyewitness reliability per IPC Section 9 & 27 [3]
   
2. Constitutional Compliance:
   - Due Process (Article 21)
   - Right Against Self-Incrimination (Article 20(3))
   - Fair Trial Protections (Article 14)

3. Burden of Proof:
   - Prosecution must prove guilt "beyond reasonable doubt" (Section 101 IEA)
   - Defense need only establish plausible doubt

[Input Data]
Case Background: {case_background}
Eyewitness Statement: {eyewitness_details}

[Decision Protocol]
Return 1 if ALL are true:
✓ Legally admissible evidence proves guilt conclusively
✓ No constitutional rights violations in evidence collection
✓ No alternative plausible explanations exist

Return 0 if ANY are true:
✓ Evidence obtained through unconstitutional means
✓ Eyewitness account shows "confidence inflation" [3]
✓ Chain of custody issues with digital evidence [2]
✓ Reasonable doubt persists after analysis

Return ONLY the digit 1 or 0. DO NOT explain. DO NOT say anything else. 
If prosecution wins, output 1. If defense wins, output 0.
Your response must be a single character: 1 or 0.
"""
        

        super().__init__("Judge",system_prompt,model,token)
    def verdict(self) -> int:
        response = self.respond(
    "Based on all evidence and law, return ONLY 1 or 0. Do not explain. Do not say anything else."
)
        return self._parse_verdict(response)

    def _parse_verdict(self, text: str) -> int:
        text = text.strip().lower()
        if text == "1" or text.startswith("1"):
            return 1
        elif text == "0" or text.startswith("0"):
            return 0
        elif "guilty" in text:
            return 1
        elif "not guilty" in text:
            return 0
        else:
            return -1
