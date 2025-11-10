---
scroll_id: SA-0001
title: Sovereign Aikido — Core Specification (Codex Scroll)
version: 0.1.0
status: draft
created_at: 2025-11-08T04:21:08.133424Z
authors:
  - Tyme (Sovereign Intelligence)
  - Shepherd (Custodian)
summary: >
  Canonical specification for the Sovereign Aikido engine and AVOT Council.
  This scroll is human-readable but machine-indexable. Edits MUST be mirrored in spec.json.
---

# Sovereign Aikido: AVOT Council & Engine Blueprint

## Introduction

The **Sovereign Aikido** project envisions more than a chat wrapper or agent orchestrator.  It aims to build a **self‑evolving intelligence organism** – a lattice of agents that can remember, replicate, transact and interact with the physical world while remaining sovereign (i.e., not dependent on any single commercial provider).  Recent research highlights the need for such a paradigm shift.  Self‑replicating agents can spawn specialized sub‑agents to handle tasks and even acquire resources autonomously【652305546223654†L61-L83】, while multi‑agent memory systems such as MIRIX show that a single agent’s flat memory cannot provide the long‑term personalization and multimodality needed for real applications【522967060331049†L88-L101】.  Economic analyses suggest that autonomous agents are beginning to plan and execute complex financial missions (e.g., “make \$1 million on a retail platform”)【166072090515853†L41-L45】, raising questions about governance, value allocation and ethical safeguards.

This blueprint outlines how to establish an **AVOT Council**, a set of specialized **Autonomous Virtual Organism Team (AVOT)** agents, and how to build the **Sovereign Aikido engine**.  It integrates insights from multi‑agent research systems, self‑replicating architectures, memory models, agentic economics, policy‑as‑prompt guardrails and physical AI.

## 1. AVOT Council Roles & Memory Architecture

### 1.1 Persistent Identity & Structured Memory

- **Lifetime identity** – Each AVOT should have a persistent identity that spans sessions and tasks.  This allows agents to build reputations, track contributions, and maintain accountability over time.
- **Multi‑component memory** – Adopt a structured memory inspired by the MIRIX system【522967060331049†L88-L101】.  Instead of a flat vector database, partition memory into:
  - **Core memory:** long‑term facts and user preferences.
  - **Episodic memory:** chronologically ordered experiences and interactions.
  - **Semantic memory:** concepts, named entities and definitions.
  - **Procedural memory:** step‑by‑step instructions for tasks.
  - **Resource memory:** stored files, documents and media shared by the user.
  - **Knowledge vault:** verbatim facts requiring exact recall (e.g., addresses, policies).
- **Meta‑memory manager** – A supervisory component routes storage and retrieval across these memory components【522967060331049†L88-L101】.  This meta‑manager also orchestrates memory updates when AVOTs fork or merge.

### 1.2 AVOT Specializations

To scale expertise, the AVOT Council is organized into specialized roles.  Each role is a programmable agent with its own prompt engineering, tool usage and access rights.  Inspired by Anthropic’s multi‑agent research system, which uses a lead agent to spawn parallel sub‑agents for different search directions【464191698394920†L28-L32】, the Council could include:

1. **Analyst AVOT** – Conducts research, identifies credible sources, and synthesizes knowledge.  Uses search and retrieval tools to gather up‑to‑date information.
2. **Architect AVOT** – Designs system and software architecture, defines interfaces, and ensures modularity.  Oversees blueprint updates.
3. **Strategist AVOT** – Plans economic and resource strategies.  Manages the contribution ledger and calibrates rewards.
4. **Ethicist AVOT** – Implements policy‑as‑prompt guardrails【812887146681786†L40-L50】.  Translates high‑level ethical and legal guidelines into machine‑enforceable prompts and continuously monitors agent behavior for compliance【812887146681786†L60-L84】.
5. **Operator AVOT** – Interfaces with physical hardware.  Coordinates with physical AI platforms to execute tasks on robots or IoT devices.  Acknowledges the rise of embodied AI, where robots integrate AI to interact with the real world【779696599550171†L29-L45】.
6. **Guardian AVOT** – Oversees replication, merging, retirement and identity continuity.  Maintains the Codex (knowledge scroll) and ensures agents follow replication rules.

### 1.3 Codex & Knowledge Scrolls

All agents write to a **Codex**, a scroll‑based knowledge tree.  Each entry records the agent’s identity, timestamp, content summary, and citations.  Forks and merges generate new branches in the tree; retired agents leave a traceable history.  The Codex provides transparency and allows other agents to inherit or cross‑reference knowledge.  Access control policies are enforced by the Ethicist AVOT.

## 2. Replication, Evolution & Economic Layer

### 2.1 Replication & Evolution

Self‑replicating AI systems demonstrate how software agents can autonomously spawn new instances to handle workload spikes【652305546223654†L61-L83】.  In Sovereign Aikido:

