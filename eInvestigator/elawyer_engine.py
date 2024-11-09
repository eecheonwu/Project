import os
import google.generativeai as genai
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

genai.configure(api_key="AIzaSyCth3JwTTQlK_zj3LbQCYnqaYOe0XNq1AE")
pc = Pinecone(api_key='0eda1969-7f57-4cc5-9ea4-e13073b52730')

# Initialize the Gemini model with system instructions
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""You are an expert in the Nigeria constitution and criminal code. You are responsible in 
                          understanding the context and theme of the topic and offers specialized and detailed 
                          analysis by processing the statements given either by text, image or audio.
                          """
)

embedder = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1", truncate_dim=1024)

index = pc.Index("legal-docs")
def retrieve_answer(query_vector, k=10):
    # Query the index
    results = index.query(vector=query_vector, top_k=k)
    # Extract the top k vectors and their scores
    top_vectors = [(result.id, result.score) for result in results.matches]
    return top_vectors

def embed_text(text):
    # Create embeddings for the prompt
    vectors = embedder.encode(text)
    # Extract the vector from the response (adjust based on ollama's output structure)
    return vectors.tolist()  # Return just the vector


def process_input(input_type, input_data):
    """Processes input data based on type (text, image, or audio) using Gemini."""
    if input_type == "text":
        prompt = f" Critical analyze the question and identify the key words in the following ststement: {input_data}"
        processed_text = model.generate_content(prompt)
        response = processed_text.candidates[0].content.parts[0].text
        return  response
    else:
        raise ValueError(f"Invalid input type: {input_type}")


def analyze_input(processed_input, input_data):
    """Analyzes processed inputs using RAG and llama and Gemini to generate question ideas as steps and give indepth answer."""
    # Find relevant documents from the knowledge base using EmbedChain.ai's RAG
    query_vectors = embed_text(input_data)
    retrieved_answer = retrieve_answer(query_vectors, k=10)
    prompt = f"from the keywords {processed_input} and retrieved answer {retrieve_answer}, generate answer to the question: {input_data} using suitable provided sources to reference, if possible."
    processed_answer = model.generate_content(prompt)
    relevant_documents = processed_answer.candidates[0].content.parts[0].text
    return relevant_documents


