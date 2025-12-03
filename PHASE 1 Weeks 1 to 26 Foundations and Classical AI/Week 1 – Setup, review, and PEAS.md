## Week 1 – Setup, review, and PEAS


- Reading: Skim Preface and re‑read Chapters 1–2 to solidify definitions (rational agent, PEAS, task environments).[aima.berkeley+1](https://aima.cs.berkeley.edu/contents.html)​

- Coding:

   - Finish VS Code + conda “aima” environment and confirm you can import `agents`, `search`, etc., from aima‑python.[github+1](https://github.com/hanzopgp/ModernApproachAIExercices)​

   - Run at least one aima‑python notebook or small script to verify everything works.[github](https://github.com/hanzopgp/ModernApproachAIExercices) (DONE, it’s working, i can run agent.ipynb)​

- Concepts to write in your notes: definitions of agent, agent function vs. program, PEAS for at least three systems (vacuum, taxi, recommendation system).[aima.berkeley+1](https://aima.cs.berkeley.edu/)​

- Mini‑project: Implement or clean up your **simple reflex vacuum agent** and environment with a performance measure and a short text summary.[aima.berkeley+1](https://aima.cs.berkeley.edu/contents.html)

​

[https://www.youtube.com/watch?v=wsz17HhAhKU](https://www.youtube.com/watch?v=wsz17HhAhKU)


The study plan for Week 1 focuses on establishing the foundational understanding of Artificial Intelligence (AI) paradigms, setting up essential programming tools, and mastering the crucial concept of describing an agent's operational environment using the **PEAS** framework.

This week aligns with the beginning of the **Foundations (AIMA I, II, III) & Python Mastery** phase of a comprehensive curriculum, specifically corresponding to the start of the "Introduction to AI Paradigms" module (Weeks 1–4).

---

## Detailed Study Plan for Week 1 – Setup, Review, and PEAS

### Theme: Introduction to AI Paradigms and Agent Environment Specification

The goal of Week 1 is to establish the conceptual framework of **rational agents** interacting with environments and to achieve mastery in fundamental programming and data handling techniques necessary for later implementation.

### 1\. Core Reading and Goals (Theoretical Foundation)

The theoretical foundation for this week is drawn from the initial sections of the curriculum, focusing on intelligent agents and defining AI.

| Component | Focus/AIMA Alignment | Key Concepts to Master | Source Reference | 
|---|---|---|---|
| **Reading** | **AIMA Part I: Introduction and Intelligent Agents** (AIMA Chapters 1 and 2) | Defining AI, the notion of an **agent**, agency, autonomy, and the essential characteristics of intelligent agents (reactivity, proactiveness, social ability). |  | 
| **Goal 1: Define AI** | Understand the different goals used to approach AI: concerned with thinking or behavior; modeling humans or achieving optimal results. AI is concerned mainly with **rational action**, where an ideal intelligent agent takes the best possible action in a situation. |  |  | 
| **Goal 2: Agent Design** | Grasp that the first step in designing an agent must always be to specify the **task environment as fully as possible**. Understand how agents can be categorized by architecture (e.g., simple reflex, model-based, goal-based, utility-based). |  |  | 
| **Goal 3: Master PEAS** | Be able to define the **PEAS** description elements for various task environments. |  |  | 

### 2\. Setup and Review (Programming and Data Handling)

This initial week requires an intensive review or refresher of foundational programming skills, specifically Python and data-related libraries, which forms the **Python Mastery** segment of Phase I. The expectation is that prerequisite material, including **Math, stats, and Python basics**, should ideally be completed before the first day of class.

| Component | Task Detail | Expected Outcome/Tools | Source Reference | 
|---|---|---|---|
| **Environment Setup** | Install required development environment (e.g., Python, Jupyter Notebooks). | A functional environment ready for coding exercises. |  | 
| **Programming Review** | Intensive Python refresher, focusing on core Python syntax, **file I/O**, and **error handling**. Review resources like Real Python or freeCodeCamp for core Python concepts. | Proficiency in Python essentials for script development. |  | 
| **Data Handling Review** | Review data handling techniques, particularly using **NumPy** for numerical computing and **Pandas DataFrames** for cleaning, transforming, and analyzing complex datasets. | Ability to harness NumPy arrays and Pandas DataFrames. |  | 
| **Algorithmic Review** | Review **Big-O notation** and the complexity of algorithms. | Understanding of practical versus theoretical efficiency. |  | 

### 3\. Core Coding / Exercises

The practical work focuses on conceptualizing problems through the lens of agent design and the **PEAS** framework.

1. **PEAS Formulation Exercise:** Formulate at least three different tasks as agent environments using the **PEAS** description.

   - *Example Task:* Analyze the **automated taxi driver** environment, detailing its Performance measure, Environment, Actuators, and Sensors.

   - *Performance Measure:* Should maximize profit, ensure a legal, safe, and comfortable trip.

   - *Environment:* Includes roads, other traffic, pedestrians, and the customer.

   - *Actuators:* The devices that enable action, such as the steering wheel, accelerator, brake, signal, and display.

   - *Sensors:* Used to perceive the environment, including cameras, sonar, GPS, speedometer, accelerometer, engine/fuel sensors, and passenger input (touchscreen or voice).

2. **Agent Characteristics Exercise:** Identify the key characteristics (reactivity, proactiveness, social ability, autonomy) required for several agents (e.g., a simple vacuum cleaner agent vs. a modern generative AI-powered travel agent).

### 4\. Reflection (Short Write-up)

Conclude the week with a reflective exercise to solidify the foundational concepts.

- **Reflection Topic:** In a short note (½–1 page), compare and contrast the different goals people approach AI with (thinking vs. behavior, human model vs. optimal results), and explain how the decision to use a **knowledge-based agent** differs from the reflex and search agents introduced in the early chapters. Specifically, reflect on the advantages and limitations of relying on an explicit **knowledge base** to guide decisions.

   - The **knowledge-based agent** uses a knowledge base (KB) consisting of sentences and differs from early search agents by its reliance on the **TELL** and **ASK** functions to manage knowledge and infer the state of the world. This symbolic reasoning is foundational for later work in agent design.