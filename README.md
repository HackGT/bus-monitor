# bus-monitor

## Installation and Setup

### Requirements
- Python 3.6 (it's _insert year_!)
- virtualenv

### Install
- Setup a virtual environment `virtualenv -p python3 venv`
- Activate virtual environment `source venv/bin/activate` (depends on your shell)
- Install dependencies `pip install -r requirements.txt`

### Configure: TODO
- `cp config.example.ini config.ini`
- Edit `config.ini` if necessary

### Start!
- `export FLASK_APP=app.py`
- `flask run` or `python -m flask run`
