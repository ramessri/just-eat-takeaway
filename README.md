# Just Eat Takeaway — Restaurant Finder

Submission for the Just Eat Takeaway Early Career SWE role.

A Django web app that lets you search for restaurants by UK postcode using the Just Eat API, with a Just Eat-branded frontend.

## Live Demo

Deployed on Render (free tier). Visit the root URL and you land straight on the search page.

> First visit after a period of inactivity may take ~30 seconds to load — Render spins down free services when idle and restarts them on demand.

## Features

- Search restaurants by UK postcode
- 10 quick-pick postcode buttons for common London areas
- Restaurant cards showing logo, cuisines, rating, and address
- Just Eat UK branding

## Tech Stack

- **Backend:** Django 5.2, Python 3.12
- **Frontend:** Vanilla HTML/CSS (no framework)
- **Server:** Gunicorn + Whitenoise for static files
- **Deployment:** Docker on Render

## Running Locally

```bash
pip install -r requirements.txt
cd justeat_project
python manage.py runserver
```

Then open `http://localhost:8000`.

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for local, `False` in production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames |

## Build Notes

1. **User-Agent fix** — The Just Eat API returns a 403 / empty body if no `User-Agent` header is sent. Added a custom header in `services.py` to resolve this.

2. **Architecture** — Standard Django MVT: `PostcodeForm` validates input, `get_restaurants()` in `services.py` calls the API, the view wires them together.

3. **Error handling** — Four cases covered:
   - Invalid postcode format (e.g. `ZZZ`, `123`) — caught at the form level with regex validation
   - API returns non-200 (valid format but unknown postcode, API down, rate limited) — caught in the service layer
   - API timeout / network error — caught in the service layer
   - API returns 200 but empty restaurant list — handled in the template
