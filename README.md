# Just Eat Takeaway — Restaurant Finder

Submission for the Just Eat Takeaway Early Career SWE role.

A Django web app that lets you search for restaurants by UK postcode using the Just Eat API, with a Just Eat-branded frontend.

## Live Demo

Deployed on Render (free tier). Visit the root URL and you land straight on the search page.

> First visit after a period of inactivity may take ~30 seconds to load — Render spins down free services when idle and restarts them on demand.

## Features

- Search restaurants by UK postcode
- 10 quick-pick postcode buttons for common London areas
- Restaurant cards showing name, cuisines, rating (as a number), and address
- Limited to the first 10 restaurants returned
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

## Assumptions & Things Not Clear

- The API returns a large restaurant object — I assumed only the four required fields (name, cuisines, rating, address) plus the logo URL were worth extracting. The logo is displayed as a nice-to-have but is not one of the required data points.
- "Rating as a number" — the API returns `starRating` as a float (e.g. `4.5`). I display this as-is rather than rounding, as it felt more informative.
- "Address" — the API splits address across multiple fields (`firstLine`, `city`, `postalCode`). I display all three joined together as a full address since `firstLine` alone felt incomplete.
- The brief says to limit to 10 restaurants. I apply this limit at the service layer (`[:10]`) before any data is passed to the frontend.

## Improvements I'd Make

- **Caching** — every search hits the Just Eat API live. Adding a short cache (e.g. 5 minutes per postcode) would reduce latency and avoid rate limiting.
- **Pagination or load more** — currently hard-capped at 10. A "show more" button would improve usability without overwhelming the page.
- **Sorting and filtering** — let users sort by rating or filter by cuisine type.
- **Better error messages** — currently a failed API call silently returns an empty list. Surfacing a user-friendly "something went wrong" message would improve the experience.
- **Postcode autocomplete** — as the user types, suggest valid UK postcodes.
- **Tests for the view layer** — existing tests cover the service and basic view behaviour, but more edge cases could be covered (e.g. API timeout UI behaviour).

## Build Notes

1. **User-Agent fix** — The Just Eat API returns a 403 / empty body if no `User-Agent` header is sent. Added a custom header in `services.py` to resolve this.

2. **Architecture** — Standard Django MVT: `PostcodeForm` validates input, `get_restaurants()` in `services.py` calls the API, the view wires them together.

3. **Error handling** — Four cases covered:
   - Invalid postcode format (e.g. `ZZZ`, `123`) — caught at the form level with regex validation
   - API returns non-200 (valid format but unknown postcode, API down, rate limited) — caught in the service layer
   - API timeout / network error — caught in the service layer
   - API returns 200 but empty restaurant list — handled in the template

## AI Disclosure

- **Claude** (Anthropic) — used to generate the frontend HTML/CSS template
- **ChatGPT** (OpenAI) — used to debug the Render deployment configuration
