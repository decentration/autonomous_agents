import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from agents.Memory.memory import Memory
from agents.Thought.thought import Reflection
from agents.embedding import get_embedding
import openai
import os

from dotenv import load_dotenv


# Load .env file
load_dotenv()

# Get API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_organization = os.getenv("OPENAI_ORGANIZATION")


def decay_function(time_elapsed):
    decay_rate = 0.5
    return np.exp(-time_elapsed * decay_rate)

def calculate_relevance(memory, query_memory):
    memory_vector = memory.embedding
    query_memory_vector = query_memory.embedding
    return cosine_similarity(memory_vector, query_memory_vector)

def calculate_importance(memory):
    return memory.importance

def calculate_recency(memory, current_time):
    memory_time = memory.timestamp
    time_elapsed = current_time - memory_time
    return decay_function(time_elapsed)

# def retrieve_memory(memory_stream, query_memory, current_time):
#     scores = []
#     for memory in memory_stream.memories:
#         recency = calculate_recency(memory, current_time)
#         relevance = calculate_relevance(memory, query_memory)
#         importance = calculate_importance(memory)

#         score = recency + relevance + importance
#         scores.append((memory, score))

#     sorted_memories = sorted(scores, key=lambda x: x[1], reverse=True)
#     return [memory for memory, score in sorted_memories[:5]]

def calculate_importance_sum(memory_stream, n_latest_events):
    return sum(mem.importance for mem in memory_stream[-n_latest_events:])

def query_language_model(memories):
    # openai.api_key = "your_openai_api_key"

    # Combine the memory contents into a single string
    memory_texts = [memory.content for memory in memories]
    memory_input = "\n".join(memory_texts)

    # Construct the prompt for the language model
    prompt = f"Reflect on the following memories:\n{memory_input}\n\nReflection: "

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
    )

    reflection_content = response.choices[0].text.strip()
    evidence_indices = []  # You can modify this to include evidence indices if necessary

    return reflection_content, evidence_indices

def generate_sample_reflection(memory_stream):
    reflection_content, evidence_indices = query_language_model(memory_stream[-100:])
    
    reflection = Memory.Reflection(
        content=reflection_content,
        timestamp='2023-04-10 12:00:00',
        importance=6,
        evidence=evidence_indices
    )
    
    return reflection

def print_memory_item(memory, retrieved=False):
    importance_color = ConsoleColor.YELLOW
    if memory.importance >= 8:
        importance_color = ConsoleColor.GREEN
    elif memory.importance >= 5:
        importance_color = ConsoleColor.MAGENTA

    evidence_text = ""
    if isinstance(memory, Reflection):
        evidence_summary = [f"{e.id} ({e.content[:50]}...)" for e in memory.evidence]
        evidence_text = f"Evidence: {', '.join(evidence_summary)}"

    importance_str = f"{importance_color}importance: {memory.importance}{ConsoleColor.RESET}"

    memory_line = f"{memory.symbol} {memory.number} | {memory.timestamp}  | {importance_str} | {memory.content} | {memory.type} | {evidence_text}"
    print(memory_line)

    if retrieved and hasattr(memory, 'normalized_recency'):
        norm_values_line = f"Normalized retrieval values: norm_recency: {memory.normalized_recency}, norm_relevance: {memory.normalized_relevance}, norm_importance: {memory.normalized_importance}"
        print(norm_values_line)
    

class ConsoleColor:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
# # Add a new memory item (e.g., observation, plan, or ideal) to the memory_stream
# new_memory_item = Observation(content='Klaus Mueller is discussing his research with a colleague', timestamp='2023-04-10 12:30:00', importance=6)
# memory_stream.add_memory(new_memory_item)

# # Calculate the sum of importance scores for the latest events
# importance_sum = calculate_importance_sum(memory_stream.memories, 5)

# # If the importance sum exceeds the threshold, generate a reflection and add it to the memory stream and tree
# if importance_sum >= importance_threshold:
#     reflection = generate_reflection(memory_stream.memories)
#     memory_stream.add_memory(reflection)
    
#     reflection_node = TreeNode(reflection)
#     for evidence_idx in reflection.evidence:
#         memory_tree.children[evidence_idx].add_child(reflection_node)
