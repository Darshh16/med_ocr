# src/prescription_reader/utils.py
from PIL import Image, ImageDraw, ImageFont
import os

def create_sample_prescription(output_path, medicines=None):
    """
    Create a sample prescription image with text
    
    Args:
        output_path: Path to save the sample prescription
        medicines: List of medicines to include in the prescription
    
    Returns:
        Path to the created sample prescription
    """
    # Create a sample prescription image with text
    img = Image.new('RGB', (800, 600), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # Try to use a standard font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        # Use default font if arial is not available
        font = ImageFont.load_default()
    
    # Write prescription text
    d.text((50, 50), "Dr. Jane Smith\nCity Medical Center\nLicense: 12345", fill=(0, 0, 0), font=font)
    d.text((50, 150), "Patient: John Doe\nAge: 45\nDate: 2025-03-18", fill=(0, 0, 0), font=font)
    
    # Add medicines to the prescription
    if not medicines:
        medicines = [
            {"name": "Dolo", "dosage": "650mg", "instructions": "1 tablet three times daily after meals"},
            {"name": "Paracetamol", "dosage": "500mg", "instructions": "As needed for fever, not exceeding 4 tablets in 24 hours"}
        ]
    
    rx_text = "Rx:\n\n"
    for i, med in enumerate(medicines, 1):
        rx_text += f"{i}. {med['name']} {med['dosage']} - {med['instructions']}\n\n"
    
    d.text((50, 250), rx_text, fill=(0, 0, 0), font=font)
    d.text((50, 400), "Signature: _________________", fill=(0, 0, 0), font=font)
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save the image
    img.save(output_path)
    
    return output_path

def print_medicine_results(medicines):
    """
    Print the medicines found in a prescription
    
    Args:
        medicines: List of identified medicines
    """
    if medicines:
        print("\nMedicines found in prescription:")
        for medicine in medicines:
            print(f"\nName: {medicine['name'].upper()}")
            print(f"Generic Name: {medicine['generic_name']}")
            print(f"Significance: {medicine['significance']}")
    else:
        print("No medicines found in the prescription or error occurred.")