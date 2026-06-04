"""
Flow — a command-line habit tracker.

Group project for intro programming.
Run with:  python flow.py
"""

# ANSI color codes — make the terminal look nice
PURPLE = "\033[95m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Sample habits — Phase 2 will let users add their own
SAMPLE_HABITS = [
    {"name": "Drink water",   "icon": "💧", "done": False},
    {"name": "Exercise",      "icon": "💪", "done": True},
    {"name": "Read 10 pages", "icon": "📚", "done": False},
    {"name": "Meditate",      "icon": "🧘", "done": False},
]


def banner():
    """Print the program title."""
    print()
    print(f"{PURPLE}{BOLD}  ╔════════════════════════════════════╗{RESET}")
    print(f"{PURPLE}{BOLD}  ║           F L O W                  ║{RESET}")
    print(f"{PURPLE}{BOLD}  ║      your daily habit tracker      ║{RESET}")
    print(f"{PURPLE}{BOLD}  ╚════════════════════════════════════╝{RESET}")


def show_habits(habits):
    """Print today's habits with checkboxes."""
    done = sum(1 for h in habits if h["done"])
    total = len(habits)
    print()
    print(f"  {BOLD}Today's habits{RESET}  {GRAY}({done}/{total} done){RESET}")
    print(f"  {GRAY}{'─' * 36}{RESET}")
    for i, h in enumerate(habits, start=1):
        mark = f"{GREEN}[✓]{RESET}" if h["done"] else f"{GRAY}[ ]{RESET}"
        name = h["name"] if not h["done"] else f"{GRAY}{h['name']}{RESET}"
        print(f"  {i}. {mark} {h['icon']}  {name}")
    print()


def show_menu():
    """Print the action menu."""
    print(f"  {BOLD}What now?{RESET}")
    print(f"    {CYAN}1{RESET}  View today's habits")
    print(f"    {CYAN}2{RESET}  Add a habit")
    print(f"    {CYAN}3{RESET}  Mark a habit as done")
    print(f"    {CYAN}4{RESET}  Delete a habit")
    print(f"    {CYAN}5{RESET}  Quit")
    print()


def main():
    """Run the program."""
    habits = SAMPLE_HABITS
    banner()

    while True:
        show_menu()
        choice = input(f"  {CYAN}>{RESET} ").strip()

        if choice == "1":
            show_habits(habits)
        elif choice == "2":
            print(f"\n  {YELLOW}[ Phase 2 — add a habit ]{RESET}\n")
        elif choice == "3":
            print(f"\n  {YELLOW}[ Phase 3 — mark done ]{RESET}\n")
        elif choice == "4":
            print(f"\n  {YELLOW}[ Phase 4 — delete a habit ]{RESET}\n")
        elif choice == "5":
            print(f"\n  {PURPLE}See you tomorrow!{RESET}\n")
            break
        else:
            print(f"\n  {YELLOW}'{choice}' isn't 1–5. Try again.{RESET}\n")


if __name__ == "__main__":
    main()