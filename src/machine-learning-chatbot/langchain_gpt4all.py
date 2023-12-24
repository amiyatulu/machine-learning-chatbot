# Works offline
from langchain.llms import GPT4All
from langchain.chains import LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from pathlib import Path



template = """
Let's think step by step of the question: {question}
"""

prompt = PromptTemplate(template=template, input_variables=["question"])

callbacks = [StreamingStdOutCallbackHandler()]


llm = GPT4All(
    streaming=True,
    model="model/orca-mini-3b-gguf2-q4_0.gguf",
    verbose=True,
    callbacks=callbacks,
)

llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
llm_chain.run(question)