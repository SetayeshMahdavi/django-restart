# AGENTS.md

Django 5.2 project (`mysite`) with two apps: `website` and `blog`. Python 3 + venv at `venv/`.

## Commands

Run everything through the venv (plain `python` on PATH may lack Django):

```
venv\Scripts\python.exe manage.py runserver
venv\Scripts\python.exe manage.py makemigrations
venv\Scripts\python.exe manage.py migrate
venv\Scripts\python.exe manage.py createsuperuser
```

No linter, formatter, or CI config exists. `blog/tests.py` and `website/tests.py` are empty boilerplate — there is no real test suite.

## Layout gotchas

- `STATIC_ROOT` is `static/` (collectstatic output) but source assets live in `statics/` (`STATICFILES_DIRS`). Don't confuse the two; note `static/` is NOT gitignored (only `staticfiles/` is).
- Templates live in the top-level `templates/` dir (per-app subdirs `templates/blog`, `templates/website`), not inside the apps.
- Empty top-level `migrations/` dir is a leftover — real migrations are per-app (`blog/migrations`, `website/migrations`).
- Media uploads go to `media/` (`authors/` avatars, `blog/` post images).

## URLs

`mysite/urls.py` mounts `website.urls` at `/` and `blog.urls` at `/blog/`, plus static/media serving in DEBUG. Namespaced as `website:*` and `blog:*`.

## Known code quirks (don't "fix" blindly)

- `website/views.py` `contact_view` hard-codes `contact.name = "......"` before saving (line 20).
- `Contact.updated_date` uses `auto_now_add` (copy-paste from `created_date`).
- `blog/views.py` `single_blog` does `Post.objects.get(id=post_id)` (raises on invalid id) and increments `counted_views` with a full save.