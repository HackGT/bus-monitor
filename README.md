# bus-monitor

## Installation and Setup

### Requirements
- Python 3.6 (it's _insert year_!)
- virtualenv

### Install
- Setup a virtual environment `virtualenv -p python3 venv`
- Activate virtual environment `source venv/bin/activate` (depends on your shell)
- Install dependencies `pip install -r requirements.txt`

### Configure
- `cp config.example.ini config.ini`
- Edit `config.ini` if necessary
- `cp secrets.example.ini secrets.ini`
- Edit `secrets.ini` (please never deploy with default secrets file)

If deploying (with biodomes or other infrastructure) and config/secret files are
stored elsewhere you can set environment variables to their respective paths.

| environment variable  | description                                      |
|-----------------------|--------------------------------------------------|
| `BUS_MONITOR_CONFIG`  | path to config file (see `config.example.ini`)   |
| `BUS_MONITOR_SECRETS` | path to secrets file (see `secrets.example.ini`) |

### Start!
- `export FLASK_APP=server/app.py`
- `flask run` or `python -m flask run`
