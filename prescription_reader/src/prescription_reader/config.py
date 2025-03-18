# src/prescription_reader/config.py
import os

# Default paths
DEFAULT_DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                               'data', 'medicine_database.json')

# OCR configuration
OCR_CONFIG = {
    'psm': 6,  # Page segmentation mode
    'oem': 3,  # OCR Engine mode
    'lang': 'eng'  # Language
}

# Image preprocessing parameters
PREPROCESSING = {
    'denoise_h': 10,
    'denoise_template_window_size': 7,
    'denoise_search_window_size': 21,
    'dilation_kernel_size': (1, 1),
    'dilation_iterations': 1
}

# Medicine pattern matching
PATTERN_MATCHING = {
    'use_regex': True,
    'case_sensitive': False,
    'whole_word': True
}