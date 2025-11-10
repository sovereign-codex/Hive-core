#!/usr/bin/env python3
import json, sys, pathlib
from jsonschema import validate

root = pathlib.Path(__file__).resolve().parents[1]
schema = json.loads(open(root/'codex'/'schema'/'scroll.schema.json').read())

spec = json.loads(open(root/'codex'/'scrolls'/'0001-Sovereign-Aikido-Core-Spec'/'spec.json').read())
validate(spec, schema)
print('OK: spec.json validates against scroll.schema.json')
