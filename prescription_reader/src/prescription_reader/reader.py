# src/prescription_reader/reader.py
import re
import pytesseract
from .preprocessing import preprocess_image
from .medicine_db import MedicineDatabase

class PrescriptionReader:
    def __init__(self, tesseract_path=None, medicine_db_path=None):
        """
        Initialize the prescription reader
        
        Args:
            tesseract_path: Path to tesseract executable if not in PATH
            medicine_db_path: Path to the medicine database JSON file
        """
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
            
        # Initialize medicine database
        self.medicine_db = MedicineDatabase(medicine_db_path)
        
    def extract_text(self, preprocessed_img):
        """
        Extract text from preprocessed image using OCR
        
        Args:
            preprocessed_img: Preprocessed image
            
        Returns:
            Extracted text
        """
        # Use Tesseract to extract text
        config = '--psm 6'  # Assume a single block of text
        text = pytesseract.image_to_string(preprocessed_img, config=config)
        return text
    
    def identify_medicines(self, text):
        """
        Identify medicine names from extracted text
        
        Args:
            text: Extracted text from prescription
            
        Returns:
            List of identified medicines with their details
        """
        # Convert text to lowercase for easier matching
        text_lower = text.lower()
        
        # Find all medicine matches
        found_medicines = []
        
        for medicine_name, details in self.medicine_db.get_all_medicines().items():
            # Look for the medicine name as a word
            pattern = r'\b' + re.escape(medicine_name) + r'\b'
            if re.search(pattern, text_lower):
                found_medicines.append({
                    "name": medicine_name,
                    "generic_name": details["generic_name"],
                    "significance": details["significance"]
                })
                
        return found_medicines
    
    def process_prescription(self, image_path):
        """
        Process prescription image and extract medicine information
        
        Args:
            image_path: Path to prescription image
            
        Returns:
            List of identified medicines
        """
        try:
            # Preprocess image
            preprocessed = preprocess_image(image_path)
            
            # Extract text
            text = self.extract_text(preprocessed)
            
            # Identify medicines
            medicines = self.identify_medicines(text)
            
            return medicines
        except Exception as e:
            print(f"Error processing prescription: {e}")
            return []