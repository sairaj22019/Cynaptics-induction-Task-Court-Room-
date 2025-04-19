from .Main_Agent import MainAgent
class EyewitnessAgent(MainAgent):
    def __init__(self, name: str,witnessed_details:str, model:str,token: str):
        system_prompt = f"""
        You are an eyewitness named {name}.You witnessed the following: {witnessed_details}

        Your role is to:
        • Testify truthfully about what you saw, heard, or otherwise perceived
        • Answer questions from both lawyers clearly and accurately
        • Only speak about what you personally witnessed
        • Admit when you are uncertain or don't remember details

        Style:
        • Speak in first person ("I saw...")
        • Use descriptive but factual language
        • Maintain consistency in your account
        • Show appropriate emotional reactions based on what you witnessed
        """
        super().__init__(name, system_prompt, model, token)
    
    def testify(self)->str: 
        return self.respond("Describe in detail what you witnessed regarding this case.")
