# finquery-streamlit
AI-Powered Financial Query application

## Project structure
```aiignore
├── .gitignore 
├── .github 
│   └── workflows
│       └── cicd.yml
├── Dockerfile 
├── LICENSE
├── README.md
├── data
│   ├── Finance Dataset Description.docx
│   ├── accounting_transactions.csv
│   ├── financial_transactions.csv
│   └── sample_sales_data.csv
├── k8s
│   ├── deployment.yaml
│   ├── hostpath-pv.yaml
│   ├── hostpath-pvc.yaml
│   ├── ingress.yaml
│   └── service.yaml
├── pyproject.toml
├── run.sh
├── scripts
│   └── create_db.sql
├── src
│   └── finquery_streamlit
│       ├── app.py
│       ├── db_agent.py
│       ├── orchestrator.py
│       ├── plotly_agent.py
│       ├── presentation_agent.py
│       └── settings.py
├── tests
│   ├── __init__.py
│   └── test_math.py
├── uv.lock
└── var
    ├── conf
    │   └── finquery
    │       └── .env.dev
    └── log
```
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
uv run streamlit run src/finquery_streamlit/app.py
^c
```

## Local Docker setup
### Configure
Copy the configuration template:
```bash
cp var/conf/finquery/.env.dev-docker var/conf/finquery/.env-docker
```
Edit `var/conf/finquery/.env-docker` with your values

### Build and run the docker image
```bash
./run.sh
```

### Hit the app
visit <http://localhost:8511>

*Note*: if you're accessing a database on localhost, you might have to
change your Host to `host.docker.internal`

## Local k3d setup
### Prerequisites
- Docker installed
- k3d installed (`curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash`)

### Record the configuration directory
```bash
VAR_DIR=$(pwd)/var
```
### Create a new k3d cluster
```bash
k3d cluster create finquery --api-port 6443 -p "8899:80@loadbalancer" --volume "$VAR_DIR:/mnt/var@server:0"
```

### Encrypt the configuration
The kubernetes environment assumes that configuration exists as 
gpg-encrypted .env files on your file system.  Do not store unencrypted credentials on your
file system.

Create a GPG_PASSPHRASE:
```bash
export GPG_PASSPHRASE=$(openssl rand -base64 32)
```

Encrypt your credentials: 
```bash
rm -f var/conf/finquery/.env.dev.gpg
cat var/conf/finquery/.env|gpg --symmetric --cipher-alg AES256 --batch --passphrase "$GPG_PASSPHRASE" -o var/conf/finquery/.env.dev.gpg
```

Note: you can decrypt your conf using
```bash
gpg --batch --yes --passphrase "$GPG_PASSPHRASE" -o var/conf/finquery/.env.dev.decrypted -d var/conf/finquery/.env.dev.gpg                          
```

### Build the Docker image and import it into the cluster
```bash
docker build -t finquery:latest .
k3d image import finquery:latest -c finquery
```

### Install the configuration encryption key
```bash
kubectl create secret generic gpg-passphrase --from-literal=GPG_PASSPHRASE=$GPG_PASSPHRASE
```

### Deploy to k3d
```bash
kubectl apply -f k8s/
```

### Verify deployment
```bash
kubectl get deployments
kubectl get pods
kubectl get ingress
```

### Access the service
visit http://localhost:8899/finquery/

### Destroy cluster
```bash
k3d cluster delete finquery
```

## Data
Sample data is provided in the `data` directory.

It can be loaded into a msyql instance by setting up environment variables
```bash
export ROOT_PASSWORD=YOUR_ROOT_PASSWORD
export USER_PASSWORD=YOUR_DB_USER_PASSWORD
```
and then executing:
```bash
cd scripts
envsubst < create_db.sql | mysql --local-infile=1 -uroot -p $ROOT_PASSWORD
```