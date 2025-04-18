from .Main_Agent import MainAgent
class JudgeAgent(MainAgent):
    def __init__(self, model:str,token: str ,system_prompt: str):
        
        super().__init__("Judge",system_prompt,model,token)
    def verdict(self)->str:
        return self.respond("Deliver your verdict and explain your reasoning.")