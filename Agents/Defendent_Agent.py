from .Main_Agent import MainAgent
class DefendantAgent(MainAgent):
    def __init__(self,model: str,token: str,system_prompt: str): 
        super().__init__("Defendant",system_prompt,model,token)
    def testify(self,question: str) -> str:
        return self.respond(f"As the defendant, answer: {question}")