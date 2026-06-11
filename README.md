# eInvestigator

## Overview

eInvestigator is an AI-powered legal investigation and analysis system designed to assist with legal research, constitutional interpretation, and criminal law analysis. The project combines **Retrieval-Augmented Generation (RAG)**, **vector search**, **semantic embeddings**, and **large language models (LLMs)** to provide context-aware legal responses.

The solution focuses on Nigerian legal and constitutional domains and is capable of analyzing user queries, extracting key legal concepts, retrieving relevant information from a vector knowledge base, and generating detailed responses grounded in retrieved evidence.

---

## Key Features

- **Legal Question Analysis**
  - Identifies and extracts key legal concepts and keywords from user queries.

- **Retrieval-Augmented Generation (RAG)**
  - Retrieves relevant legal information from a vector database before generating answers.

- **Semantic Search**
  - Uses transformer-based embeddings for high-quality semantic matching.

- **AI-Powered Legal Reasoning**
  - Leverages Google's Gemini model to generate contextualized legal insights.

- **Vector Database Integration**
  - Uses Pinecone for efficient storage and retrieval of legal knowledge embeddings.

- **Observability & Monitoring**
  - Integrates Traceloop workflows for monitoring and tracing AI operations.

---

## Architecture

```text
User Query
     |
     v
Keyword & Context Extraction (Gemini)
     |
     v
Text Embedding Generation
(Sentence Transformers)
     |
     v
Pinecone Vector Search
     |
     v
Relevant Legal Context Retrieval
     |
     v
Gemini Response Generation
     |
     v
Final Legal Analysis
```

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| LLM | Google Gemini 1.5 Flash |
| Vector Database | Pinecone |
| Embedding Model | mixedbread-ai/mxbai-embed-large-v1 |
| AI Observability | Traceloop |
| Programming Language | Python |
| RAG Framework | Custom Retrieval Pipeline |

---

## Core Workflow

### 1. Query Processing
The system receives a legal question and extracts relevant concepts, entities, and keywords.

### 2. Embedding Generation
The query is transformed into vector embeddings using a sentence transformer model.

### 3. Knowledge Retrieval
Embeddings are used to search a Pinecone index containing legal knowledge and reference materials.

### 4. Contextual Answer Generation
Retrieved context is combined with the original query and supplied to Gemini to generate a comprehensive response.

---

## Project Structure

```text
eInvestigator.ipynb
│
├── Model Initialization
├── Traceloop Workflow Configuration
├── Embedding Generation
├── Pinecone Vector Retrieval
├── Input Processing
└── Legal Analysis & Response Generation
```

---

## Use Cases

- Legal research assistance
- Constitutional interpretation
- Criminal law analysis
- Case investigation support
- Legal knowledge retrieval
- AI-assisted legal advisory systems

---

## Installation

```bash
git clone <repository-url>
cd eInvestigator
```

Install dependencies:

```bash
pip install google-generativeai
pip install pinecone
pip install sentence-transformers
pip install traceloop-sdk
```

---

## Configuration

Configure the following services before running the notebook:

- Google Gemini API
- Pinecone Account and Index
- Traceloop Account

Store all credentials securely using environment variables rather than hardcoding them in source code.

Example:

```bash
export GEMINI_API_KEY=your_key
export PINECONE_API_KEY=your_key
export TRACELOOP_API_KEY=your_key
```

---

## Running the Project

Launch the notebook:

```bash
python main.py
```

Execute the workflow cells sequentially to:

1. Initialize services.
2. Process legal questions.
3. Generate embeddings.
4. Retrieve legal context.
5. Produce AI-generated legal analysis.

---

## Future Enhancements

- Multi-modal support for images and audio evidence.
- Citation-based legal references.
- Court case summarization.
- Legal document ingestion pipeline.
- Advanced legal reasoning agents.
- Support for additional jurisdictions beyond Nigeria.

---

## Security Recommendations

- Remove hardcoded API keys from source code.
- Use secrets management solutions.
- Enable authentication and authorization.
- Encrypt sensitive legal data.
- Maintain audit logs for investigations.

---

## Disclaimer

This project is intended for legal research and investigative assistance purposes only. Generated outputs should not be considered formal legal advice and must be reviewed by qualified legal professionals before use in legal proceedings.

---

## License

Specify an appropriate open-source or proprietary license before production deployment.
