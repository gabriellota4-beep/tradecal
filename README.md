# TradCal

TradCal is a full-stack Django trading journal that lets authenticated traders create, review, update and delete their own trade records. The project was built as a Data Centric Development application and demonstrates relational data modelling, server-side form validation, user authentication, CRUD operations, responsive UI design, testing and cloud-ready configuration.

## Live application

The project is configured for Heroku deployment. Add the current deployed URL here before submission.

## Repository

https://github.com/gabriellota4-beep/tradecal

## User Experience (UX)

### Project goals

TradCal gives a trader a simple private journal for recording trade execution and reviewing previous trades without relying on a spreadsheet.

### User stories

- As a visitor, I can understand the purpose of TradCal and create an account.
- As a registered user, I can log in and log out securely.
- As a trader, I can create a trade with instrument, direction, entry, exit and notes.
- As a trader, I can view only my own recorded trades.
- As a trader, I can edit an existing trade when information changes or needs correction.
- As a trader, I can delete one of my trades after a confirmation prompt.
- As a trader, I receive clear validation and success feedback after actions.
- As a mobile user, I can use the journal on smaller screens through Bootstrap's responsive grid.

## Features

### Authentication and ownership

Django's authentication system is used for account creation, login and logout. Each new `Trade` is linked to the authenticated `User` through a foreign key. Trade queries are filtered by the current user and edit/delete views also check ownership.

### Full CRUD

| Operation | Implementation |
| --- | --- |
| Create | Authenticated users add trades with `TradeForm`. |
| Read | The home page lists the signed-in user's trades. |
| Update | `edit_trade` loads an existing trade into `TradeForm` and saves changes. |
| Delete | `delete_trade` accepts POST only and verifies ownership before deletion. |

### Responsive interface

Bootstrap 5 provides responsive cards, navigation, buttons and form layout. Trade cards adapt from one column on small screens to multiple columns on larger screens.

### Validation and feedback

The model form validates required fields and ensures entry/exit prices are greater than zero. Django messages provide feedback after create, update and delete actions.

## Data model

TradCal uses Django's built-in `User` model and a custom `Trade` model.

### User → Trade relationship

One `User` can own many `Trade` records. Each new trade belongs to one user. The relationship uses `on_delete=models.CASCADE`, so records do not remain orphaned if a user is deleted.

### Trade fields

| Field | Type | Purpose |
| --- | --- | --- |
| user | ForeignKey(User) | Owner of the trade |
| instrument | CharField | Traded market, e.g. MNQ |
| direction | CharField/choices | Long or Short |
| entry_price | DecimalField | Entry price |
| exit_price | DecimalField | Exit price |
| notes | TextField | Journal notes |
| created_on | DateTimeField | Creation timestamp |
| updated_on | DateTimeField | Last update timestamp |

The `user` field remains nullable only to preserve compatibility with records created by the original project version before authentication was added. All trades created through the current application are assigned to the logged-in user.

## Technologies

- Python
- Django
- Django ORM
- HTML5
- Bootstrap 5
- SQLite for local development
- PostgreSQL through `DATABASE_URL` in production
- WhiteNoise for static files
- Gunicorn
- Git and GitHub
- Heroku-ready deployment configuration

## Local installation

Clone the repository:

```bash
git clone https://github.com/gabriellota4-beep/tradecal.git
cd tradecal
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies and migrate the database:

```bash
pip install -r requirements.txt
python manage.py migrate
```

Set local environment variables. Never commit the real values. `.env.example` documents the expected names:

```text
SECRET_KEY=<your-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Start the application:

```bash
python manage.py runserver
```

## Deployment

The project is prepared for Heroku with `gunicorn`, `dj-database-url`, WhiteNoise and a `Procfile`.

1. Create the Heroku application and attach a PostgreSQL database if required.
2. In Heroku Config Vars, set a **new** `SECRET_KEY`.
3. Set `DEBUG=False`.
4. Set `ALLOWED_HOSTS` to the deployed host, for example `.herokuapp.com` or the exact application hostname.
5. Ensure `DATABASE_URL` is supplied by the database add-on.
6. Deploy the GitHub branch.
7. Run `python manage.py migrate` in the Heroku console after deployment.

The source code does not contain the production secret key or database credentials. `.env` files and SQLite databases are excluded by `.gitignore`.

> Security note: if a secret was committed in an earlier version of the repository, it must be rotated in the hosting environment because removing it from the latest source does not invalidate an exposed credential.

## Testing

### Automated tests

`trades/tests.py` includes tests for the core data and security behaviour:

- anonymous visitors cannot see private trade records;
- authenticated users can create trades;
- users can update their own trades;
- users cannot edit another user's trade;
- delete rejects GET requests and accepts an authorised POST.

Run the test suite with:

```bash
python manage.py test
```

Run Django's system checks with:

```bash
python manage.py check
```

### Manual testing checklist

| Test | Expected result |
| --- | --- |
| Sign up with valid details | Account is created and user is logged in |
| Log in with valid account | User reaches TradCal successfully |
| Submit empty/invalid trade form | Validation errors are displayed; invalid record is not created |
| Add valid trade | Trade appears in the user's journal |
| Edit trade | Updated values appear in journal |
| Delete trade | Browser asks for confirmation and POST removes the record |
| Visit another user's edit URL | Application returns 404 |
| Log out | Private trades are no longer visible |
| Resize to mobile width | Navigation, forms and trade cards remain usable |

### Validator checks before submission

The final deployed pages should be checked with the W3C HTML validator and CSS validator. Any third-party Bootstrap CDN warnings should be distinguished from project-authored markup errors.

## Security

- Production `SECRET_KEY` comes from an environment variable.
- `DEBUG` defaults to `False`.
- `ALLOWED_HOSTS` is configured from the environment rather than `*`.
- CSRF protection is enabled and all state-changing forms use `{% csrf_token %}`.
- Delete is POST-only.
- Edit and delete operations verify record ownership.
- Secure cookies are enabled when `DEBUG=False`.
- `.env`, local SQLite databases and virtual environments are ignored by Git.

## Version control

Git and GitHub are used for source control. Commits should be small and descriptive, for example:

- `Add user ownership to Trade model`
- `Implement edit and secure delete CRUD views`
- `Add authentication and responsive navigation`
- `Move production secrets to environment variables`
- `Add CRUD and ownership tests`
- `Expand README with data model testing and deployment`

## Known limitations / future improvements

- Add calculated profit/loss fields.
- Add filters by instrument and date.
- Add performance statistics and charts.
- Add pagination for large journals.
- Migrate legacy pre-authentication records to a known owner where appropriate.

## Author

Gabriel Dada Lota
