## Python Flask Login with 5s Loading Screen

A simple Flask app that provides a login page (username `whiteout`, password `123`). After a successful login, it shows a loading screen for 5 seconds and then opens a dashboard.

### Credentials
- **Username**: `whiteout`
- **Password**: `123`

### Setup
Option A: Use user-level pip (no virtualenv):
```bash
python3 -m pip install -r requirements.txt --user
```

Option B: Use a virtual environment (recommended):
```bash
sudo apt-get update && sudo apt-get install -y python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run
```bash
python3 app.py
```

Open `http://localhost:8000` in your browser.

### Notes
- Change credentials by editing `VALID_USERNAME` and `VALID_PASSWORD` in `app.py`.
- Click "Skip" on the loading screen to go to the dashboard immediately.