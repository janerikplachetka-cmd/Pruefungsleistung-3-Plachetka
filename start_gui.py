
import sys
import os

# Sicherstellen, dass Python das src-Verzeichnis findet 
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from gui.main_gui import main

if __name__ == "__main__":
    main()