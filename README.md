## **Getting Started**

Follow these steps to get the project up and running on your local machine.

### **Commands to Start the Project**

```bash
# 1️⃣ Clone the repository
git clone https://github.com/alexandersadovski/django-next-alpha.git

# 2️⃣ Navigate into the project directory
cd path-to-project  # Replace 'path-to-project' with the actual path to project directory

# 3️⃣ Create and activate a virtual environment
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate on macOS/Linux
venv\Scripts\activate  # Activate on Windows

# 4️⃣ Install the required dependencies
pip install -r requirements.txt

# 5️⃣ Apply database migrations
python manage.py migrate

# 6️⃣ (Optional) Create a superuser (Admin) account
python manage.py createsuperuser

# 7️⃣ (Optional) Create a report reviewer (Staff) account
python manage.py createreportreviewer

# 8️⃣ (Optional) Populate the database with mock users
python manage.py populate_users

# 9️⃣ Start the development server
python manage.py runserver

# ✅ You're all set! Access the project at http://127.0.0.1:8000/
```
