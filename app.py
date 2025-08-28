import os
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file

app = Flask(__name__)

# --- Connect to MongoDB using environment variable ---
MONGO_URI = os.environ.get('MONGO_URI')
if not MONGO_URI:
    raise Exception("MONGO_URI environment variable not set!")
    
client = MongoClient(MONGO_URI)
db = client.healthcare_db
collection = db.surveys

# ... (the rest of your app.py code remains the same) ...

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        # 1. Collect basic user details
        user_data = {
            'age': int(request.form.get('age')),
            'gender': request.form.get('gender'),
            'total_income': float(request.form.get('total_income')),
            'expenses': {}
        }
        
        # 2. Collect expense data
        checked_expenses = request.form.getlist('expenses') 
        
        for expense in checked_expenses:
            amount_key = f"amount_{expense.lower().replace(' ', '_')}"
            amount_value = request.form.get(amount_key)
            if amount_value:
                user_data['expenses'][expense] = float(amount_value)

        # 3. Insert the data into MongoDB
        collection.insert_one(user_data)
        message = "Thank you! Your survey has been submitted."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)