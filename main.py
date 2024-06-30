import sys
from PySide6.QtWidgets import QApplication
from window import ImageViewer

# def main():
    # Créer l'application Qt
app = QApplication(sys.argv)

    # Créer une instance de la fenêtre principale
viewer = ImageViewer()
viewer.show()

    # Exécuter la boucle principale de l'application
sys.exit(app.exec())
