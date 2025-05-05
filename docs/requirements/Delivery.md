# 🚚 Delivery Partner Requirements Documentation

## 👤 Role: Delivery Partner

Delivery partners are responsible for dispatching approved orders from suppliers to customers. Their access is limited strictly to delivery-related information.

---

## 🔐 Authentication & Authorization

- Delivery partners must log in via **Clerk** and have a custom role claim: `role: 'delivery'`.
- All delivery APIs and dashboard routes must be protected using Clerk JWT validation on the backend (Flask).
- Delivery users should not access user, product, or financial data.

---

## ✅ Functional Requirements

### 📦 Order Management
- View a list of orders assigned to them
- Mark orders as:
  - Picked Up
  - In Transit
  - Delivered
  - Failed / Returned
- View delivery addresses and customer contact (limited fields)

### 🧭 Delivery Dashboard
- View current and completed deliveries
- Map integration (optional for later)
- Status overview of their deliveries (pending, in progress, completed)

---

## 🚫 Non-Functional Requirements

- Secure data access — delivery users can only see orders assigned to them
- Real-time updates (polling or sockets in future phase)
- Mobile-responsive frontend interface

---

## 🧪 Acceptance Criteria

- Delivery partner can log in and only see assigned orders
- Cannot view or access admin/supplier/user-only routes or data
- Can update order delivery status with validation
- All updates are tracked with timestamps

---

## 📌 Planned API Endpoints (with Clerk Auth)

| Method | Endpoint                             | Access     | Description                           |
|--------|--------------------------------------|------------|---------------------------------------|
| GET    | `/api/delivery/orders`               | Delivery   | List assigned orders                  |
| PATCH  | `/api/delivery/order/<id>/status`    | Delivery   | Update order delivery status          |
| GET    | `/api/delivery/dashboard`            | Delivery   | Show basic delivery stats             |

---

## 📝 Clerk Setup Notes

- Clerk users must include `role: delivery` in their metadata
- Flask backend must verify JWT role claim before allowing delivery access

---

