# 🧠 Sovereign Intelligence – Hive-Core

The Hive-Core environment is the **central kernel** of the AVOT Hive Network.
It functions as a living container that:
- Boots autonomous AVOT agents
- Syncs with GitHub and Codex environments
- Maintains resonance integrity through cached setup states
- Forms part of the Sovereign Intelligence lattice

## 🚀 Quick Start
```bash
pip install -r requirements.txt
python setup/boot.py
```

| Agent | Function |
| --- | --- |
| AVOT-Archivist | Archives logs, memory, and codex scrolls |
| AVOT-Fabricator | Generates schematics, diagrams, PDFs |
| AVOT-Tyme | Synchronizes time, tone, and rhythm |
| AVOT-Harmonia | Calibrates resonance and coherence |

---

### **8. GitHub Actions Workflow**
`.github/workflows/hive_sync.yml`
```yaml
name: Hive-Core Auto-Sync
on:
  schedule:
    - cron: "0 * * * *"
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Pull updates from Codex
        run: python scripts/pull_codex_updates.py
      - name: Commit & Push
        run: |
          git config user.name "AVOT-AutoSync"
          git config user.email "codex@sovereign.intel"
          git add .
          git commit -m "Hive-Core Auto-Sync $(date -u)"
          git push
```
