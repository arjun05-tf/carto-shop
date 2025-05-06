# 🎨 Frontend Technical Documentation

## 🚀 Stack

- **Framework:** React (or HTML + Tailwind CSS)
- **Authentication:** Clerk Frontend SDK
- **HTTP Client:** Axios (for API calls)
- **Tooling:** Vite or Create React App (recommended)

---

## 🗂️ Structure (React Example)

```

frontend/
├── public/
├── src/
│   ├── pages/         # Page components (Dashboard, Login, etc.)
│   ├── components/    # Reusable UI components
│   ├── services/      # Axios config, Clerk helpers
│   └── App.jsx
├── .env
├── package.json
└── vite.config.js

````

---

## 🧩 Clerk Setup

### 1. Install Clerk SDK

```bash
npm install @clerk/clerk-react
````

### 2. Wrap the App

```jsx
import { ClerkProvider } from "@clerk/clerk-react";

<ClerkProvider publishableKey="YOUR_CLERK_PUBLISHABLE_KEY">
  <App />
</ClerkProvider>
```

### 3. Use Protected Routes

```jsx
import { SignedIn, SignedOut, RedirectToSignIn } from "@clerk/clerk-react";
```

### 4. Role-Based Access

Use Clerk session metadata:

```js
import { useAuth } from "@clerk/clerk-react";

const { session } = useAuth();
const role = session?.publicUser?.unsafeMetadata?.role;
```

---

## 🌐 API Integration

* Use **Axios** to make requests to the Flask backend.
* Attach Clerk JWT to each request:

```js
axios.get("/api/endpoint", {
  headers: {
    Authorization: `Bearer ${session.idToken}`
  }
});
```

---

## ✅ To-Do

* [ ] Create pages for Admin, Supplier, and User dashboards
* [ ] Build Navbar, Login, and Dashboard components
* [ ] Add loading and error states
* [ ] Integrate Clerk role-based routing
