# Flow Habit Tracker

Flow is a simple habit-tracking app built with Python and Streamlit. It helps users create daily habits, mark them as complete, track progress, keep streaks, and save their data locally.

The project started with a small command-line prototype in `flow.py` and now includes a graphical Streamlit app in `app.py`.

## What The App Does

Flow lets a user:

- Create an account or log in with an existing account
- Track a personal list of daily habits
- Mark habits as done or undo them for the current day
- Add, edit, and delete habits
- Choose an icon and color for each habit
- See daily progress as counts and percentages
- Track simple habit streaks
- Write a quick daily note
- View a basic stats page showing completed and open habits
- Save user data locally in JSON files

## Main Screens

### Login

Users must log in before seeing the habit tracker. The app stores usernames and password hashes in `users.json`.

A default test account is included:

```text
Username: test
Password: test
```

### Today

The Today page shows:

- Today's date
- Number of completed habits
- Overall completion percentage
- Number of open habits
- A progress bar
- Today's habit list
- A quick note area

### Habits

The Habits page is where users manage their habit list. Users can:

- Add a new habit
- Pick an icon
- Pick an accent color
- Mark a habit as done
- Edit a habit's name, icon, or color
- Delete habits

### Stats

The Stats page gives a simple overview of the current day:

- Total habits
- Completed habits
- Progress percentage
- Completed habit names
- Habits still open

## How Data Is Saved

The app saves data locally using JSON files.

- `users.json` stores registered users and password hashes.
- `flow_data_<username>.json` stores each user's habit data.
- `flow_data_test.json` is the saved habit data for the default `test` user.
- `flow_data.json` is the fallback data file if no user is active.

Each habit record stores its name, icon, completion state, color, streak, and last completed date. The app also stores the next habit ID, the user's note, the last active date, and simple history data.

## Requirements

You need:

- Python 3
- Streamlit

Install Streamlit with:

```bash
pip install streamlit
```

## How To Run The App

From the project folder, run:

```bash
streamlit run app.py
```

Streamlit will start a local web server and show a URL in the terminal, usually:

```text
http://localhost:8501
```

Open that URL in a browser to use the app.

## Optional: Run The Command-Line Prototype

The repository also includes an earlier terminal version of the habit tracker:

```bash
python flow.py
```

This version shows a basic menu in the terminal and was used as an early prototype before the Streamlit interface.

## Project Structure

```text
flow-habit-tracker/
├── app.py               # Main Streamlit web app
├── flow.py              # Command-line prototype and sample habits
├── users.json           # Local user accounts with password hashes
├── flow_data_test.json  # Saved data for the default test user
└── README.md            # Project documentation
```

## Notes For Development

- The app uses local JSON files instead of a database.
- Passwords are hashed with SHA-256 before being saved.
- Usernames are converted into safe filenames for per-user habit data.
- Streamlit session state is used to keep track of login state, current habits, editing mode, notes, and page interactions.
- This project is intended as an introductory programming project, so the code favors readability over complex architecture.

