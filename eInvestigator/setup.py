import importlib
import subprocess
import platform

def check_and_install_packages():
    packages = ['pinecone', 'streamlit', 'google.generativeai', 'sentence_transformers', 'numpy']
    for package in packages:
        if importlib.util.find_spec(package) is None:
            print(f"Installing {package}...")
            subprocess.check_call([pip_executable(), "-q", "install", package])
            print(f"{package} installed.")
        else:
            print(f"{package} is already installed.")

def pip_executable():
    return "pip" if platform.system() == "Windows" else "pip3"




    
