from flask import Flask, render_template, request
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

app=Flask(__name__)
template="""Question: {question}
Answer: Let's think by step"""

promp=PromptTemplate(template=template, input_variables=["question"])

repo_id="google/flan-t5-xxl"
llm=HuggingFaceHub(repo_id=repo_id,
                   model_kwargs={"temperature":0.5,"max_length":120})

llm_chain=LLMChain(prompt=promp,llm=llm)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_input=request.form['user_input']
    response=llm_chain.run(user_input)
    return response

if __name__=='__main__':
    app.run(debug=True)







