# Creative Autonomous Agents, with Generative Language Models, for Real-World Organizational Tasks

This work is driven by the idea that our organisations will contain more helpful autonomous agents, that can free humans from repetitive work to work on not in the organisation, and will likely make create more business owners than workers. 

We're exploring an exciting application of generative language models, currently OpenAI's GPT-4, to create autonomous agents capable of memory retrieval, planning, and reflection. Our work is inspired by interacting with GPT-4, and further reading of the research paper [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/pdf/2304.03442.pdf), which introduces a framework for creating agents that can exhibit human-like behavior, as well as the paper Reflexions. Our implementation goes beyond the papers by applying the concepts in a practical context and adding the concept of ideals to the agents' memory. 

## Background
Generative language models, like GPT-4, have shown impressive performance in various natural language processing tasks. While they can generate coherent and contextually relevant text, their application as autonomous agents capable of interacting with the environment and other agents has not been extensively explored.

The research paper mentioned above presents a general architecture for creating generative agents that can interact with each other and users, exhibiting behaviors like memory retrieval, planning, and reflection based on memory and retrieval concepts such as recency, relevance, and importance. Our implementation is tailored to real-world organizational tasks and adds the concept of ideals to the agents' memory, making them more suitable for complex problem-solving scenarios.

## The Framework
Our implementation follows the framework outlined in the paper but adapts it to a real-world organizational context and includes the concept of ideals in the agents' memory. The framework consists of three main components: memory, retrieval, and reflection.

## Memory
Memory is an essential aspect of human cognition and is vital for the development of intelligent agents. The agents we're creating have a memory stream, which includes observations, plans, reflections, and ideals. Ideals represent the desired goals or outcomes for a given situation. These memory objects are stored in a tree-like structure, with leaf nodes representing base observations and non-leaf nodes representing higher-level, more abstract thoughts.

## Retrieval
Retrieval is the process of accessing stored memories based on the current context. In our implementation, memory retrieval is based on three key factors: recency, relevance, and importance. Recency is determined by a decay function, relevance is measured using cosine similarity between memory objects and the current context, and importance is determined by the agent's assessment of a memory's significance.

## Reflection
Reflection is a higher-level cognitive process that allows agents to generate insights based on their experiences. In the framework we've implemented, agents generate reflections periodically when the sum of the importance scores for the latest events perceived by the agents exceeds a certain threshold. Reflections can be based on both observations and other reflections, allowing agents to create trees of reflections that represent increasingly abstract thoughts higher up the tree.

## Implementation
We've implemented the framework using Python and created a simple API for users to interact with the agents. The application's file structure consists of multiple components, including autonomous agents with their own memory and planning capabilities, GPT instances, and conversation history between agents and users.

The agents in our implementation can communicate with each other and users, retrieve memories based on the current context, and generate reflections to create higher-level insights. By tailoring the agents to real-world organizational tasks and incorporating the concept of ideals, our implementation demonstrates the potential for these agents to perform complex problem-solving and decision-making processes in practical settings.

## Conclusion
Creating autonomous agents with generative language models is an exciting and promising area of research. By implementing the framework outlined in the research paper and adapting it to real-world organizational tasks, we've demonstrated how GPT-4 can be used to create agents capable of memory retrieval, planning, and reflection in a practical context. This work opens up the possibility for a wide range of applications, including virtual assistants, automated customer support, and even collaborative problem-solving within organizations.

Our implementation's inclusion of ideals in the agents' memory further expands their capability to consider desired goals and outcomes when making decisions and generating responses. This makes the agents more adaptable and suitable for tasks that require a deeper understanding of the context and the objectives at hand.

As the field of artificial intelligence and generative language models continues to advance, we can expect to see even more sophisticated and capable autonomous agents that can perform complex tasks and interact with users and other agents in a human-like manner. This will undoubtedly lead to new applications and opportunities for AI in various industries and domains.

We hope this blog post has provided you with a better understanding of the potential of generative language models like GPT-4 in creating autonomous agents for real-world organizational tasks. Our implementation serves as a starting point and inspiration for further exploration and development in this exciting area of AI research.
