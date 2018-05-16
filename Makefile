SHELL := /bin/bash -euo pipefail


installcheck:
	pip install pytest

check:
	pytest -v
