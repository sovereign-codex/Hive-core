# Codex API (prototype) for AVOT-Archivist
import json, hashlib, os, datetime, hmac

class CodexAPI:
    def __init__(self, repo_root='.'):
        self.root = repo_root
        self.scroll = os.path.join(self.root, 'codex', 'scrolls', '0001-Sovereign-Aikido-Core-Spec')
        self.spec_path = os.path.join(self.scroll, 'spec.json')
        self.md_path = os.path.join(self.scroll, 'index.scroll.md')
        self.schema_path = os.path.join(self.root, 'codex', 'schema', 'scroll.schema.json')
        self.evo_path = os.path.join(self.scroll, 'evolution.log')
        self.seal_path = os.path.join(self.scroll, 'seal.sig')

    def read_json(self, p):
        with open(p, 'r', encoding='utf-8') as f:
            return json.load(f)

    def write_json(self, p, obj):
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(obj, f, indent=2)

    def sha256(self, path):
        h = hashlib.sha256()
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                h.update(chunk)
        return h.hexdigest()

    def append_evolution(self, line):
        ts = datetime.datetime.utcnow().isoformat()+'Z'
        with open(self.evo_path, 'a', encoding='utf-8') as f:
            f.write(f"[{ts}] {line}\n")

    def load_spec(self):
        return self.read_json(self.spec_path)

    def save_spec(self, spec):
        self.write_json(self.spec_path, spec)

    def check_md_json_parity(self):
        spec = self.load_spec()
        md = open(self.md_path, 'r', encoding='utf-8').read()
        ok = (spec.get('title','') in md) and (spec.get('version','') in md)
        return ok

    def seal(self, seed_hex):
        key = bytes.fromhex(seed_hex)
        h = hmac.new(key, digestmod='sha256')
        h.update(open(self.spec_path,'rb').read())
        h.update(open(self.md_path,'rb').read())
        sig = h.hexdigest()
        with open(self.seal_path, 'w', encoding='utf-8') as f:
            f.write(f'SEALED sha256-hmac-proto {sig}\n')
        return sig
