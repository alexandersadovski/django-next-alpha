# Next - A Django-Based Dating App

**Next** is a modern dating application built using Django, designed to provide a smooth and engaging user experience. The app allows users to connect with others through swiping and mutual matches, fostering meaningful conversations.

---

## Key Features

### User Profile Management
- **Registration**: Users can sign up and create a profile.
- **Profile Customization**: View, edit, or delete your profile as needed.
- **Password Management**: Change your password anytime for enhanced security.

### Matchmaking Functionality
- **Swiping Mechanism**: Users can swipe through profiles to indicate their interest.
- **Mutual Matches**: When two users like each other, a match is formed, allowing them to connect further.
- **Chat Integration**: Matched users can initiate and engage in conversations.

### Chat Features
- **Conversations List**: View all ongoing conversations in one place.
- **Messaging**: Chat with your matches seamlessly.
- **Conversation Management**: Option to delete conversations when needed.

### Reporting System
- **Report User**: Users can report inappropriate behavior or other concerns.
- **Report Tracking**: View the status of reports, categorized as **Pending**, **Resolved**, or **Dismissed**.

### Admin Panel
- **Report Review**: A dedicated "report reviewer" role has access to the admin panel to manage user reports effectively.
- **Status Management**: Update the status of reports to keep users informed.

---

## Technology Stack
- **Backend**: Django
- **Frontend**: A mix of HTML, CSS, Django Template Language (DTL), and JavaScript with AJAX for dynamic interactions.
- **Database**: PostgreSQL

---

## How It Works
1. Register and create a profile.
2. Swipe through user profiles to like or pass on them.
3. When a mutual match occurs, start chatting and get to know each other.
4. Use the reports feature to flag any concerns and track their resolution.

---

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
