## Working offline
from pathlib import Path
from gpt4all import GPT4All
model = GPT4All(model_name='orca-mini-3b-gguf2-q4_0.gguf',
                model_path=(Path.home()/'.local'/'share'/'nomic.ai'/'GPT4All'),
                allow_download=False)
response = model.generate("The capital of France is ", temp=0)
print(response)

