# setup.py
from setuptools import setup, find_packages

setup(
    name="prescription_reader",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "pytesseract>=0.3.8",
        "Pillow>=8.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for reading and analyzing medical prescriptions using OCR",
    keywords="prescription, ocr, medical, opencv",
    python_requires=">=3.6",
)