"""
Flow Streamlit app.

Run with:
    streamlit run app.py
"""

from copy import deepcopy
from datetime import date

import streamlit as st

from flow import SAMPLE_HABITS


st.set_page_config(
    page_title="Flow",
    page_icon="✓",
    layout="wide",
    initial_sidebar_state="expanded",
)


HABIT_ICONS = ["💧", "💪", "📚", "🧘", "🌱", "☀️", "🎯", "✍️", "🥗", "😴"]
HABIT_COLORS = ["#7c5cff", "#22d3ee", "#34d399", "#fbbf24", "#f87171", "#a78bfa"]


def load_css():
    st.markdown(
        """
        <style>
        :root {
            --bg-0: #07080c;
            --bg-1: #0b0d14;
            --panel: rgba(20, 24, 35, .72);
            --panel-hover: rgba(28, 33, 47, .92);
            --border: rgba(255, 255, 255, .08);
            --border-strong: rgba(255, 255, 255, .16);
            --text: #e8ecf3;
            --text-dim: #9aa3b2;
            --text-faint: #5b6271;
            --accent: #7c5cff;
            --accent-2: #22d3ee;
            --success: #34d399;
            --danger: #f87171;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(124, 92, 255, .18), transparent 34rem),
                radial-gradient(circle at bottom right, rgba(34, 211, 238, .12), transparent 40rem),
                var(--bg-0);
            color: var(--text);
        }

        section[data-testid="stSidebar"] {
            background: rgba(11, 13, 20, .88);
            border-right: 1px solid var(--border);
        }

        section[data-testid="stSidebar"] * {
            color: var(--text);
        }

        .block-container {
            max-width: 1160px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        h1, h2, h3 {
            letter-spacing: 0;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: .7rem;
            margin: .35rem 0 1.25rem;
            font-size: 1.25rem;
            font-weight: 800;
        }

        .brand-logo {
            width: 34px;
            height: 34px;
            border-radius: 8px;
            display: grid;
            place-items: center;
            background: linear-gradient(135deg, var(--accent), var(--accent-2));
            color: #fff;
            box-shadow: 0 10px 30px -10px rgba(124, 92, 255, .8);
        }

        .greeting {
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 800;
            line-height: 1.05;
            margin-bottom: .2rem;
            background: linear-gradient(135deg, #fff 30%, #9aa3b2);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .date-line {
            color: var(--text-dim);
            margin-bottom: 1.5rem;
        }

        .panel {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1.15rem;
            backdrop-filter: blur(20px);
            box-shadow: 0 20px 60px -28px rgba(0, 0, 0, .65);
        }

        .panel-lg {
            padding: 1.5rem;
            border-radius: 18px;
        }

        .metric-card {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1rem;
            position: relative;
            overflow: hidden;
        }

        .metric-card:before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--accent), transparent);
            opacity: .65;
        }

        .metric-label {
            color: var(--text-dim);
            font-size: .78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: .06em;
        }

        .metric-value {
            color: var(--text);
            font-size: 2rem;
            font-weight: 800;
            margin-top: .25rem;
        }

        .habit-row {
            display: flex;
            align-items: center;
            gap: .9rem;
            background: rgba(255, 255, 255, .04);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: .9rem 1rem;
            margin-bottom: .65rem;
        }

        .habit-row.complete {
            background: rgba(52, 211, 153, .08);
            border-color: rgba(52, 211, 153, .25);
        }

        .habit-icon {
            width: 42px;
            height: 42px;
            border-radius: 10px;
            display: grid;
            place-items: center;
            flex: 0 0 auto;
            font-size: 1.35rem;
            box-shadow: inset 0 0 0 1px rgba(255, 255, 255, .09);
        }

        .habit-name {
            color: var(--text);
            font-size: 1rem;
            font-weight: 700;
            line-height: 1.2;
        }

        .habit-meta {
            color: var(--text-dim);
            font-size: .82rem;
            margin-top: .2rem;
        }

        .quote-bar {
            padding: .85rem 1rem;
            background: linear-gradient(90deg, rgba(124, 92, 255, .09), rgba(34, 211, 238, .04));
            border: 1px solid var(--border);
            border-left: 3px solid var(--accent);
            border-radius: 14px;
            color: var(--text-dim);
            font-style: italic;
            margin-bottom: 1rem;
        }

        .empty {
            text-align: center;
            color: var(--text-dim);
            padding: 2rem 1rem;
        }

        div[data-testid="stProgress"] > div > div {
            background: linear-gradient(90deg, var(--accent), var(--accent-2));
        }

        .stButton > button,
        .stDownloadButton > button,
        button[data-testid="baseButton-secondary"] {
            background: rgba(255, 255, 255, .07);
            border: 1px solid var(--border);
            border-radius: 10px;
            color: var(--text);
            font-weight: 700;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            background: rgba(255, 255, 255, .12);
            border-color: var(--border-strong);
            color: #fff;
        }

        div[data-testid="stForm"] {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1rem;
        }

        input, textarea, select {
            color: var(--text) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def seed_habits():
    habits = []
    for index, habit in enumerate(deepcopy(SAMPLE_HABITS)):
        habits.append(
            {
                "id": index + 1,
                "name": habit["name"],
                "icon": habit["icon"],
                "done": habit["done"],
                "color": HABIT_COLORS[index % len(HABIT_COLORS)],
            }
        )
    return habits


def init_state():
    if "habits" not in st.session_state:
        st.session_state.habits = seed_habits()
    if "next_id" not in st.session_state:
        st.session_state.next_id = len(st.session_state.habits) + 1
    if "note" not in st.session_state:
        st.session_state.note = ""


def completion_stats():
    total = len(st.session_state.habits)
    done = sum(1 for habit in st.session_state.habits if habit["done"])
    percent = done / total if total else 0
    return total, done, percent


def add_habit(name, icon, color):
    st.session_state.habits.append(
        {
            "id": st.session_state.next_id,
            "name": name.strip(),
            "icon": icon,
            "done": False,
            "color": color,
        }
    )
    st.session_state.next_id += 1


def mark_done(habit_id):
    for habit in st.session_state.habits:
        if habit["id"] == habit_id:
            habit["done"] = True
            break


def delete_habit(habit_id):
    st.session_state.habits = [
        habit for habit in st.session_state.habits if habit["id"] != habit_id
    ]


def render_sidebar():
    st.sidebar.markdown(
        """
        <div class="brand">
            <div class="brand-logo">✓</div>
            <span>Flow</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    page = st.sidebar.radio(
        "Navigate",
        ["Today", "Habits", "Stats"],
        label_visibility="collapsed",
    )
    st.sidebar.caption("Saved in this Streamlit session")
    return page


def render_metric(label, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_habit_row(habit, show_delete=False):
    state_class = "complete" if habit["done"] else ""
    state_text = "Complete" if habit["done"] else "Waiting for today"
    row, actions = st.columns([5, 2], vertical_alignment="center")

    with row:
        st.markdown(
            f"""
            <div class="habit-row {state_class}">
                <div class="habit-icon" style="background:{habit['color']}22;color:{habit['color']}">
                    {habit['icon']}
                </div>
                <div>
                    <div class="habit-name">{habit['name']}</div>
                    <div class="habit-meta">{state_text}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with actions:
     if not habit["done"]:
        if st.button("Done", key=f"done_{habit['id']}", use_container_width=True):
        mark_done(habit["id"])
        st.rerun()
    else:
    st.write("Completed")


def render_today():
    total, done, percent = completion_stats()
    today = date.today().strftime("%A, %B %d")

    st.markdown('<div class="greeting">Good day. Keep your flow.</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="date-line">{today}</div>', unsafe_allow_html=True)

    metric_cols = st.columns(3)
    with metric_cols[0]:
        render_metric("Done Today", f"{done}/{total}")
    with metric_cols[1]:
        render_metric("Completion", f"{round(percent * 100)}%")
    with metric_cols[2]:
        render_metric("Open Habits", total - done)

    st.write("")
    st.progress(percent)
    st.markdown(
        '<div class="quote-bar">Small daily actions turn into something you can actually feel.</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.35, 1], gap="large")
    with left:
        st.subheader("Today's habits")
        if st.session_state.habits:
            for habit in st.session_state.habits:
                render_habit_row(habit)
        else:
            st.markdown('<div class="empty">No habits yet. Add one from the Habits page.</div>', unsafe_allow_html=True)

    with right:
        st.subheader("Quick note")
        st.session_state.note = st.text_area(
            "Note",
            value=st.session_state.note,
            placeholder="What would make today feel successful?",
            label_visibility="collapsed",
            height=160,
        )
        if st.button("Clear note", use_container_width=True):
            st.session_state.note = ""
            st.rerun()


def render_habits():
    st.title("Habits")
    st.caption("Add, complete, and remove the habits from your Flow list.")

    with st.form("add_habit", clear_on_submit=True):
        st.subheader("Add a habit")
        name = st.text_input("Habit name", placeholder="Example: Stretch for 5 minutes")
        cols = st.columns(2)
        with cols[0]:
            icon = st.selectbox("Icon", HABIT_ICONS)
        with cols[1]:
            color = st.selectbox("Accent color", HABIT_COLORS)
        submitted = st.form_submit_button("Add habit", use_container_width=True)

    if submitted:
        if name.strip():
            add_habit(name, icon, color)
            st.success("Habit added.")
            st.rerun()
        else:
            st.warning("Add a habit name first.")

    st.write("")
    st.subheader("Your habits")
    if st.session_state.habits:
        for habit in st.session_state.habits:
            render_habit_row(habit, show_delete=True)
    else:
        st.markdown('<div class="empty">Your habit list is empty.</div>', unsafe_allow_html=True)


def render_stats():
    total, done, percent = completion_stats()
    st.title("Stats")
    st.caption("A simple snapshot for the current day.")

    cols = st.columns(3)
    with cols[0]:
        render_metric("Total Habits", total)
    with cols[1]:
        render_metric("Completed", done)
    with cols[2]:
        render_metric("Progress", f"{round(percent * 100)}%")

    st.write("")
    st.progress(percent)

    complete = [habit["name"] for habit in st.session_state.habits if habit["done"]]
    waiting = [habit["name"] for habit in st.session_state.habits if not habit["done"]]

    cols = st.columns(2, gap="large")
    with cols[0]:
        st.subheader("Completed")
        st.write(", ".join(complete) if complete else "Nothing completed yet.")
    with cols[1]:
        st.subheader("Still open")
        st.write(", ".join(waiting) if waiting else "Everything is complete.")


def main():
    load_css()
    init_state()
    page = render_sidebar()

    if page == "Today":
        render_today()
    elif page == "Habits":
        render_habits()
    else:
        render_stats()


if __name__ == "__main__":
    main()
