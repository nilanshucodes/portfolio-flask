# Nilanshu — Flask Portfolio

A minimal, clean personal portfolio built with Flask. Includes Home, Projects, and Resume pages,
plus a ready-to-deploy setup using Gunicorn.

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Customize

- Edit `data/profile.json` to update name, skills, projects, and links.
- Replace `resume/Nilanshu_RESUME_232.pdf` with your latest resume (keep the same filename or update the route in `app.py`).
- Tweak styles in `static/css/main.css`.
- Add screenshots to `static/images/` and link them from `projects.html` as needed.

## Deploy on Render (Free)

1. Push this folder to a new GitHub repo.
2. On [Render](https://render.com), create **New > Web Service** and connect your repo.
3. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Region**: closest to your users
4. Add environment variable (optional): `PYTHON_VERSION=3.11`
5. Deploy. Render will give you a public URL.

## Deploy on Railway (Alternative)

1. Push to GitHub.
2. On [Railway](https://railway.app), create a new project from the repo.
3. Set the start command: `gunicorn app:app` and add a Python environment.
4. Deploy.

---

**Tip:** Keep your `profile.json` short and focused. Link to GitHub/LinkedIn for details.