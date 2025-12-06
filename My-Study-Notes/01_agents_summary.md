# Study Notes: Intelligent Agents (`agents.ipynb`)

> **Session Date**: Thursday, December 5, 2025
> **Session Time**: 19:02 (GMT+8)


## 1. Phase 1: Foundations of Agents & Environments
**Goal**: Understand the basic `Agent` and `Environment` classes.

### The `Agent` Class
- **Program**: A function `f(percept)` -> `action`.
- **Location**: Agents have a `.location` attribute.
- **Life**: `.is_alive()` status usually determined by the environment.

### The `Environment` Class
- **Simulator Loop** (`run` method):
    1.  `step()`:
        - Get actions from agents (`program(percept)`).
        - Execute actions (`execute_action(agent, action)`).
        - Update environment (e.g., delete eaten food).
- **Percept**: The `percept(agent)` method defines what the agent *sees*.

---

## 2. Phase 2: 2D Environments & Visualization
**Goal**: Move from 1D text output to 2D graphical grids.

### `Park2D`
- **Grid**: A 5x5 (or similar) grid of squares.
- **Coordinates**:
    - **Code (Agent)**: Uses `(x, y)` where `x` is column, `y` is row.
    - **Visualization (Tooltip)**: Uses `(row, col)`.
    - **Movement**: The dog moves "down" by increasing the y-coordinate: `self.location[1] += 1`.
- **Simulation**: The notebook shows the dog moving step-by-step, updating the grid visualization.

### `EnergeticBlindDog`
- **Definition**: Defined in the notebook (not `agents.py`).
- **Program**:
  - Uses `random.choice` to decide actions.
  - **Logic**:
    - If `Food` or `Water` is perceived -> `eat` or `drink`.
    - If `Bump` (at edge) -> Randomly turn Left or Right.
    - Otherwise -> Randomly Turn Left, Turn Right, or Move Forward.
- **Behavior**:
  - Can produce duplicate actions like "turnleft" then "turnright" at the same location.
  - **Reason**:
    - **Turning is In-Place**: It changes `direction` but not `location`.
    - **Probabilities**: 25% Turn Left, 25% Turn Right, 50% Move Forward.
    - **Result**: The dog often "spins" in place (e.g., Left -> Right -> Left) before finally deciding to move forward.
    - **Note on Randomness**: Just like flipping a coin, getting "Heads" twice in a row is perfectly normal. The dog doesn't remember its last turn; it just rolls the dice again!


### Coordinate Confusion Alert ⚠️
- **Log Output**: Uses `[x, y]` format (Column, Row).
  - Example: `[0, 2]` means **Column 0, Row 2**.
- **Visualization Tooltip**: Uses `[row, col]` format (Row, Column).
  - Example: `Index: [0, 2]` means **Row 0, Column 2**.
- **Result**: If the log says `[0, 2]`, look for the dog at `Index: [2, 0]` in the grid!

## 5. Phase 3: The Wumpus World 🏹
A classic AI challenge requiring reasoning under uncertainty.

### The Mission
You are an **Explorer** in a dark cave. Your goal is to find the **Gold** and get out alive without falling into a **Pit** or getting eaten by the **Wumpus**.

### PEAS Description
- **Performance**:
  - +1000 for climbing out with Gold.
  - -1000 for falling into a Pit or getting eaten by Wumpus.
  - -1 for each action taken.
  - -10 for using up your arrow.
- **Environment**:
  - A 4x4 Grid of rooms.
  - **Start**: Bottom-left square [1, 1].
  - **Hazards**:
    - **Wumpus**: A beast that eats you. Notoriously smelly.
    - **Pits**: Bottomless holes. They produce a breeze.
- **Actuators**: `TurnLeft`, `TurnRight`, `Forward`, `Grab`, `Shoot`, `Climb`.
- **Sensors** (What you perceive):
  - **Stench**: In square directly adjacent to Wumpus.
  - **Breeze**: In square directly adjacent to a Pit.
  - **Glitter**: In the square where the Gold is.
  - **Bump**: If you walk into a wall.
  - **Scream**: If the Wumpus is killed.

