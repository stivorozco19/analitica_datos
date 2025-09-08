#!/usr/bin/env python3
"""
Automated setup script for Data Analytics Workshop
Author: Julian Eduardo Garzon Giraldo, MsC
"""

import os
import subprocess
import sys
import platform

def run_command(command, description, shell=False):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        if shell:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
        else:
            result = subprocess.run(command.split(), capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ {description} completed successfully!")
            return True
        else:
            print(f"❌ Error in {description}: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Exception in {description}: {str(e)}")
        return False

def main():
    """Main setup function"""
    print("🚀 Data Analytics Workshop - Automated Setup")
    print("=" * 50)
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8+ required. Current version:", sys.version)
        sys.exit(1)
    
    print(f"✅ Python {python_version.major}.{python_version.minor} detected")
    
    # Detect OS
    current_os = platform.system()
    print(f"🖥️  Operating System: {current_os}")
    
    # Set up commands based on OS
    if current_os == "Windows":
        python_cmd = "python"
        activate_cmd = "data_analytics_env\\Scripts\\activate"
        venv_activate = "data_analytics_env\\Scripts\\activate.bat"
    else:
        python_cmd = "python3"
        activate_cmd = "source data_analytics_env/bin/activate"
        venv_activate = "data_analytics_env/bin/activate"
    
    # Step 1: Create virtual environment
    venv_command = f"{python_cmd} -m venv data_analytics_env"
    if not run_command(venv_command, "Creating virtual environment"):
        print("❌ Failed to create virtual environment. Please check your Python installation.")
        sys.exit(1)
    
    # Step 2: Upgrade pip in virtual environment
    if current_os == "Windows":
        pip_upgrade_cmd = "data_analytics_env\\Scripts\\python.exe -m pip install --upgrade pip"
    else:
        pip_upgrade_cmd = "data_analytics_env/bin/python -m pip install --upgrade pip"
    
    run_command(pip_upgrade_cmd, "Upgrading pip in virtual environment")
    
    # Step 3: Install requirements
    if current_os == "Windows":
        install_cmd = "data_analytics_env\\Scripts\\pip.exe install -r requirements.txt"
    else:
        install_cmd = "data_analytics_env/bin/pip install -r requirements.txt"
    
    if not run_command(install_cmd, "Installing required packages"):
        print("❌ Failed to install packages. Please check requirements.txt file exists.")
        sys.exit(1)
    
    # Step 4: Install Jupyter kernel
    if current_os == "Windows":
        kernel_cmd = "data_analytics_env\\Scripts\\python.exe -m ipykernel install --user --name=data_analytics_env --display-name=\"Data Analytics Workshop\""
    else:
        kernel_cmd = "data_analytics_env/bin/python -m ipykernel install --user --name=data_analytics_env --display-name=\"Data Analytics Workshop\""
    
    run_command(kernel_cmd, "Installing Jupyter kernel", shell=True)
    
    # Success message
    print("\n" + "=" * 60)
    print("🎉 SETUP COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\n📋 Next Steps:")
    print("1. Activate your virtual environment:")
    
    if current_os == "Windows":
        print("   data_analytics_env\\Scripts\\activate")
    else:
        print("   source data_analytics_env/bin/activate")
    
    print("\n2. Start Jupyter Notebook:")
    print("   jupyter notebook")
    
    print("\n3. Open 'financial_analysis_workshop.ipynb'")
    
    print("\n4. In Jupyter, select kernel: Kernel → Change Kernel → Data Analytics Workshop")
    
    print("\n5. Run the first cell to verify installation")
    
    print(f"\n💡 Your virtual environment is located at: {os.path.abspath('data_analytics_env')}")
    print("\n🎯 You're ready to start the workshop! Good luck!")

if __name__ == "__main__":
    main()