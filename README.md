# TradCal

TradCal is a Django-based trading journal application that allows traders to record and review their trades in one place.

## Features

- View all recorded trades
- Add new trades
- Store:
  - Instrument
  - Direction
  - Entry Price
  - Exit Price
  - Notes
- Trade records stored in a SQLite database
- Responsive layout using Bootstrap

## Technologies Used

- Python
- Django
- HTML
- Bootstrap 5
- SQLite
- Git
- GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/gabriellota4-beep/tradecal.git
```

Navigate to the project:

```bash
cd tradecal
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

## Usage

1. Open the application.
2. Click Add Trade.
3. Enter trade details.
4. Save the trade.
5. Review trades on the home page.

## Future Improvements

- User authentication
- Trade editing
- Trade deletion confirmation
- Profit and loss calculations
- Trading performance statistics
- Charts and analytics dashboard

## Testing

Testing was carried out by:

- Adding new trades
- Verifying trade data displays correctly
- Checking page navigation
- Verifying database storage
- Testing form submission

## Version Control

Git and GitHub were used for version control throughout development.

## Author

Gabriel Dada Lota