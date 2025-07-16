import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

if __name__=="__main__":

    print("\n Starting the Ingetion...\n")

    loader=TextLoader(r"C:\Users\user\Documents\ai\langchain_vector_dbs\medium_blog_1.txt", encoding='utf-8')
    document=loader.load()
    
    print("spliting...\n")

    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    texts=text_splitter.split_documents(document)

    print(f"created {len (texts)} chunks\n")

    embeddings=OpenAIEmbeddings(openai_api_type=os.environ.get("OPEN_API_KEY"))

    print("Ingeting in Pinecone\n")

    PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ['INDEX_NAME'])
    
    print("finish")
    
