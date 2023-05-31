
# Autonomous Agents

AI Agents which form into teams and organisations and behave autonomously (human-out-the-loop). This application enables the interaction of autonomous agents using generative language models (LLMs). An agent includes, an LLM/GPT instance with: dynamic memory retrieval; group planning and schedulin;  and reflection, which weights recency, relevance, and importance. Stored in trees and in a vector database. 

## Table of Contents

<ul>
 <li><a href="#Features">Features</a> </li>
 <li><a href="#Installation">Installation</a> </li>
 <li><a href="#Usage">Usage</a> </li>
 <li><a href="#File Structure">File Structure</a> </li>
 <li><a href="#Contributing">Contributing</a> </li>
 <li><a href="#License">License</a> </li>
</ul>

## Features

- Multiple GPT instances acting as autonomous agents with their own memory and planning capabilities
- Memory retrieval based on recency, relevance, and importance
- Reflection mechanism that generates higher-level insights based on agents' experiences
- Communication between agents and users via a simple API
- Easy to extend and modify the behavior of agents

## Installation

1. Clone the repository:

```bash
git clone https://github.com/subchorus/autonomous_agents.git
```

2. Change directory to the project folder:

```bash
cd autonomous_agents
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the main application:
```bash
python main.py (currently not functioning, just go into tests folder and run tests)
```

2. Run tests:

Test Agents in a DAO functionality:
```bash
python3 autonomous_agents/agents/tests/test_dao.py
```
## File Structure

```markdown
autonomous_agents/
│
├─ agents/
│   ├─ autonomous_agent.py (AutonomousAgent class)
│   └─ agent_behaviour.py (agent related functions)
│   ├─ memory_stream.py (MemoryStream class)
│   └─ utils.py (utility functions)
│   └─ reflection_tree.py (ReflectionTree class)
│   └─ embedding.py (for relevance function)
│
├─ instances/
│   ├─ gpt_instances.py (GPT instances)
│   └─ conversation_history.py (conversation history)
│
├─ endpoints/
│   ├─ api.py (API endpoints)
│   └─ server.py (server configuration)
│
└─ main.py (main entry point)
```

## Contributing

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes following the coding style used in the project.
4. Write tests for your changes.
5. Update the documentation if necessary.
6. Submit a pull request with a description of your changes.

## License
This project is licensed under the MIT License.