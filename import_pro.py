#secondary imports
###
try:
    import psutil
    def requirements_status():
        return True
    psutil_lib = True
except:
    def requirements_status():
        return False
    psutil_lib = False
###
try:
    import fpdf
    def reuirements_status():
        return True
    fpdf_lib = True
except:
    def requirements_status():
        return False
    fpdf_lib = False
###
try:
    import PyPDF2 
    def reuirements_status():
        return True
    PyPDF2_lib = True
except:
    def requirements_status():
        return False
    PyPDF2_lib = False
###
try:
    import tabulate 
    def reuirements_status():
        return True
    tabulate_lib = True
except:
    def requirements_status():
        return False
    tabulate_lib = False
###
try:
    import speedtest 
    def reuirements_status():
        return True
    speedtest_lib = True
except:
    def requirements_status():
        return False
    speedtest_lib = False
###
try:
    import cryptography.fernet 
    def reuirements_status():
        return True
    cryptography_lib = True
except:
    def requirements_status():
        return False
    cryptography_lib = False
###
try:
    import phonenumbers 
    def reuirements_status():
        return True
    phonenumbers_lib = True
except:
    def requirements_status():
        return False
    phonenumbers_lib = False
###
try:
    import colorama 
    def reuirements_status():
        return True
    colorama_lib = True
except:
    def requirements_status():
        return False
    colorama_lib = False
###
try:
    import pytube 
    def reuirements_status():
        return True
    pytube_lib = True
except:
    def requirements_status():
        return False
    pytube_lib = False
###
    
#tertiary imports
if (fpdf_lib == True):
    from fpdf import FPDF
if (PyPDF2_lib == True):
    from PyPDF2 import PdfFileReader, PdfFileWriter
if (tabulate_lib == True):
    from tabulate import tabulate
if (cryptography_lib == True):
    from cryptography.fernet import Fernet
if (phonenumbers_lib == True):
    from phonenumbers import carrier
    from phonenumbers import geocoder
if (colorama_lib == True):
    from colorama import init, Fore, Style
if (pytube_lib == True):
    from pytube import YouTube