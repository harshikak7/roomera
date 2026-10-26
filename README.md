# Roomera: Smart Roommate Matching Allocation System

Roomera is a full-stack, intelligent hostel accommodation and roommate matching platform built as an Research project. It combines preference-based weighted compatibility algorithms with real-time messaging and an administrative bed-allocation dashboard to streamline institution-level housing.

---

## 🚀 Tech Stack

* **Frontend:** React (Vite), React Router, Tailwind CSS, Lucide React, Framer Motion
* **Backend:** Python (FastAPI), Pydantic v2, Uvicorn
* **Database & ORM:** PostgreSQL, SQLAlchemy (Core/ORM), Alembic (Migrations)
* **Real-Time:** Native WebSockets (for live messaging)

---

## 📁 Project Architecture

```text
roomera/
├── frontend/                  # React + Vite Client Application
│   ├── public/                # Static assets & curated avatars
│   ├── src/
│   │   ├── components/        # Reusable UI & Layout elements
│   │   ├── features/          # Feature-based modules (auth, profile, matching, chat, admin)
│   │   ├── lib/               # API client setup (Axios)
│   │   └── App.jsx            # Core application entry point
│   ├── .env.local             # Local frontend environment variables
│   └── package.json
│
├── backend/                   # FastAPI Server Application
│   ├── app/
│   │   ├── api/v1/            # API endpoint routers
│   │   ├── core/              # Config & security utilities
│   │   ├── db/                # SQLAlchemy session & base models
│   │   ├── models/            # Database ORM models
│   │   ├── schemas/           # Pydantic request/response validation schemas
│   │   ├── services/          # Business logic (matching, allocation, OTP)
│   │   └── websocket/         # Real-time chat socket manager
│   ├── migrations/            # Alembic database migration versions
│   ├── data/                  # CSV datasets and private records
│   ├── scripts/               # Database seeding scripts
│   ├── tests/                 # Backend test suite
│   ├── .env                   # Local backend secrets & database URI
│   └── requirements.txt
│
└── docs/                      # Project documentation and architecture notes