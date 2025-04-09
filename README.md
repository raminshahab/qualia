# Full Stack Demo Boilerplate

### Boiler plate using Django and Vue.js

BP is a web application that allows you to setup a boiler plate Django and VUE project using a simple Docker command and your local computer. Note: You will need Docker Desktop and have the Docker daemon running in order to use.

---

## 🚀 Setup

1. **Clone the repository:**
   ```sh
   git clone <repo_url>
   cd project_name
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


---

## 🧪 Testing

- **Django Admin Panel:** [http://localhost:8000/admin](http://localhost:8000/admin)
  - Credentials: `admin/adminpassword`
- **Vue Frontend App:** [http://localhost:5173](http://localhost:5173)
- **Running test.py inside the Docker container:** (docker exec -it <container_id> python manage.py test)

---
