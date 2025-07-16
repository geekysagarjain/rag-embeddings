Vector Databases for RAG with Pinecone

This repository documents my hands-on journey into Vector Databases and their role in Retrieval-Augmented Generation (RAG) using Pinecone. It includes experiments, code samples, and notes on embedding generation, similarity search, and integrating with LLMs for enhanced context-aware responses.
Ideal for anyone exploring how to combine semantic search with LLMs in real-world applications.

✅ Key Steps of RAG Ingestion in LangChain ->
📂 Load Data (Document Loader)->
✂️ Split Text (Text Splitter)
🔢 Generate Embeddings (Embedding Model)->
💾 Store Vectors (Vector Store)

<img width="1777" height="670" alt="image" src="https://github.com/user-attachments/assets/1346d72f-861e-4643-8813-3678722a2906" />

| Step | Task                  | Tools                                       |
| ---- | --------------------- | ------------------------------------------- |
| 1    | Load documents        | `PyPDFLoader`, `TextLoader`, etc.           |
| 2    | Split text            | `RecursiveCharacterTextSplitter`            |
| 3    | Embed text            | `OpenAIEmbeddings`, `HuggingFaceEmbeddings` |
| 4    | Store vectors         | `FAISS`, `Chroma`, `Pinecone`, etc.         |
| 5    | Save store (optional) | `save_local()`, cloud save                  |


