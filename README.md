# Loans

# Start project
mkdir loan-approval-api && cd loan-approval-api

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

# Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/loan-approval-api.git
git branch -M main
git push -u origin main
