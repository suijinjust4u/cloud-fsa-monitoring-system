import ollama

# Use Client to connect to specific Ollama host/port:
from ollama import Client

ollama_client = Client(host='http://localhost:11434')

def ask_ollama_with_data(question, data, model='mistral:7b'):
    """
    Sends live system node data and user question to Ollama's Mistral 7B model,
    to get a data-grounded AI response.
    """
    # Format node info lines for prompt
    nodes_info = []
    for node in data['nodes']:
        nid = node['node_id']
        state = data["states"].get(nid, "Unknown")
        value = node["value"]
        nodes_info.append(f"{nid}: {state}, {value} kW power (timestamp: {node['timestamp']})")
    node_summary = "\n".join(nodes_info)

    system_prompt = (
        "You are a monitoring assistant for a distributed renewable energy network.\n"
        "Here is the most recent data for all nodes:\n"
        f"{node_summary}\n"
        "Answer user questions ONLY by referring to this real data and the states. "
        "Do NOT hallucinate or invent any data."
    )

    response = ollama.chat(
        model=model,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': question},
        ],
    )
    return response['message']['content']
