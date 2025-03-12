# Instateam

### Team Management System using Django and Vue.js

Instateam is a web application that allows you to manage team members, including creating, updating, deleting, and listing members. It uses **Django** for the backend API and **Vue.js** for the frontend.

---

## 🚀 Setup

1. **Clone the repository:**
   ```sh
   git clone <repo_url>
   cd instateam
   ```
2. **Run the application using Docker:**
   ```sh
   docker-compose up --build
   ```

---

## 🐳 Docker Commands

### 📌 Migrate the Database
To apply database migrations, including the `add_dummy_team_members` migration, run:
   ```sh
   docker exec -it <django_container_id> python manage.py migrate
   ```

### 📌 Seed Dummy Team Members
(Currently not specified in the instructions—add if needed.)

### 📌 Run Django Development Server
   ```sh
   docker exec -it <django_container_id> python manage.py runserver 0.0.0.0:8000
   ```

### 📌 Run NPM Commands (Vue.js Frontend)
   ```sh
   docker exec -it <vue_container_id> npm install
   docker exec -it <vue_container_id> npm run dev
   ```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|---------------------------|-------------------------------|
| `GET`  | `/api/team-members/`      | List all members              |
| `POST` | `/api/team-members/`      | Create a new member           |
| `PUT`  | `/api/team-members/<id>/` | Update an existing member     |
| `DELETE` | `/api/team-members/<id>/` | Delete a member              |

---

## 🧪 Testing

- **Django Admin Panel:** [http://localhost:8000/admin](http://localhost:8000/admin)
  - Credentials: `admin/adminpassword`
- **Vue Frontend App:** [http://localhost:5173](http://localhost:5173)
- **Running test.py inside the Docker container:** (docker exec -it <container_id> python manage.py test)

---
