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

**Tip:** Keep your `profile.json` short and focused. 
