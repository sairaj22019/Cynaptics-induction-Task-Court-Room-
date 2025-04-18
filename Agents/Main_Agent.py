from __future__ import annotations
import os
from dotenv import load_dotenv
from huggingface_hub import login
from typing import List, Dict
from huggingface_hub import InferenceClient

load_dotenv() 
token = os.getenv("HF_API_TOKEN")
login(token=token)
model="microsoft/Phi-3-mini-4k-instruct"

class MainAgent:
    def __init__(self, name: str, system_prompt: str, model: str, token: str):
        self.name = name
        self.system_prompt = system_prompt.strip()
        self.history: List[Dict[str, str]] = []
        self.client = InferenceClient(model, token=token)

    def _format_prompt(self, user_msg: str) -> str:
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.history)
        messages.append({"role": "user", "content": user_msg})
        prompt = ""
        for m in messages:
            prompt += f"<|{m['role']}|>\n{m['content']}\n"
        prompt += "<|assistant|>\n"
        return prompt

    def respond(self, user_msg: str, **gen_kwargs) -> str:
        prompt = self._format_prompt(user_msg)
        completion = self.client.text_generation(
            prompt,
            max_new_tokens=512,
            temperature=0.7,
            do_sample=True,
            stream=False,
            **gen_kwargs
        )
        answer = completion.strip()
        self.history.append({"role": "user", "content": user_msg})
        self.history.append({"role": "assistant", "content": answer})
        return answer
    

