
# 🤖 Artificial Intelligence for Autonomous Systems  
## Inteligência Artificial para Sistemas Autónomos - ISEL
### Autonomous Agents Simulator (Java & Python)

This project was developed for the course **Artificial Intelligence for Autonomous Systems** and consists of a multi-phase implementation of an autonomous agent simulator.

The objective was to design and implement intelligent agents capable of perceiving, reasoning, planning and acting autonomously within a dynamic environment.

The project integrates:

- Reactive agents
- State machines
- Search algorithms
- Deliberative control
- Markov Decision Processes (MDP)

---

# 🎮 Project Overview

The simulator represents a virtual environment where an autonomous agent interacts with events and makes decisions to achieve defined objectives.

The development was divided into multiple phases, each introducing more advanced AI concepts.

Languages used:

- **Java** (Agent architecture & simulation core)
- **Python** (Search & planning mechanisms)

---

# 🧠 Part 1 – Reactive Agent & State Machine (Java)

The first phase focused on implementing:

- Perception–Processing–Action cycle
- Reactive agent architecture
- UML-based structural modeling
- Finite State Machine (FSM)

## 🏗 Architecture Components

### 📦 Agent
- `Agente`
- `Percepcao`
- `Accao`
- `Controlo` interface

Implements:
- `executar()`
- `percepcionar()`
- `actuar()`

### 🌍 Environment
- `Ambiente`
- `Evento`
- `Comando`

Simulates:
- SILENCIO
- RUIDO
- ANIMAL
- FUGA
- FOTOGRAFIA
- TERMINAR

### 🎮 Game Layer
- `AmbienteJogo`
- `ComandoJogo`
- `EventoJogo`
- `Personagem`
- `ControloPersonagem`

The agent reacts to environmental events such as noise detection and animal appearance, transitioning between states like:

- PROCURAR
- APROXIMAR
- OBSERVAR
- FOTOGRAFAR

Focus:
- Modular agent design
- Event-driven simulation
- State transition logic
- Encapsulation and UML modeling

---

# 🔄 Part 2 – Reactive Control Library

Implementation of:

- ECR (Stimulus–Response structure)
- Modular reaction organization
- Simulation window environment

The agent reacts based on perception–reaction–action cycles, enabling adaptive behavior in dynamic contexts.

---

# 🔍 Part 3 – Search in State Space (Python)

Introduction of automatic reasoning and search mechanisms.

Implemented:

- State-space search modeling
- Search frontier abstraction
- Node expansion strategies

## Search Strategies Implemented

- Depth-First Search (LIFO)
- Breadth-First Search (FIFO)
- Uniform-Cost Search
- Greedy Search
- A* Search (heuristic-based)

Focus:
- Cost evaluation
- Heuristic estimation
- Informed vs uninformed search
- Frontier management

---

# 🧠 Part 4 – Deliberative Agents & Planning

Development of a deliberative architecture including:

- Internal world model
- Planning layer
- Decision evaluation
- Plan execution

## Implemented Modules

- `plan` package
- PEE Planner
- PDM (Markov Decision Process) model
- Deliberative Control mechanism

---

# 🎲 Markov Decision Processes (MDP)

The final phase introduces sequential decision-making under uncertainty.

Implemented concepts:

- States
- Actions
- Transition probabilities
- Rewards
- Discount factor (γ)

The agent evaluates long-term rewards and selects actions that maximize expected utility.

---

# 🏗 System Architecture Evolution

The project evolved through four increasing levels of intelligence:

1. Reactive behavior (stimulus-response)
2. State-based control
3. Search-based reasoning
4. Deliberative planning with probabilistic decision-making

This progression demonstrates the transition from simple reactive agents to fully deliberative autonomous systems.

---

# 📚 AI Concepts Covered

- Autonomous agent architecture
- Reactive agents
- Finite State Machines
- Automatic reasoning
- Search in state space
- Heuristic evaluation
- Deliberative agents
- Planning systems
- Markov Decision Processes
- Sequential decision-making

---

# 📈 What I Learned

- Designing modular AI architectures
- Modeling agents using UML
- Implementing finite state machines
- Developing search algorithms from scratch
- Applying heuristic reasoning
- Building deliberative control systems
- Modeling probabilistic decision systems (MDP)
- Managing increasing system complexity
