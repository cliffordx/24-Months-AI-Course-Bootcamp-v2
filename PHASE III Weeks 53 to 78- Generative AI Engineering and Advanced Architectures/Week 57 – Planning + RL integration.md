## Week 57 – Planning + RL integration

- **Reading (1–2 sessions):** Revisit key sections of Chapter 11 (planning) and Chapter 17 (MDPs) that discuss planning vs. acting under uncertainty, using RL chapter commentary as a guide.aima.berkeley+1​

- **Coding (1–2 sessions):**

   - Implement a **hybrid agent** in gridworld: use a classical planner (A\* on known map) to propose a path, while RL (Q‑learning or SARSA) refines action choices to handle stochastic transitions or unknown costs.stonybrook+1​

   - Compare pure planning, pure RL, and hybrid approaches on the same tasks (e.g., success rate, steps to goal).modanesh.github+1​

- **Reflection:** Write about when planning is more efficient than RL, when RL is indispensable, and how a planner can reduce RL’s sample complexity.modanesh.github+1​