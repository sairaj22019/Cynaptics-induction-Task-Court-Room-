from .Main_Agent import MainAgent
class PlaintiffAgent(MainAgent):
    def __init__(self, model: str,token: str,system_prompt:str):
        super().__init__("Plaintiff",system_prompt,model,token)
    def statement(self) -> str:
        return self.respond("State your grievance and what you want from the court.")