# finquery-streamlit
AI-Powered Financial Query application

## Get the project
Find a suitable dir (such as `~/Data/code`) and:
```bash
cd ~/Data/code
rm -rf finquery-streamlit
git clone git@github.com:ericmelz/finquery-streamlit.git
cd finquery-streamlit
```

## Local laptop native setup
### Install uv if it's not already on your system

```bash
pip install uv
```

### Create and activate a virtual environment
```bash
uv venv
```

### Install dependencies, including development dependencies
```bash
uv pip install -e ".[dev]"
```

### Run tests
```bash
uv run pytest
```

### Run the app
```bash
uv run streamlit run src/app.py
^c
```
