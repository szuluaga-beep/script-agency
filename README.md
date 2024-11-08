python -m venv .venv
.venv\Scripts\Activate.ps1
pip install "fastapi[standard]"
pip freeze > requirements.txt
fastapi dev main.py
python -m pip install requests

![alt text](image.png)