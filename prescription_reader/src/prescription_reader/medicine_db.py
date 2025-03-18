# src/prescription_reader/medicine_db.py
import json
import os

class MedicineDatabase:
    def __init__(self, db_path=None):
        """
        Initialize the medicine database
        
        Args:
            db_path: Path to the JSON medicine database file
        """
        self.db = {}
        if db_path and os.path.exists(db_path):
            self.load_database(db_path)
        else:
            # Default database
            self.db = {
                "dolo": {
                    "generic_name": "Paracetamol",
                    "significance": "Pain reliever and fever reducer. Used for headaches, muscle aches, backaches, colds, and fevers."
                },
                "paracetamol": {
                    "generic_name": "Paracetamol",
                    "significance": "Pain reliever and fever reducer. Used for headaches, muscle aches, backaches, colds, and fevers."
                },
                "crocin": {
                    "generic_name": "Paracetamol",
                    "significance": "Pain reliever and fever reducer. Used for treating mild to moderate pain."
                },
                "aspirin": {
                    "generic_name": "Acetylsalicylic acid",
                    "significance": "Pain reliever, fever reducer, and anti-inflammatory. Also used as a blood thinner."
                },
                "azithromycin": {
                    "generic_name": "Azithromycin",
                    "significance": "Antibiotic used to treat infections caused by bacteria."
                }
            }
    
    def load_database(self, db_path):
        """
        Load medicine database from JSON file
        
        Args:
            db_path: Path to the JSON medicine database file
        """
        try:
            with open(db_path, 'r') as f:
                self.db = json.load(f)
        except Exception as e:
            print(f"Error loading medicine database: {e}")
            # Fall back to default database
            self.db = {}
    
    def save_database(self, db_path):
        """
        Save medicine database to JSON file
        
        Args:
            db_path: Path to save the JSON medicine database file
        """
        try:
            with open(db_path, 'w') as f:
                json.dump(self.db, f, indent=4)
        except Exception as e:
            print(f"Error saving medicine database: {e}")
    
    def get_medicine_info(self, medicine_name):
        """
        Get information about a medicine
        
        Args:
            medicine_name: Name of the medicine
            
        Returns:
            Dictionary containing medicine information or None if not found
        """
        medicine_name = medicine_name.lower()
        return self.db.get(medicine_name)
    
    def add_medicine(self, name, generic_name, significance):
        """
        Add a new medicine to the database
        
        Args:
            name: Medicine name
            generic_name: Generic name of the medicine
            significance: Significance/use of the medicine
        """
        name = name.lower()
        self.db[name] = {
            "generic_name": generic_name,
            "significance": significance
        }
    
    def get_all_medicines(self):
        """
        Get all medicines in the database
        
        Returns:
            Dictionary of all medicines
        """
        return self.db