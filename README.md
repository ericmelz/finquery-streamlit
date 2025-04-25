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

### Configure
Copy the configuration template:
```bash
cp var/conf/finquery/.env.dev var/conf/finquery/.env
```
Edit `var/conf/finquery/.env` with your values

### Run the app
```bash
uv run streamlit run src/app.py
^c
```

## Local Docker setup
### Build and run the docker image
```bash
./run.sh
```

### Hit the app
visit <http://localhost:8501>

*Note*: if you're accessing a database on localhost, you might have to
change your Host to `host.docker.internal`
