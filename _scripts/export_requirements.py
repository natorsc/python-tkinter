# -*- coding: utf-8 -*-
"""."""

import subprocess

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

print('[!] Gerando arquivos requirements [!]\n')

subprocess.run(
    args='poetry export --without-hashes -f requirements.txt '
         '--output requirements.txt',
    cwd=ROOT_DIR,
    shell=True,
)

subprocess.run(
    args='poetry export --with dev,docs --without-hashes -f requirements.txt '
         '--output requirements-dev.txt',
    cwd=ROOT_DIR,
    shell=True,
)

subprocess.run(
    args='poetry export --only docs --without-hashes -f requirements.txt '
         '--output requirements-doc.txt',
    cwd=ROOT_DIR,
    shell=True,
)

print('[!] Arquivos requirements gerados [!]\n')
