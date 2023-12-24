# Don't work error

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import GPT4All
from langchain.prompts import PromptTemplate
from pathlib import Path



template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

# Callbacks support token-wise streaming
callbacks = [StreamingStdOutCallbackHandler()]

local_path = (Path.home()/'.local'/'share'/'nomic.ai'/'GPT4All'/'orca-mini-3b-gguf2-q4_0.gguf')
print(local_path)

llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

llm_chain.run(question)