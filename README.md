# Django To-Do App 🌱

It's Django To-Do App! This is a simple yet powerful task management application built with Django. The app allows users to perform CRUD (Create, Read, Update, Delete) operations effectively, enabling them to manage tasks with features like registration, login, task addition, deletion, editing, sorting, and filtering. Each task can have attributes such as category, deadline, and priority, providing a comprehensive toolset for organizing tasks efficiently.

## Features

- User registration and login
- Adding new tasks
- Editing existing tasks
- Deleting tasks
- Sorting tasks by different criteria (deadline, priority, etc.)
- Filtering tasks by priority, status
- Signing task as completed


## Installation

1. Clone the repository:
   
    ```bash
    git clone https://github.com/yourusername/todo-app.git
    cd todo-app
    ```

2. Install `virtualenv`:
    ```bash
    pip install virtualenv
    ```

3. Create a new virtual environment:
    ```bash
    virtualenv virt
    ```

4. Activate the virtual environment:
    ```bash
    source virt/Scripts/activate
    ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:
    ```bash
    python manage.py migrate
    ```

7. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:
    ```bash
    python manage.py runserver
    ```

