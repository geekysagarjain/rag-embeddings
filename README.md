

📦 Vector Databases for RAG with Pinecone: Ingestion & Retrieval

This repository demonstrates how to build a Retrieval-Augmented Generation (RAG) pipeline using vector databases with a focus on Pinecone. It covers end-to-end steps including document loading, chunking, embedding generation, vector storage, and retrieval for LLM-powered applications.

🔧 Features:

Document ingestion from various sources (PDF, text, web)

Text chunking with LangChain splitters

Embedding with OpenAI or HuggingFace

Vector storage and similarity search with Pinecone

Retrieval and integration with LLMs for RAG workflows

🧠 Ideal for: Developers building scalable, production-grade RAG systems using vector databases.

<img width="1777" height="670" alt="image" src="https://github.com/user-attachments/assets/1346d72f-861e-4643-8813-3678722a2906" />

<img width="1154" height="588" alt="image" src="https://github.com/user-attachments/assets/1d385646-a3f6-47c7-a1c7-78afd9107719" />


| **Step** | **Task**                       | **Tools**                                                                       |
| -------- | ------------------------------ | ------------------------------------------------------------------------------- |
| 1        | Load documents                 | `PyPDFLoader`, `TextLoader`, `WebBaseLoader`, `NotionLoader`, etc.              |
| 2        | Split text                     | `RecursiveCharacterTextSplitter`, `CharacterTextSplitter`                       |
| 3        | Embed text                     | `OpenAIEmbeddings`, `HuggingFaceEmbeddings`, `CohereEmbeddings`, etc.           |
| 4        | Store vectors                  | `FAISS`, `Chroma`, `Pinecone`, `Weaviate`, `Milvus`, `Elasticsearch`            |
| 5        | Save store (optional)          | `save_local()`, `persist()`, cloud-specific save methods                        |
| 6        | Retrieve relevant chunks       | `VectorStoreRetriever`, `MultiQueryRetriever`, `ContextualCompressionRetriever` |
| 7        | Generate answer with LLM       | `OpenAI`, `Anthropic`, `HuggingFace` (via LLM chains)                           |
| 8        | (Optional) Filter/Rank results | Metadata filters, similarity scores, `MaxMarginalRelevanceRetriever`            |




