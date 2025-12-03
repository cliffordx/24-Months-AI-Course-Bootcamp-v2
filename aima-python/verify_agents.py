import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

print("Attempting to import agents...")
try:
    import agents
    print("SUCCESS: Imported agents")
except Exception as e:
    print(f"FAILURE: Could not import agents: {e}")

print("\nAttempting to import agents4e...")
try:
    import agents4e
    print("SUCCESS: Imported agents4e")
except Exception as e:
    print(f"FAILURE: Could not import agents4e: {e}")
