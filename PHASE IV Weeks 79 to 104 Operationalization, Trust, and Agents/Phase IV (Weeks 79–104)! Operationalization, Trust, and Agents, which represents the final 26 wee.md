# **Phase IV (Weeks 79–104): Operationalization, Trust, and Agents**, which represents the final 26 weeks of the curriculum. This phase is dedicated to deploying, governing, and integrating sophisticated AI systems, focusing heavily on Trustworthy AI (TAI), specialized GenAI Operations (GenAI-Ops), and the ultimate **Capstone Project**.

This phase operationalizes the theoretical core established in Phase I (Foundations) and the specialization achieved in Phase III (Generative AI Engineering) by synthesizing them into production-ready, verifiable agentic systems.

### Phase IV: Weeks 79–104 – Operationalization, Trust, and Agents

| Structural Element | Details | Sources | 
|---|---|---|
| **Weeks Covered** | 79–104 |  | 
| **AIMA Coverage** | Focuses on AIMA Part VII (Ethics, Safety, and Trustworthy AI Systems). |  | 
| **Primary Focus** | Operationalization, Governance, and Capstone (GenAI-Ops and TAI). |  | 
| **Theory/Practice Ratio** | Approximately **20% Theory / 80% Practice**. |  | 
| **Key Deliverable/Milestone** | **Capstone Project** integrating TAI/Neuro-Symbolic Elements. |  | 

---

### Phase IV Modular Breakdown (Weeks 79–104)

Phase IV is structured into three critical modules focused on implementation, governance, and final project synthesis.

#### Module 1: GenAI Operations (GenAI-Ops) and Multi-Agent Deployment (Weeks 79–86)

This module focuses on extending traditional MLOps to handle the unique challenges of large language models (LLMs) and deploying complex multi-agent systems.

| Week Range | Bootcamp Module Title | Core Focus Areas | Detailed Topics and Goals | Sources | 
|---|---|---|---|---|
| **Weeks 79–80** | **LLM/Agentic Workflow Integration** | **Multi-Agent Orchestration & Tool Use** | Design the **NLP front-end**, focusing on how user text transforms into structured goals, constraints, or queries. Implement multi-agent systems using frameworks like **CrewAI, AutoGen, and LangGraph**. Integrate an LLM layer that interprets user text and implements a **tool-calling protocol** to trigger queries or critiques from classical modules. Structure teaching around the **Coordinator, Worker, and Delegator (CWD) model**, as agents need planning and tool-use capabilities to complete complex tasks. |  | 
| **Week 81** | **Evaluation and Experimentation** | **Performance & RAG Evaluation** | Define and implement **quantitative metrics** for the system, such as task success rate, plan optimality gap, regret, and latency. Implement an experiment harness for end-to-end logging and metrics. Introduce modern RAG evaluation tools such as **Ragas** and **DeepEval**. Evaluation metrics should track Context Relevance, Faithfulness, and Answer Relevance. |  | 
| **Weeks 82–86** | **GenAI-Ops and Monitoring** | **Production Pipeline & Drift** | Augment the MLOps curriculum to specifically cover **GenAI-Ops**. Teach monitoring techniques for unique GenAI issues, including **semantic drift** (degradation of meaning/style) and adversarial attacks like **prompt injection and jailbreaking**. GenAI-Ops must cover extending CI/CD to prompt engineering and monitoring for drift in RAG pipelines. Defensive measures should include **Red Teaming**. Model monitoring is crucial for detecting **model decay**. |  | 

#### Module 2: Trust, Safety, and Explainable AI (Weeks 87–94)

This module implements the theoretical and ethical requirements of Trustworthy AI (TAI), translating philosophical concepts into engineering specifications.

| Week Range | Bootcamp Module Title | Core Focus Areas | Detailed Topics and Goals | Sources | 
|---|---|---|---|---|
| **Weeks 87–94** | **Trustworthy AI (TAI) Implementation** | **TAI, XAI, and Safety** | Implementation of TAI principles, which require **robustness, interpretability, and privacy**. Reinforce that TAI is implemented through engineering practice and emphasize **transparency**. Technical instruction on **Explainable AI (XAI)** techniques. |  | 
| **Weeks 87–94** | **Explainability and Meta-Reasoning** | **Introspection in Agents** | Strengthen the XAI module by linking it to **meta-reasoning**. Meta-reasoning allows the agent to evaluate its own reasoning processes, estimate uncertainty, identify knowledge gaps, and determine how much reasoning to perform to ensure the output is consistent with the design goals. |  | 
| **Weeks 87–94** | **AI Security and Adversarial Defenses** | **Security Engineering** | Mandatory modules must cover **AI security, adversarial attacks, and necessary defenses**. This includes privacy risks in ML applications, specific adversarial attacks (e.g., evasion attacks, poisoning), and defensive countermeasures. |  | 

#### Module 3: Neuro-Symbolic Integration and Capstone (Weeks 95–104)

This final module focuses on advanced hybrid architectures and the culminating project synthesis.

| Week Range | Bootcamp Module Title | Core Focus Areas | Detailed Topics and Goals | Sources | 
|---|---|---|---|---|
| **Weeks 95–98** | **Neuro-Symbolic AI Integration** | **Verifiable Reasoning (Graph RAG)** | Study **Neuro-Symbolic integration**, combining neural and symbolic reasoning. Deepen the coverage of the hybrid approach, emphasizing how **Knowledge Graphs (KGs)** provide the verifiable, structured knowledge that anchors LLM outputs. Practical application of **Graph RAG (GraphRAG)**, demonstrating how it operationalizes classical logic and knowledge representation (AIMA Part III) into a modern, verifiable production system. KGs can categorize complex data and provide citations and **confidence scores** for RAG answers. |  | 
| **Weeks 99–104** | **Capstone Project** | **Final Project Execution and Delivery** | The final four weeks are dedicated entirely to the Capstone Experience. This project must be a synthesis point, mandating the integration of Generative AI capabilities, MLOps deployment practices, and the demonstration of Trustworthy AI compliance (e.g., verifiable outputs, drift monitoring). The project must demonstrate a **hybrid classical + modern AI system** that is technically solid and safety-aware. |  | 

Phase IV ensures that the graduates are not just trained in complex modern models but are equipped to deliver robust, ethical, and fully engineered AI systems capable of executing complex, multi-step tasks autonomously. The focus on multi-agent frameworks, GenAI-Ops, and verifiable reasoning layers transforms the theoretical knowledge from AIMA into practical, high-value engineering skills.