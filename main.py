#Instalator DCS Bios by Eldritch_514 WMFA117  

import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtGui import QPixmap

# Funkcja do wyszukiwania instalacji DCS Bios na istniejących dyskach
def find_installation_paths():
    # Lista dostępnych dysków
    drives = [drive for drive in os.listdir('/') if os.path.exists(os.path.join('/', drive))]
    
    found_paths = []

    for drive in drives:
        possible_path = os.path.join(drive, "Program Files", "Eagle Dynamics", "DCS")
        if os.path.exists(possible_path):
            found_paths.append(possible_path)
        
        possible_path = os.path.join(drive, "Program Files", "Eagle Dynamics", "DCS OpenBeta")
        if os.path.exists(possible_path):
            found_paths.append(possible_path)

        possible_path = os.path.join(drive, "Users", os.getlogin(), "Saved Games", "DCS")
        if os.path.exists(possible_path):
            found_paths.append(possible_path)

        possible_path = os.path.join(drive, "Users", os.getlogin(), "Saved Games", "DCS OpenBeta")
        if os.path.exists(possible_path):
            found_paths.append(possible_path)

    if found_paths:
        result_label.setText("Znaleziono następujące ścieżki instalacji na dostępnych dyskach:")
        paths_text.setPlainText("\n".join(found_paths))
    else:
        result_label.setText("Nie znaleziono żadnych ścieżek instalacji na dostępnych dyskach.")
        open_explorer_button.setEnabled(True)

# Funkcja do otwierania eksploratora plików
def open_file_explorer():
    folder = os.path.join(os.environ['USERPROFILE'], 'Saved Games')
    if os.path.exists(folder):
        file_dialog = QFileDialog()
        file_dialog.setDirectory(folder)
        file_dialog.exec_()

# Tworzenie głównego okna
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Instalacja DCS Bios")

layout = QVBoxLayout()

# Dodawanie obrazka
image_label = QLabel()
pixmap = QPixmap("/mnt/chromeos/MyFiles/Downloads/Screenshot 2023-02-18 19.06.12.png")  # Podaj ścieżkę do swojego obrazka
image_label.setPixmap(pixmap)
layout.addWidget(image_label)

# Etykieta z wynikami
result_label = QLabel("")
layout.addWidget(result_label)

# Przycisk "Szukaj"
find_button = QPushButton("Szukaj")
find_button.clicked.connect(find_installation_paths)
layout.addWidget(find_button)

# Przycisk "Otwórz eksplorator plików"
open_explorer_button = QPushButton("Otwórz eksplorator plików")
open_explorer_button.clicked.connect(open_file_explorer)
open_explorer_button.setEnabled(False)
layout.addWidget(open_explorer_button)

# Pole tekstowe na ścieżki
paths_text = QTextEdit()
paths_text.setReadOnly(True)
layout.addWidget(paths_text)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())





