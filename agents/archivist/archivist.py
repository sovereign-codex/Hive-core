# AVOT-Archivist (prototype)
import os, json, sys, argparse
from datetime import datetime
from jsonschema import validate
from codex_api import CodexAPI

class Archivist:
    def __init__(self, repo_root='.'):
        self.api = CodexAPI(repo_root)
        self.identity = json.load(open(os.path.join(os.path.dirname(__file__), 'identity.json')))

    def validate_scroll(self):
        schema = self.api.read_json(self.api.schema_path)
        spec = self.api.read_json(self.api.spec_path)
        validate(spec, schema)
        parity = self.api.check_md_json_parity()
        if not parity:
            raise SystemExit('ERROR: index.scroll.md and spec.json appear out of parity.')
        return True

    def seal_scroll(self):
        sig = self.api.seal(self.identity['seed_hex'])
        self.api.append_evolution(f"ARCHIVIST seal: {self.identity['public_fingerprint']} sig={sig[:16]}...")
        return sig

    def genesis(self):
        self.api.append_evolution(f"GENESIS: AVOT-Archivist activated id={self.identity['public_fingerprint']}")
        return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', default='.', help='Path to repo root containing /codex')
    parser.add_argument('--action', choices=['genesis','validate','seal','all'], default='all')
    args = parser.parse_args()

    agent = Archivist(args.repo)
    if args.action in ['genesis','all']:
        agent.genesis()
    if args.action in ['validate','all']:
        agent.validate_scroll()
    if args.action in ['seal','all']:
        agent.seal_scroll()
    print('Archivist OK:', args.action)

if __name__ == '__main__':
    main()
