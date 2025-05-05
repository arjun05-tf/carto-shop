# 📋 Admin Requirements Documentation

## 👤 Role: Admin

Admins are responsible for managing the platform’s operations, users, products, and orders. They have the highest level of access and can perform actions across all other roles.

---

## 🔐 Authentication & Authorization

- The app uses **[Clerk](https://clerk.dev)** for authentication and user management across all roles.
- Admins must be verified Clerk users with a specific **custom role claim** (e.g., `role: 'admin'`).
- All admin pages and APIs must be protected by Clerk JWT and validated on the backend with Flask middleware.

---

## ✅ Functional Requirements

### 🧭 Dashboard
- Overview of platform activity:
  - Total Sales
  - Total Orders
  - Product Inventory Status
  - User/Supplier Counts
- List all orders across the system

### 👥 Manage Users
- View all users from Clerk and database
- Add, edit, or remove users (assign roles: user, supplier, delivery)
- Suspend or re-enable accounts
- Reset or trigger Clerk password resets

### 🏭 Manage Suppliers
- List all suppliers and their products
- Add/edit/remove supplier accounts
- Track supplier activity and approval status

### 🛒 Product Management
- Create, read, update, delete (CRUD) products
- View product submissions by suppliers
- Approve or reject supplier-submitted products
- Update stock levels or correct metadata

---

## 🚫 Non-Functional Requirements

## 🧪 Acceptance Criteria

- Admin can manage Clerk user roles and suspend users.
- Admin can approve/reject supplier products and view real-time order updates.
- Clerk JWT is required to access admin routes, and unauthorized requests are denied.

---

## 🔐 Clerk Integration Notes

- Clerk will handle:
  - Email/password sign-in
  - Session JWTs
  - Role-based access via metadata or session claims
- Flask middleware must decode Clerk JWT and enforce access based on role.
- Admin routes in frontend must verify role via Clerk frontend SDK.

---

## 📱 Admin Dashboard Feature Summary

| Section            | Feature                                     | Notes                                   |
|--------------------|---------------------------------------------|-----------------------------------------|
| **Overview**       | Sales KPIs, order stats                     | Live updates                            |
| **Users**          | Clerk-integrated table + role badges        | Action buttons: suspend, edit           |
| **Suppliers**      | Supplier approval flow                      | Track performance and activity          |
| **Products**       | CRUD + status filters                       | Approve or reject flows                 |
| **Orders**         | Order management and status updates         | View detailed description of past orders|
| **Reports**        | CSV/Excel export for sales/inventory        | Alerts for low stock or delayed orders  |

---

## 📌 Planned Admin API Endpoints (with Clerk Auth)

| Method | Endpoint                        | Access   | Description                        |
|--------|----------------------------------|----------|------------------------------------|
| GET    | `/api/admin/dashboard`          | Admin    | Return summary statistics          |
| GET    | `/api/admin/users`              | Admin    | List users from Clerk + DB         |
| PATCH  | `/api/admin/user/<id>`          | Admin    | Modify user role or suspend        |
| GET    | `/api/admin/suppliers`          | Admin    | List and manage supplier accounts  |
| GET    | `/api/admin/products`           | Admin    | Review and manage all products     |
| PATCH  | `/api/admin/product/<id>`       | Admin    | Approve, reject, or update product |
| GET    | `/api/admin/orders`             | Admin    | List and update order statuses     |
| GET    | `/api/admin/reports/inventory`  | Admin    | Report on low-stock products       |

---

## 📝 Clerk Setup Checklist

- [ ] Set up Clerk project and dashboard
- [ ] Define roles in Clerk metadata (`role: admin/supplier/delivery/user`)
- [ ] Use Clerk JWT verification in Flask with a decorator
- [ ] Build admin-only routes in both frontend and backend

---

