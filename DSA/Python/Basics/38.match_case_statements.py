# Match-Case Statements (Python 3.10+)
# - A cleaner, more readable alternative to writing many 'elif' statements.
# - Also known as "Structural Pattern Matching".
# - It compares a 'subject' value against one or more 'patterns'.
# - Very similar to the 'switch-case' statement found in Java, C++, or JavaScript.

print("--- 🔀 Match-Case Statements 🔀 ---")

# --- 1. Basic Match-Case (Replacing If-Elif) ---
print("\n--- 1. Basic Example (Days of the week) ---")

def day_of_week(day):
    # 'day' is the subject we are matching against
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:   # The underscore '_' is the wildcard character (the "default" case if nothing else matches!)
            return "Not a valid day"

print(f"Day 2 is: {day_of_week(2)}")
print(f"Day 6 is: {day_of_week(6)}")
print(f"Day 9 is: {day_of_week(9)}")


# --- 2. Grouping Patterns using '|' (OR) ---
print("\n--- 2. Grouping Patterns ---")

# We can use the bitwise OR operator (|) to check multiple patterns in a single case!
def is_weekend(day):
    match day.capitalize():
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Invalid input. Please enter a day."

print(f"Is Saturday a weekend? : {is_weekend('Saturday')}")
print(f"Is Monday a weekend?   : {is_weekend('Monday')}")
print(f"Is Pizza a weekend?    : {is_weekend('Pizza')}")


# --- ⏱️ Time Complexities (Average Case) ---
# Match-case evaluates patterns sequentially from top to bottom, similar to if-elif.
day_of_week(2)             # Match Case Evaluation - O(N) (Where N is the number of cases evaluated before a match is found)
