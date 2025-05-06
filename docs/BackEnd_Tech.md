# 💾 Backend Technical Documentation

## ⚙️ Stack

- Python 3.x
- Flask
- SQLAlchemy
- Clerk JWT middleware
- SQLite or PostgreSQL

## 📁 Structure

```
backend/
├── app/
│ ├── routes/
│ ├── models/
│ ├── middleware/ # Clerk auth
│ ├── services/
│ └── utils/
├── main.py
├── config.py
├── requirements.txt
└── .env
```

---


## 🔐 Clerk Integration (Backend)

- 1. Use `Authorization: Bearer <JWT>` header.
- 2. Create a Flask middleware or decorator to:
   - Verify Clerk JWT
   - Extract role from session claims
   - Reject if not authorized

### Example pseudo-decorator:

```python
from flask import request, abort
import jwt  # Use Clerk’s JWKS to verify token

def require_role(role):
    def wrapper(f):
        def decorated(*args, **kwargs):
            token = request.headers.get("Authorization").split()[1]
            decoded = verify_clerk_jwt(token)
            if decoded['role'] != role:
                abort(403)
            return f(*args, **kwargs)
        return decorated
    return wrapper
```
---

## 🔗 Sample Endpoints:

| Method | URL                    | Auth     | Purpose            |
| ------ | ---------------------- | -------- | ------------------ |
| GET    | `/api/admin/dashboard` | Admin    | Show system stats  |
| POST   | `/api/products`        | Supplier | Create new product |
| GET    | `/api/user/products`   | User     | Browse products    |

--- 

## ✅ Setup:

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run

```
---

## 📋 To-Do
- Write full Clerk JWT verification middleware
- Seed sample data
- Add test coverage with pytest

---