### Visualization Legend 🗺️
The grid uses specific colors to show what exists in each square (even if your agent can't "see" it yet!):
- **🟦 Blue**: The **Explorer** (You).
- **🟧 Orange/Gold**: The **Gold** (Objective).
- **⬛ Black**: A **Pit** (Death).
- **⬜ White**: **Breeze** (Warning: Pit adjacent).
- **🌫️ Grey**: **Stench** (Warning: Wumpus adjacent).
- **Empty/Safe**: Green
- **Hazards**: Black (Pit), Brown (Wumpus)

### ⚠️ Visualization Limitation: Direction
**Crucial Point**: The blue block **does not show which way it is facing**.
- If you type `TurnRight`, the agent internally rotates, but the block looks identical.
- You must remember your direction mentally!
- **Default Start**: Usually facing **Right**.

### How to Play (The Input Box)
The popup is the Agent's "Brain" asking you for a command. You must type one of these exact strings:
- `Forward` (Move one square in facing direction)
- `TurnLeft` (Rotate 90° CCW)
- `TurnRight` (Rotate 90° CW)
- `Grab` (Pick up Gold if in same square)
- `Climb` (Exit game if at [1,1])
- `Shoot` (Fire arrow)

### 💀 Game Over Conditions
- **Death by Pit [-1000]**: You entered a **Black Square**.
- **Death by Wumpus [-1000]**: You entered a **Brown Square** (and the Wumpus was alive).
- **Victory [+1000]**: You climbed out at `[1, 1]` with the Gold.
  - **Note**: `Climb` command **DOES NOTHING** if you are not at `[1, 1]`. You must walk back!


> [!TIP]
> **Survival Strategy**: Since you can't see which way you are facing, write it down!
> "Start Right -> Turn Right (Now Down) -> Turn Right (Now Left)..."

### Decoding the Raw Percepts `[...]`
When the program prints `[[...], [...], [...], [...], [...]]`, it is showing you what the Agent "feels" in all directions:
1.  **Index 0 (Left)**: What is to your Left.
2.  **Index 1 (Right)**: What is to your Right.
3.  **Index 2 (Up)**: What is Above you.
4.  **Index 3 (Down)**: What is Below you.
5.  **Index 4 (Center)**: **Where you are right now.**

**Example**: `[..., ..., ..., ..., [<Breeze>, <Glitter>, None]]`
- `<Glitter>` in the **5th list (Center)** means **YOU FOUND THE GOLD!** 💰

---

## 4. Phase 4: Advanced Agent Architectures
**Goal**: Understand the progression from simple to sophisticated agent designs.

### Agent Architecture Hierarchy (AIMA Figures 2.7 - 3.1)

```
Table-Driven → Simple Reflex → Model-Based Reflex → Goal-Based → Utility-Based
    ↓               ↓                  ↓                  ↓              ↓
 (Memory)       (Rules)           (Internal State)    (Planning)    (Optimization)
```

### 1. Table-Driven Agent (Figure 2.7)
**Location**: [`agents.py` lines 118-133](aima-python/agents.py#L118-L133)

- **Mechanism**: Stores **entire percept history**, looks up action in a giant table.
- **Limitation**: Table size grows **exponentially** with history length.
- **Example**: [`TableDrivenVacuumAgent`](aima-python/agents.py#L209-L228)

### 2. Simple Reflex Agent (Figure 2.10)
**Location**: [`agents.py` lines 153-165](aima-python/agents.py#L153-L165)

- **Mechanism**: Maps **current percept → action** using condition-action rules.
- **No memory**: Cannot handle partially observable environments.
- **Example**: [`ReflexVacuumAgent`](aima-python/agents.py#L231-L252) — If dirty → Suck; else move.

### 3. Model-Based Reflex Agent (Figure 2.12)
**Location**: [`agents.py` lines 168-181](aima-python/agents.py#L168-L181)

- **Mechanism**: Maintains **internal state** (model of the world).
- **Advantage**: Knows when to **stop** (e.g., all squares clean → NoOp).
- **Example**: [`ModelBasedVacuumAgent`](aima-python/agents.py#L255-L279) — Remembers which squares are clean.

### 4. Goal-Based Agent (Figure 3.1)
**Location**: [`search.py` lines 92-127](aima-python/search.py#L92-L127)

- **Mechanism**: Uses **search/planning** to find action sequences.
- **Key steps**: `formulate_goal()` → `formulate_problem()` → `search()` → Execute plan.
- **Example**: [`SimpleProblemSolvingAgentProgram`](aima-python/search.py#L92-L127)

### Agent Comparison Results (Vacuum World Test)
| Agent | Score | Behavior |
|-------|-------|----------|
| **Random** | 5 | Wanders, eventually cleans |
| **Reflex** | **-10** | ⚠️ Bounces Left↔Right forever |
| **Model-Based** | **9** | ✅ Cleans, then stops with NoOp |

> [!IMPORTANT]
> The Reflex Agent got the **worst** score because it has **no memory**. Even when both squares are clean, it keeps moving, losing 1 point per move.

---

## 🎓 Executive Summary: Intelligent Agents

### 1. Agent Comparison Table
| Feature | **Blind Dog** 🐕 | **Energetic Blind Dog** 🏃 | **Wumpus Explorer** 🤠 | **Goal-Based** 🎯 |
| :--- | :--- | :--- | :--- | :--- |
| **Logic** | Fixed Sequence | Random / Stochastic | Mental Model (You!) | Planning / Search |
| **Environment** | 1D Park | 2D Park | Wumpus Cave (4x4) | Problem Space |
| **Memory** | None | None | You track it! | Internal model + Plan |
| **Key Lesson** | Hardcoded limits | Randomness ≠ Intelligence | Reasoning under Uncertainty | **Planning beats reacting** |

### 2. Key Concepts Mastered (Glossary)
- **Agent Program**: The internal function `f(percept) = action` that maps what the agent sees to what it does.
- **PEAS**: The framework to define any AI problem: **P**erformance, **E**nvironment, **A**ctuators, **S**ensors.
- **Stochastic vs. Deterministic**:
    - *Deterministic*: Output is predictable (Blind Dog).
    - *Stochastic*: Output involves randomness (Energetic Dog's coin flip).
- **Static vs. Dynamic**:
    - *Static*: The world doesn't change while you think (Wumpus World).
    - *Dynamic*: The world changes (e.g., a self-driving car).
- **Goal-Based Planning**: Formulate goal → Define problem → Search for solution → Execute plan.

### 3. Skills Acquired ✅
- [x] **Code Analysis**: Dissected `Agent` and `Environment` classes in `agents.py`.
- [x] **Debugging**: Diagnosed "spinning" behavior using trace logs.
- [x] **Visualization Decoding**: Learned to map logs `[x,y]` to visual grids `[row,col]`.
- [x] **Game Theory**: Played a partial information game (Wumpus) using sensor inference.
- [x] **Workflow**: Validated Environment Setup → Agent Init → Step execution.
- [x] **Agent Architectures**: Compared Table-Driven, Reflex, Model-Based, and Goal-Based agents.

### 4. Next Steps 🧭
- **Topic**: Search Algorithms (Solving problems by finding path sequences).
- **Notebook**: [`search.ipynb`](aima-python/search.ipynb).
- **Goal**: Stop wandering randomly and start **planning** efficient paths.

