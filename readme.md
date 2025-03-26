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

### 4 **Run the Development Server**
```bash
python manage.py runserver
```
Server will be running at: `http://127.0.0.1:8000/`

---

##  **Sample API Requests**

### 1️ **Create a Task**
**Endpoint:**
```
POST /api/create-tasks/
```
**Request Body:**
```json
{
    "name": "Report Creation",
    "description": "Create Report",
    "task_type": "normal",
    "status": "pending"
}
```
**Response:**
```json
{
    "id": 5,
    "assigned_users": [],
    "name": "Report Creation",
    "description": "Create Report",
    "created_at": "2025-03-26T11:32:01.037160Z",
    "completed_at": null,
    "task_type": "normal",
    "status": "pending"
}
```

### 2️ **Assign Task to Users**
**Endpoint:**
```
POST /api/assign-tasks/
```
**Request Body:**
```json
{
    "task_id": 3,
    "user_ids": [10]
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
GET /api/get-tasks-of-user/<int:user_id>
```
**Example:**
```
GET /api/get-tasks-of-user/1
```
**Response:**
```json
[
    {
        "id": 1,
        "assigned_users": [],
        "name": "Fix Bug",
        "description": "Resolve the production issue",
        "created_at": "2025-03-25T20:50:43.542583Z",
        "completed_at": null,
        "task_type": "urgent",
        "status": "pending"
    },
    {
        "id": 2,
        "assigned_users": [],
        "name": "Documentation",
        "description": "Create Documentation",
        "created_at": "2025-03-25T21:22:19.909325Z",
        "completed_at": null,
        "task_type": "normal",
        "status": "pending"
    }
]
```

---

##  **Test Credentials**
For Admin:
- **Username:** admin
- **Password:** admin

For other User:
- **Username:** TestUser1
- **Password:** Test@123




