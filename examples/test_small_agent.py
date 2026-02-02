import os
import json
from smolagents import (
    CodeAgent,
    VLLMServerModel,
    WikipediaRetrieverTool
)

# Setup the VLLM local model
model = VLLMServerModel(
    model_id="Qwen/Qwen2.5-1.5B-Instruct",
    api_base=os.getenv("VLLM_API_BASE", "http://127.0.0.1:8000/v1"),
    api_key=os.getenv("VLLM_API_KEY", "token-abc"),
    lora_name="finetune",
    max_tokens=1024,
    n=4, temperature=0.4 # for SAG
)

# Agent setting
agent = CodeAgent(
    tools=[
        WikipediaRetrieverTool(),
    ],
    additional_authorized_imports=["numpy", "sympy"],
    model=model,
    verbosity_level=2,
    max_steps=5
)

# Run
result = agent.run(
    "How many times taller is the Empire State Building than the Eiffel Tower?",
    use_short_system_message=True
)