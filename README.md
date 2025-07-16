Vector Databases for RAG with Pinecone

This repository documents my hands-on journey into Vector Databases and their role in Retrieval-Augmented Generation (RAG) using Pinecone. It includes experiments, code samples, and notes on embedding generation, similarity search, and integrating with LLMs for enhanced context-aware responses.
Ideal for anyone exploring how to combine semantic search with LLMs in real-world applications.

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




