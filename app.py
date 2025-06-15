from flask import Flask, render_template, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage (in production, use a database)
people = []
expenses = []

@app.route('/')
def index():
    return render_template('index.html', people=people, expenses=expenses)

@app.route('/add_person', methods=['POST'])
def add_person():
    name = request.form.get('name', '').strip()
    if name and name not in [p['name'] for p in people]:
        person = {
            'id': str(uuid.uuid4()),
            'name': name
        }
        people.append(person)
        return render_template('partials/person_list.html', people=people)
    return '', 400

@app.route('/remove_person/<person_id>', methods=['DELETE'])
def remove_person(person_id):
    global people
    people = [p for p in people if p['id'] != person_id]
    return render_template('partials/person_list.html', people=people)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    description = request.form.get('description', '').strip()
    amount = request.form.get('amount', '').strip()
    for_person = request.form.get('for_person', '').strip()
    
    if not (description and amount and for_person):
        return '', 400
    
    try:
        amount = float(amount)
        if amount <= 0:
            return '', 400
    except ValueError:
        return '', 400
    
    expense = {
        'id': str(uuid.uuid4()),
        'description': description,
        'amount': amount,
        'for_person': for_person,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    expenses.append(expense)
    return render_template('partials/expense_list.html', expenses=expenses)

@app.route('/remove_expense/<expense_id>', methods=['DELETE'])
def remove_expense(expense_id):
    global expenses
    expenses = [e for e in expenses if e['id'] != expense_id]
    return render_template('partials/expense_list.html', expenses=expenses)

@app.route('/calculate_split', methods=['POST'])
def calculate_split():
    if not people or not expenses:
        return render_template('partials/split_results.html', results=[], error="Need at least one person and one expense")
    
    # Calculate total expenses
    total_amount = sum(expense['amount'] for expense in expenses)
    
    # Calculate what each person owes based on their individual expenses
    person_totals = {person['name']: 0 for person in people}
    for expense in expenses:
        person_totals[expense['for_person']] += expense['amount']
    
    results = {
        'total_amount': round(total_amount, 2),
        'person_totals': {name: round(amount, 2) for name, amount in person_totals.items()}
    }
    
    return render_template('partials/split_results.html', results=results)

@app.route('/clear_all', methods=['POST'])
def clear_all():
    global people, expenses
    people = []
    expenses = []
    return render_template('partials/clear_response.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001) 