# 0x02. i18n - Internationalization in Flask
`#Back-end`

## Overview

This project focuses on building a Flask application with internationalization (i18n) features using the Flask-Babel extension. The app demonstrates how to translate text, localize timestamps, and set user preferences for locale and timezone.

## Learning Objectives

The main objectives of this project include:

- Parametrizing Flask templates to display different languages.
- Inferring the correct locale based on URL parameters, user settings, or request headers.
- Localizing timestamps according to the inferred or user-specified timezone.

## Tasks

The project consists of the following tasks, each adding a new feature to the app:

### Task 0: Basic Flask App

Set up a minimal Flask app with a single route that renders a basic template displaying a welcome message.

### Task 1: Basic Babel Setup

Install and configure the Babel extension, defining available languages (`en` and `fr`) and setting default locale and timezone configurations.

### Task 2: Get Locale from Request

Use the `request.accept_languages` to detect and apply the best matching language from supported languages.

### Task 3: Parametrize Templates

Enable template localization with `_` or `gettext` functions, creating message IDs for page titles and headers. Translation files are initialized, updated, and compiled.

### Task 4: Force Locale with URL Parameter

Implement support for a URL parameter (`locale`) that allows users to explicitly set their preferred language.

### Task 5: Mock Login System

Simulate a login system that uses a URL parameter (`login_as`) to set a user, which is then accessed through Flask’s g object.

### Task 6: Use User Locale

Prioritize locale selection based on URL parameters, user settings, and request headers in that order.

### Task 7: Infer Appropriate Timezone

Implement timezone selection using URL parameters, user settings, and defaulting to UTC if unspecified or invalid.

### Task 8: Display Current Time `#Advanced`

Display the current time on the homepage in the user’s local timezone with translated text.

## Getting Started

1. Clone the Repository:
```bash
git clone https://github.com/yourusername/alx-backend.git
cd alx-backend/0x02-i18n
```

2. Install Dependencies:
```bash
pip3 install -r requirements.txt
```

3. Run the Application:
```bash
python3 app.py
```
Open your browser and go to `http://127.0.0.1:5000`.

4. Compile Translations: Extract and compile translations after editing `.po` files:
```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
pybabel compile -d translations
```

## Features

- **Dynamic Locale Selection:** Automatically detects and applies the user's preferred language from URL parameters, user settings, or request headers.
- **Mock User Login:** Emulates user login to apply personalized settings.
- **Localized Timestamps:** Displays current time in the user's timezone.
- **Support for URL Parameter-Based Locale and Timezone:** Allows setting language and timezone directly through URL parameters.

## Files

- **app.py:** Main Flask application file.
- **Config Class:** Sets supported languages and default locale/timezone.
- **templates/:** Contains HTML templates for each stage of the project.
- **translations/:** Folder containing translation files (`.po` and `.mo`).

## Example URLs

- `http://127.0.0.1:5000/?locale=fr`: Forces the app to display in French.
- `http://127.0.0.1:5000/?login_as=2`: Simulates logging in as a user with locale preferences.
