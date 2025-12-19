#!/usr/bin/env python3
"""
GreenStore Setup Script
Initializes the database and sets up the development environment
"""

import os
import sys
import subprocess
import sqlite3
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")

def check_python_version():
    """Check if Python version is compatible"""
    print_header("Checking Python Version")
    
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def install_dependencies():
    """Install Python dependencies"""
    print_header("Installing Python Dependencies")
    
    requirements_file = Path("backend/python/requirements.txt")
    
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def setup_database():
    """Setup SQLite database"""
    print_header("Setting Up Database")
    
    db_path = Path("backend/python/greenstore.db")
    schema_path = Path("database/schema.sql")
    seed_path = Path("database/seed_data.sql")
    
    # Remove existing database
    if db_path.exists():
        print("⚠️  Existing database found. Removing...")
        db_path.unlink()
    
    # Create new database
    print("📦 Creating database...")
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Execute schema
    if schema_path.exists():
        print("📋 Loading schema...")
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema_sql = f.read()
            cursor.executescript(schema_sql)
        print("✅ Schema loaded")
    else:
        print("❌ Schema file not found")
        return False
    
    # Execute seed data
    if seed_path.exists():
        print("🌱 Loading seed data...")
        with open(seed_path, 'r', encoding='utf-8') as f:
            seed_sql = f.read()
            cursor.executescript(seed_sql)
        print("✅ Seed data loaded")
    else:
        print("⚠️  Seed data file not found (optional)")
    
    conn.commit()
    conn.close()
    
    print(f"✅ Database created at: {db_path.absolute()}")
    return True

def create_env_file():
    """Create .env file for configuration"""
    print_header("Creating Environment Configuration")
    
    env_path = Path("backend/python/.env")
    
    if env_path.exists():
        print("⚠️  .env file already exists")
        return True
    
    env_content = """# GreenStore Environment Configuration

# Database
DATABASE_URL=sqlite:///./greenstore.db

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=True

# CORS
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Security (change in production!)
SECRET_KEY=your-secret-key-here-change-in-production
"""
    
    with open(env_path, 'w') as f:
        f.write(env_content)
    
    print(f"✅ Environment file created at: {env_path.absolute()}")
    return True

def print_next_steps():
    """Print next steps for the user"""
    print_header("Setup Complete! 🎉")
    
    print("Next steps:")
    print("\n1. Start the Python backend:")
    print("   cd backend/python")
    print("   uvicorn app.main:app --reload --port 8000")
    
    print("\n2. Start the frontend (in a new terminal):")
    print("   cd frontend")
    print("   python -m http.server 3000")
    print("   # Or use PHP:")
    print("   php -S localhost:3000")
    
    print("\n3. Open your browser:")
    print("   http://localhost:3000")
    
    print("\n4. API Documentation:")
    print("   http://localhost:8000/docs")
    
    print("\n5. Alternative: Use PHP backend:")
    print("   cd backend/php")
    print("   php -S localhost:8000")
    
    print("\n" + "=" * 60)
    print("  Happy coding! 🚀")
    print("=" * 60 + "\n")

def main():
    """Main setup function"""
    print("\n")
    print("  ╔═══════════════════════════════════════════════════════╗")
    print("  ║                                                       ║")
    print("  ║           🌱 GreenStore Setup Wizard 🌱              ║")
    print("  ║                                                       ║")
    print("  ╚═══════════════════════════════════════════════════════╝")
    
    # Change to project root directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Run setup steps
    check_python_version()
    
    if not install_dependencies():
        print("\n⚠️  Setup incomplete. Please fix errors and try again.")
        sys.exit(1)
    
    if not setup_database():
        print("\n⚠️  Setup incomplete. Please fix errors and try again.")
        sys.exit(1)
    
    create_env_file()
    
    print_next_steps()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Setup failed with error: {e}")
        sys.exit(1)
