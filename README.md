# RAGLab

RAGLab is a modular project for experimenting with document ingestion, retrieval,
reranking, evaluation, generation, and agent workflows.

## Requirements

- Python 3.11 or newer
- A virtual environment is recommended

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Copy `.env.example` to `.env` and replace placeholder values only when a later
development stage requires them.

## Run the tests

```powershell
python -m pytest
```

## Project layout

- `raglab/`: core ingestion, retrieval, evaluation, generation, agent, and storage modules
- `api/`: API entry points
- `demo/`: demonstration applications
- `configs/`: experiment configuration files
- `data/`: raw, processed, and benchmark data
- `scripts/`: command-line workflows
- `tests/`: automated tests
