### Task Manager API - Django REST Framework

##  **Project Setup & Installation**

### 1️ **Clone the Repository**
```bash
git clone <repository_url>
cd task_manager
```

### 2️ **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️ **Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️ **Create a Superuser (Admin)**
```bash
python manage.py createsuperuser
```
- Enter username, email, and password as prompted.

### 6 **Run the Development Server**
```bash
python manage.py runserver
```
Server will be running at: `http://127.0.0.1:8000/`

---

##  **API Endpoints**

### 1️ **Create a Task**
**Endpoint:**
```
POST /api/tasks/
```
**Request Body:**
```json
{
    "name": "Fix Bug",
    "description": "Resolve the production issue",
    "task_type": "urgent",
    "status": "pending"
}
```
**Response:**
```json
{
    "id": 1,
    "name": "Fix Bug",
    "description": "Resolve the production issue",
    "task_type": "urgent",
    "status": "pending",
    "assigned_users": []
}
```

### 2️ **Assign Task to Users**
**Endpoint:**
```
POST /api/tasks/assign/
```
**Request Body:**
```json
{
    "task_id": 1,
    "user_ids": [1, 2]
}
```
**Response:**
```json
{
    "message": "Task assigned successfully"
}
```

### 3️ **Get Tasks for a Specific User**
**Endpoint:**
```
GET /api/users/<user_id>/tasks/
```
**Example:**
```
GET /api/users/1/tasks/
```
**Response:**
```json
[
    {
        "id": 1,
        "name": "Fix Bug",
        "description": "Resolve the production issue",
        "task_type": "urgent",
        "status": "pending",
        "assigned_users": [
            {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com"
            }
        ]
    }
]
```

---

##  **Test Credentials**
Use the superuser account created during the setup process to access the admin panel:
```
http://127.0.0.1:8000/admin/
```

Example credentials (if you create them):
- **Username:** admin
- **Password:** admin123

---

##  **Running Tests**
You can run tests using the following command:
```bash
python manage.py test
```

---

## 🛠 **Environment Variables (Optional)**
If using `.env` file for configurations:
```
SECRET_KEY=your_secret_key
DEBUG=True
```

---




