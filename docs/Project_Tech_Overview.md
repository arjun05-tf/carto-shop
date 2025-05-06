# 🛒 E-commerce Platform – Project Overview

## 📌 Description

A role-based e-commerce platform that supports:

- Admins: Manage users, suppliers, products, orders
- Suppliers: Submit and manage product listings
- Users: Browse and place orders
- Delivery Partners *(coming later)*

## 🧱 Tech Stack

| Component      | Technology           |
|----------------|----------------------|
| Frontend       | React / HTML + Tailwind |
| Backend        | Python + Flask       |
| Authentication | Clerk.dev            |
| Database       | PostgreSQL / SQLite  |
| API Type       | RESTful JSON APIs    |

## 🔐 Authentication

- **Clerk.dev** handles user sessions and authentication.
- Users are tagged with role metadata: `admin`, `supplier`, `user`, `delivery`.
- Frontend and backend verify roles before allowing access.

## 📁 Repo Structure
project-root/
├── frontend/ # Frontend client
├── backend/ # Flask backend
├── .env # Secrets
├── README.md
└── .gitignore


## 📌 Development Flow

- Code is committed to feature branches → PR → merge into `main`
- Use Clerk for auth, and JWT verification middleware in Flask
- Store app-specific data in the database (products, orders, etc.)

## 🚧 Future Phases

- Delivery partner dashboard
- Payment integration
- Admin analytics and charts

## 📄 Docs

- [Frontend Docs](./FRONTEND_TECH.md)
- [Backend Docs](./BACKEND_TECH.md)

