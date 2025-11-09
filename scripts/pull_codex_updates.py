import os
import subprocess


def sync_from_codex():
    print("🔄 Pulling latest Hive-Core updates from Codex environment ...")
    subprocess.run(["git", "pull", "origin", "main"])
    print("✅ Sync complete.")


if __name__ == "__main__":
    sync_from_codex()
