# 📌 Project Statement

## 💰 Personal Budgeting Tool

### Problem Statement

Managing personal income and expenses can become difficult when financial information is recorded manually or scattered across different places. Students and individuals may not have a simple way to record their income sources, track their monthly expenses, and understand how much money remains after spending.

The **Personal Budgeting Tool** is a Python-based command-line application developed to provide a simple and structured way to manage basic personal budget information.

### 🎯 Objective

The main objective of this project is to create a beginner-friendly budgeting application that can:

- Register users and generate a unique User ID.
- Store user information using JSON.
- Record multiple sources of monthly income.
- Record different types of monthly expenses.
- Calculate total monthly income.
- Calculate total monthly expenses.
- Calculate the remaining amount after expenses.
- Calculate expense and savings percentages.
- Compare savings with a suggested 25% project target.
- Alert the user when expenses are greater than income.
- Provide a basic budget analysis.

### 💡 Proposed Solution

The application uses a modular Python structure in which different tasks are handled by separate modules.

The application follows this basic flow:

```text
User
  │
  ▼
Registration / Existing User
  │
  ▼
User ID
  │
  ├──────────────► Income Sources
  │
  └──────────────► Expenses
                         │
                         ▼
                    Budget Analysis
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
            Income     Expenses   Savings
              │          │          │
              └──────────┼──────────┘
                         ▼
                  Budget Report
```

User data is stored in `src/user_data.json`, allowing the application to retrieve previously entered information when an existing User ID is provided.

### 🧮 Budget Analysis

The application calculates the budget using:

```text
Remaining Amount = Total Monthly Income - Total Monthly Expenses
```

```text
Expense Percentage =
(Total Monthly Expenses / Total Monthly Income) × 100
```

```text
Savings Percentage =
(Remaining Amount / Total Monthly Income) × 100
```

The project uses **25% savings as a suggested project target** for its basic analysis. This is a project guideline and is not intended to represent universal financial advice.

### 🛠️ Technologies Used

- Python
- JSON
- Command-Line Interface (CLI)
- File Handling
- Git & GitHub

### 🧠 Concepts Applied

This project applies several Python concepts, including:

- Variables and data types
- User input and output
- Conditional statements
- `for` and `while` loops
- Functions and return values
- Function parameters
- Dictionaries and nested dictionaries
- Dictionary methods
- `match-case`
- Modules and imports
- File handling
- JSON data storage and retrieval
- Type conversion
- Arithmetic operations
- Modular programming

### 📁 Project Scope

The current version focuses on basic personal budgeting and is intentionally kept simple. It does not provide professional financial advice or connect to bank accounts, investment platforms, or external financial services.

Future versions may include:

- Graphical budget visualizations
- Monthly and historical tracking
- Financial goals
- More detailed analytics
- Improved input validation
- GUI
- AI-based budgeting assistance

### 📚 Purpose of the Project

This project was developed as a practical learning project to apply Python programming concepts to a real-world problem. It demonstrates how fundamental programming concepts can be combined to build a functional application with persistent data storage and modular code organization.
