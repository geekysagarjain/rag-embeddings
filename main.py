import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore

from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


load_dotenv()


if __name__ == "__main__":
    print("Retrieving The Data...\n")

    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()

    query = "what is Pinecone in machine learning?" #defining the question to retrive data from db
    # chain = PromptTemplate.from_template(template=query) | llm #created a simple prompt and paased out wuestion

    vectorstore = PineconeVectorStore(
        index_name=os.environ["INDEX_NAME"], embedding=embeddings #getting the data from pinecone db which we save through ingetion.py
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat") #using the opensource prompt 
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt) #stuffing together the openAI llm and prompt
    retrival_chain = create_retrieval_chain(
        retriever=vectorstore.as_retriever(), combine_docs_chain=combine_docs_chain #retriving data from vectorstore
    )

    result = retrival_chain.invoke(input={"input": query}) #passing the question and invoking the same

    print(result['answer'])
