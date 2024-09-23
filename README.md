# Bloggy-V0

A simple blog application built using Django, featuring basic CRUD functionality for blog posts, and a REST API.

## Features

- Create, read, update, and delete blog posts.
- API endpoints for blog posts.
- Basic front-end templates using HTML.

## Project Structure


```myblog/
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── serializers.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── blog/
│           ├── post_list.html
│           ├── post_detail.html
│           └── post_form.html
├── __init__.py
├── settings.py
├── urls.py
└── wsgi.py
├── manage.py
├── requirements.txt
└── env/
```


# Getting Started

## Create a Virtual Environment
```bash
python -m venv myenv
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Set Up the Project

### Migrate the Database
(Note: This project is designed without a database, but this step is usually required):
```bash
python manage.py migrate
```

### Create a Superuser
(For accessing the admin panel):
```bash
python manage.py createsuperuser
```

### Run the Development Server
```bash
python manage.py runserver
```

### Access the Application
Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage
- Visit the homepage to view all blog posts.
- Click on "Create New Post" to add a new blog post.
- Click on a post title to view details, edit, or delete the post.

## API Endpoints
- **GET /api/posts/**: List all posts.
- **POST /api/posts/**: Create a new post.
- **GET /api/posts/{slug}/**: Retrieve a specific post.
- **PUT /api/posts/{slug}/**: Update a specific post.
- **DELETE /api/posts/{slug}/**: Delete a specific post.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.


