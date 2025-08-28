import os
import csv
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file

# ... (your User class remains the same) ...
class User:
    """A class to represent a survey participant's data."""
    def __init__(self, db_data):
        self.age = db_data.get('age')
        self.gender = db_data.get('gender')
        self.total_income = db_data.get('total_income')
        
        # Flatten the expenses dictionary for CSV
        expenses = db_data.get('expenses', {})
        self.utilities = expenses.get('Utilities', 0)
        self.entertainment = expenses.get('Entertainment', 0)
        self.school_fees = expenses.get('School Fees', 0)
        self.shopping = expenses.get('Shopping', 0)
        self.healthcare = expenses.get('Healthcare', 0)
        
    def to_dict(self):
        """Returns the user data as a dictionary suitable for CSV writing."""
        return {
            'Age': self.age,
            'Gender': self.gender,
            'TotalIncome': self.total_income,
            'Utilities': self.utilities,
            'Entertainment': self.entertainment,
            'SchoolFees': self.school_fees,
            'Shopping': self.shopping,
            'Healthcare': self.healthcare
        }


def process_data_to_csv():
    """Fetches data from MongoDB, processes it, and saves to a CSV file."""
    # --- Connect to MongoDB using environment variable ---
    MONGO_URI = os.environ.get('MONGO_URI')
    if not MONGO_URI:
        raise Exception("MONGO_URI environment variable not set!")
        
    client = MongoClient(MONGO_URI)
    db = client.healthcare_db
    collection = db.surveys

    # ... (the rest of your processing logic remains the same) ...
    all_surveys = list(collection.find({}))
    
    if not all_surveys:
        print("No data found in the database.")
        return

    print(f"Found {len(all_surveys)} surveys to process.")

    headers = ['Age', 'Gender', 'TotalIncome', 'Utilities', 'Entertainment', 'SchoolFees', 'Shopping', 'Healthcare']
    
    with open('survey_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        
        for data in all_surveys:
            user = User(data)
            writer.writerow(user.to_dict())
            
    print("Successfully exported data to survey_data.csv")

if __name__ == '__main__':
    process_data_to_csv()