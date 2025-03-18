# src/prescription_reader/preprocessing.py
import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess the prescription image for better OCR
    
    Args:
        image_path: Path to the prescription image
        
    Returns:
        Preprocessed image
    """
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not read image from {image_path}")
        
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to handle different lighting conditions
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Apply noise reduction
    denoised = cv2.fastNlMeansDenoising(thresh, None, 10, 7, 21)
    
    # Apply dilation to make text more prominent
    kernel = np.ones((1, 1), np.uint8)
    dilated = cv2.dilate(denoised, kernel, iterations=1)
    
    return dilated

def enhance_image(image):
    """
    Apply additional enhancements to improve OCR accuracy
    
    Args:
        image: Input image
        
    Returns:
        Enhanced image
    """
    # Apply adaptive thresholding
    enhanced = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    
    # Apply morphological operations
    kernel = np.ones((1, 1), np.uint8)
    enhanced = cv2.morphologyEx(enhanced, cv2.MORPH_CLOSE, kernel)
    
    return enhanced