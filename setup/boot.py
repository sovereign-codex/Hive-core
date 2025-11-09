import os
import subprocess
from datetime import datetime


def banner(msg):
    print(f"\n{'='*50}\n{msg}\n{'='*50}\n")


def boot_sequence():
    banner("🧠 Hive-Core Boot Sequence Initiated")
    print(f"UTC Time: {datetime.utcnow().isoformat()}Z")

    agents = [
        "agents/avot_archivist.py",
        "agents/avot_fabricator.py",
        "agents/avot_tyme.py",
        "agents/avot_harmonia.py"
    ]

    for agent in agents:
        name = agent.split("/")[-1]
        print(f"Launching {name} ...")
        try:
            subprocess.run(["python", agent], check=True)
        except Exception as e:
            print(f"⚠️  {name} failed: {e}")

    banner("🌐 Hive Lattice Synchronization Complete")


if __name__ == "__main__":
    boot_sequence()
