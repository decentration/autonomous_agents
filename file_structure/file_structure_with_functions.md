autonomous_agents/
│
├─ agents/
│   ├─ autonomous_agent.py (contains the AutonomousAgent class)
│   │   ├─ get_instance_data(instance_id)
│   │   ├─ get_conversation_history(instance_id)
│   │   ├─ process_message(message_data)
│   │   ├─ update_memory(memory_data)
│   │   └─ communicate(message_data)
│   ├─ memory_stream.py (contains the MemoryStream class)
│   │   ├─ add_memory(memory_data)
│   │   ├─ get_memory_by_id(memory_id)
│   │   └─ search_memory(query, current_time)
│   └─ utils.py (contains utility functions for memory retrieval, etc.)
│       ├─ decay_function(time_elapsed)
│       ├─ cosine_similarity(vector1, vector2)
│       ├─ calculate_relevance(memory, query_memory)
│       ├─ calculate_importance(memory)
│       ├─ calculate_recency(memory, current_time)
│       └─ retrieve_memory(memory_stream, query_memory, current_time)
│
├─ instances/
│   ├─ gpt_instances.py (contains the GPT instances, their ID, name, and system_message)
│   └─ conversation_history.py (contains the conversation history between agents and users)
│
├─ endpoints/
│   ├─ api.py (contains the API endpoints for your application)
│   └─ server.py (contains the server configuration and setup)
│
└─ main.py (main entry point for your application, initializes agents, etc.)
