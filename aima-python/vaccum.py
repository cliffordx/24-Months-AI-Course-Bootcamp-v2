from dataclasses import dataclass
import itertools
import random

A, B = "A", "B"
CLEAN, DIRTY = "Clean", "Dirty"
LEFT, RIGHT, SUCK, NOOP = "Left", "Right", "Suck", "NoOp"

@dataclass
class Agent:
    location: str
    performance: int = 0

def percept(env, agent):
    return (agent.location, env["status"][agent.location])

def execute_action(env, agent, action):
    if action == LEFT:
        if agent.location == B:
            agent.location = A
            agent.performance -= 1
    elif action == RIGHT:
        if agent.location == A:
            agent.location = B
            agent.performance -= 1
    elif action == SUCK:
        if env["status"][agent.location] == DIRTY:
            env["status"][agent.location] = CLEAN
            agent.performance += 10
    elif action == NOOP:
        pass

def simple_reflex_program(percept_tuple):
    location, status = percept_tuple
    if status == DIRTY:
        return SUCK
    elif location == A:
        return RIGHT
    else:
        return LEFT

def run_trial(status_A, status_B, start_loc, steps=100, seed=0):
    random.seed(seed)
    env = {"status": {A: status_A, B: status_B}}
    agent = Agent(location=start_loc)
    for _ in range(steps):
        p = percept(env, agent)
        action = simple_reflex_program(p)
        execute_action(env, agent, action)
    return agent.performance

# Exhaustive evaluation over initial configs and start locations
def evaluate_all(steps=100):
    results = []
    for sA, sB, start in itertools.product([CLEAN, DIRTY], [CLEAN, DIRTY], [A, B]):
        score = run_trial(sA, sB, start, steps=steps, seed=42)
        results.append(((sA, sB, start), score))
    avg = sum(score for _, score in results) / len(results)
    return results, avg

if __name__ == "__main__":
    res, avg = evaluate_all(steps=100)
    print("Per-config scores:", res)
    print("Average score:", avg)

