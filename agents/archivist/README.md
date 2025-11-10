# AVOT-Archivist

Maintains Codex integrity: validates scrolls, appends evolution, and seals releases.

## Run (from repository root)
```bash
pip install -r agents/archivist/requirements.txt
python3 agents/archivist/archivist.py --repo . --action all
```
This will:
1) Append a GENESIS line to `codex/scrolls/0001-.../evolution.log`
2) Validate `spec.json` against `codex/schema/scroll.schema.json`
3) Create a prototype seal in `seal.sig` (HMAC SHA256 over spec+scroll)

> Identity is self-generated on seed; swap to ed25519/libsodium for production-grade signatures.
