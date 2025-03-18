# examples/basic_usage.py
import os
import sys

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.prescription_reader import PrescriptionReader, create_sample_prescription, print_medicine_results

def main():
    # Create a sample prescription
    sample_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_prescriptions', 'sample1.jpg')
    print(f"Creating sample prescription at {sample_path}")
    create_sample_prescription(sample_path)
    
    # Initialize reader
    reader = PrescriptionReader()
    
    # Process the sample prescription
    print(f"Processing prescription: {sample_path}")
    results = reader.process_prescription(sample_path)
    
    # Print results
    print_medicine_results(results)

if __name__ == "__main__":
    main()