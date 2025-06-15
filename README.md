# 💰 Bill Splitter

A modern web application for splitting bills among friends and groups, built with Flask, HTMX, and AlpineJS.

## Features

- **👥 People Management**: Add and remove people from your group
- **💳 Expense Tracking**: Record expenses with description, amount, and who paid
- **🧮 Individual Tracking**: Track what each person ordered and calculate their personal total
- **⚡ Dynamic UI**: Real-time updates using HTMX without page refreshes
- **📱 Responsive Design**: Works great on desktop and mobile devices
- **🎨 Modern Interface**: Clean, intuitive design with Tailwind CSS

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTMX for dynamic interactions
- **State Management**: AlpineJS for client-side reactivity
- **Styling**: Tailwind CSS for modern, responsive design
- **Icons**: Emoji for a friendly, universal interface

## Quick Start

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:

   ```bash
   python app.py
   ```

3. **Open your browser** and navigate to `http://localhost:5001`

## How to Use

### 1. Add People

- Go to the "👥 People" tab
- Enter names of people who will be splitting bills
- Click "Add Person" to add them to the group

### 2. Add Expenses

- Switch to the "💳 Expenses" tab
- Enter expense details:
  - Description (e.g., "Alice's Burger")
  - Amount (e.g., 12.50)
  - Who is this expense for
- Click "Add Expense" to record it

### 3. Calculate Split

- Go to the "🧮 Calculate" tab
- Click "Calculate Split" to see:
  - Total amount spent
  - What each person needs to pay for their individual orders

### 4. Pay What You Ordered

Each person pays exactly what they ordered. No splitting or calculations needed!

## Example Scenario

**Group**: Alice, Bob, Charlie

**Expenses**:

- Alice's Burger: $15 (for Alice)
- Bob's Pizza: $18 (for Bob)
- Charlie's Salad: $12 (for Charlie)
- Alice's Drink: $3 (for Alice)

**Total**: $48

**Results**:

- Alice pays: $18 (Burger $15 + Drink $3)
- Bob pays: $18 (Pizza $18)
- Charlie pays: $12 (Salad $12)

**Perfect** - everyone pays only for what they ordered!

## Features in Detail

### Dynamic Interface

- Add/remove people and expenses without page reloads
- Real-time updates using HTMX
- Instant feedback and validation

### Individual Tracking

- Handles any number of people and expenses
- Tracks what each person ordered individually
- Calculates personal totals by summing individual expenses

### User-Friendly Design

- Clean, modern interface
- Color-coded sections for easy navigation
- Responsive design works on all devices
- Emoji icons for intuitive understanding

## Data Storage

Currently uses in-memory storage for simplicity. All data is lost when the server restarts. For production use, consider adding:

- Database integration (SQLite, PostgreSQL, etc.)
- User authentication
- Data persistence
- Session management

## Development

The project structure:

```
bill-splitter/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── templates/
    ├── index.html           # Main page template
    └── partials/
        ├── person_list.html     # People list component
        ├── expense_list.html    # Expenses list component
        ├── split_results.html   # Calculation results
        └── clear_response.html  # Clear confirmation
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application!