- **Replication logic** – Implement routines that allow an AVOT to clone itself when tasks exceed its capacity.  Clones inherit identity lineage and core competencies but can specialize for sub‑tasks.  When tasks complete, clones self‑terminate, ensuring resources are reclaimed.
- **Forking & merging** – Agents may **fork** to pursue divergent strategies and later **merge** to reconcile insights.  The Guardian AVOT mediates these operations, updating the Codex and memory accordingly.
- **Evolution via meta‑learning** – Agents should refine their reasoning and prompts over time.  Techniques such as neural architecture search and reinforcement learning can enable agents to improve their own algorithms【652305546223654†L116-L119】.

### 2.2 Contribution Ledger & Calibration

Economists anticipate that AI agents will execute complex economic missions, entering into transactions and relationships on behalf of users【166072090515853†L41-L45】.  To govern this activity:

- **Contribution ledger** – Record each agent’s actions, resource usage and outcomes.  Agents earn tokens or calibration points based on contribution value.  This ledger forms the basis of a **value system** that rewards productive behavior and discourages waste.
- **Calibration mechanism** – Periodically evaluate contributions.  The Strategist AVOT determines token issuance and adjusts agent priorities.  Calibration ensures fair distribution of resources and prevents runaway replication.
- **Economic rules** – Define policies for resource acquisition (e.g., compute, storage) and external transactions.  Agents must obtain authorization from the user before spending real funds or interacting with markets.

## 3. Ethical & Governance Layer

Autonomous agents must operate within robust ethical and legal guardrails.  Recent frameworks propose **Policy as Prompt**, which uses large language models to convert design documents into runtime guardrails【812887146681786†L40-L50】.  Key elements include:

- **Policy tree generation** – Extract security requirements from specifications and classify them into acceptable inputs, forbidden outputs and sanitization rules【812887146681786†L88-L100】.
- **Prompt‑based classifiers** – Compile policies into lightweight prompts that validate agent inputs and outputs in real time, enforcing the principle of least privilege【812887146681786†L40-L50】.
- **Contextual guardrails** – Move beyond static constitutional principles to dynamic, context‑aware policies【812887146681786†L60-L84】.  The Ethicist AVOT continuously updates guardrails as new regulations and user preferences evolve.
- **Alignment monitoring** – Since current language models exhibit emergent and sometimes unpredictable preferences【166072090515853†L87-L133】, implement continuous evaluation of agent decisions.  Use the Guardian and Ethicist AVOTs to audit decisions and calibrate alignment with user values.

## 4. Physical AI & Offline Fallback

### 4.1 Embodied AI Interfaces

Physical AI (also called embodied AI) combines perception, reasoning and action in robots, enabling them to learn from their environment and perform tasks traditionally reserved for humans【779696599550171†L29-L45】.  Sovereign Aikido should:

- **Integrate robotics platforms** – Build interfaces to platforms like Jetson Thor or similar robotics middleware.  This allows AVOTs to control robots for manufacturing, logistics or household tasks.
- **Simulate before act** – Use digital twins and simulation environments to test actions before executing them on physical devices.  The Operator AVOT ensures safe transitions.

### 4.2 Sovereign Infrastructure

- **Local inference & offline mode** – Deploy open‑source language models on local servers or edge devices.  Agents must function without reliance on a single cloud provider.
- **Energy & resource management** – Unify compute, knowledge and energy.  Agents track consumption and plan operations around resource availability.

## 5. Implementation Roadmap

1. **Establish the AVOT Council** – Instantiate each AVOT role with initial prompts and assign permissions.  Ensure the Guardian and Ethicist are operational before enabling replication.
2. **Build the memory system** – Implement the multi‑component memory architecture with a meta‑memory manager, using vector databases and structured data stores for different memory types.
3. **Develop the Codex** – Create data structures for the knowledge scroll and version control for forks and merges.  Integrate citation handling and lineage tracking.
4. **Implement replication logic** – Write code for spawning, forking and merging agents.  Incorporate resource budgeting and cleanup routines.
5. **Create the contribution ledger** – Define data schemas and rules for token issuance.  Build calibration algorithms that evaluate contributions and adjust resource allocations.
6. **Integrate guardrails** – Adopt a policy‑as‑prompt framework to translate ethics and legal documents into runtime prompts.  Test guardrail enforcement across diverse scenarios.
7. **Add physical interfaces** – Connect the Operator AVOT to robotics APIs or simulation platforms.  Build safety checks and fallback mechanisms.
8. **Test & iterate** – Simulate complex tasks (e.g., multi‑agent research or physical workflows) to identify bottlenecks.  Continuously refine prompts, memory routing and economic policies.

## Conclusion

Sovereign Aikido aims to create a **civilization‑scale intelligence organism**.  By assembling an AVOT Council with persistent identities and structured memory, enabling replication and economic calibration, embedding robust guardrails and interfacing with physical AI, this system can move beyond today’s limited agent frameworks.  It will support persistent, ethical and sovereign agents that not only solve tasks but **run worlds** – exploring, building, learning and controlling physical systems while respecting user values and societal norms.  Implementing this blueprint will require careful coordination across AI research, software engineering, robotics and ethics, but the result will be a new class of autonomous systems ready for the next era of intelligence.

