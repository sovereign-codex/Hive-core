#!/usr/bin/env python3
import os, sys, subprocess
repo = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(os.path.join(repo, '..'))  # up from scripts/
agent = os.path.join(repo, 'agents', 'archivist', 'archivist.py')
cmd = [sys.executable, agent, '--repo', repo, '--action', 'all']
raise SystemExit(subprocess.call(cmd))
