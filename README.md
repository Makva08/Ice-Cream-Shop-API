# Ice-Cream Shop API

Created a secure API for an ice-cream shop

Project is implemented in Python (utilizing Flask), and the main goal of it is to provide protected endpoints that clients (such as web or mobile frontends) can use to manage ice-cream offerings and user interactions.

It provides CRUD (Create, Read, Update, Delete) operations for ice cream fvalors, user authentication, and database persistence, making it suitable as the backend for a web or mobile ordering application.

Project only enables for authorized users to access/modify shop data (authentication performed via tokens), as well as create, update, view or delete ice-cream products (can be performed daily, based on the physical stock). User management is implemented, and admin will be able to register, authenticate and manage user accounts based on hiring of employees.

Storage is implemented using SQLite, and for clean and consistent API RESTful Design is utilized.
