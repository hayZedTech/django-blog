# Hayzed Blog API Engine

A production-grade, secure, and optimized backend REST API built using **Django** and **Django REST Framework (DRF)**. This project implements stateless JWT authentication, complex relational schemas (Posts, Comments, Likes), and features an auto-generated, interactive Swagger documentation dashboard.

## 🚀 Live Demo & Documentation
* **Live API Root:** [https://django-blog-cyxr.onrender.com/api/posts/](https://django-blog-cyxr.onrender.com/api/posts/)
* **Interactive Swagger UI:** [https://django-blog-cyxr.onrender.com/api/docs/swagger/](https://django-blog-cyxr.onrender.com/api/docs/swagger/)
* **Redoc View:** [https://django-blog-cyxr.onrender.com/api/docs/redoc/](https://django-blog-cyxr.onrender.com/api/docs/redoc/)

---

## 🛠️ Tech Stack & Architecture Decisions
* **Backend Framework:** Django & Django REST Framework (DRF)
* **Database:** PostgreSQL (Production) / SQLite (Local Development)
* **Authentication:** Stateless JSON Web Tokens (JWT) via `django-rest-framework-simplejwt`
* **API Documentation:** OpenAPI 3.0 specifications mapped via `drf-spectacular`
* **Production Server Layer:** Gunicorn WSGI server running multi-threaded worker configurations
* **Static File Management:** WhiteNoise for efficient asset compression and direct rendering
* **Configuration Security:** Environment isolation using `django-environ`

---

## 🔑 Core Features & System Rules
1. **Stateless JWT Authentication:** Users register securely with automated password hashing (`create_user`). Logins generate high-security, short-lived access tokens alongside persistent refresh tokens.
2. **Object Ownership Restrictions:** Implemented a custom object-level permission boundary (`IsAuthorOrReadOnly`). Anyone can browse public data, but modifications/deletions are violently blocked unless the active user session matches the author instance.
3. **Database Performance Optimization:** Resolved the classic $N+1$ database query bottleneck inside list operations using `.select_related()` to load user profiles in a single SQL operation.
4. **Intelligent Like Toggling:** Overrode standard HTTP creation logic to evaluate model histories on the fly. Sending a payload likes an unliked post, while repeating the exact payload deletes the record (unlikes it).
5. **Real-time Metrics:** Leveraged `SerializerMethodField` to calculate totals for post engagements concurrently.

---

## 📂 Project Directory Structure
```text
blog_api/
│
├── accounts/      # Custom User model, profile fields, authentication logic
├── posts/         # Blog postings, image handling, custom permission bindings
├── comments/      # One-to-Many nested posting comment layers
├── likes/         # Unique-constrained user liking toggle system
├── config/        # Central core routing, settings, and environment loaders
├── media/         # Local user file and photo storage arrays
├── .env           # (Hidden) Local credentials file
├── .gitignore     # Git exclusion parameters
├── Procfile       # Cloud container process execution directions
├── manage.py      # Django management script
└── requirements.txt