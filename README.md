# Loans

# Start project
cd credit-approval

# Setup virtualenv (optional)
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install flask pandas openpyxl
pip freeze > requirements.txt

# Run locally (for testing)
python app/main.py

# Run using Docker
docker-compose up --build

# api 
http://localhost:8000/api/redoc/
http://localhost:8000/api/docs/
http://localhost:8000/admin/
http://localhost:8000/api/register/
http://localhost:8000/
http://localhost:8000/api/register
these are the apis 
