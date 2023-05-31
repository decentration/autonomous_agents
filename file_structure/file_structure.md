autonomous_agents/
│
├─ agents/
│   ├─ autonomous_agent.py (contains the AutonomousAgent class)
│   ├─ memory_stream.py (contains the MemoryStream class)
│   └─ utils.py (contains utility functions for memory retrieval, etc.)
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
