from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QFileDialog, QErrorMessage, \
    QInputDialog
from PySide6.QtGui import QPixmap, QImage, QColor
from decoder import Decoder
from encoder import Encoder
from pathlib import Path


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 200, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        self.open_button = QPushButton("Open Image")
        self.open_button.clicked.connect(self.open_image)
        self.layout.addWidget(self.open_button)

        self.save_button = QPushButton("Save Image")
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setEnabled(False)
        self.layout.addWidget(self.save_button)

        self.image_path = None

    def open_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("ULBMP Images (*.ulbmp)")
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec():
            self.image_path = file_dialog.selectedFiles()[0]

            try:
                decoder = Decoder()
              
                image = decoder.load_from(self.image_path)
                
                listt = []

                for pixel in image.pixels:
                    listt.append((pixel.getRouge(), pixel.getGreen(), pixel.getBlue()))

                qimage = QImage(image.width, image.height, QImage.Format_RGB888)
                for y in range(image.height):
                    for x in range(image.width):
                        pixel_color = QColor(*listt[y * image.width + x])
                        qimage.setPixelColor(x, y, pixel_color)

                pixmap = QPixmap.fromImage(qimage)
                self.image_label.setPixmap(pixmap)
                self.save_button.setEnabled(True)
                self.resize(pixmap.width(), pixmap.height())

            except Exception as e:
                error_dialog = QErrorMessage(self)
                error_dialog.showMessage(f"Error opening image: {str(e)}")
                error_dialog.exec()

    def save_image(self):

        if self.image_path:

            new_filename, ok_filename = QInputDialog.getText(self, "Save Image", "Enter new filename:")

            if ok_filename:
                version, ok_version = QInputDialog.getInt(self, "Save Image", "Enter version:", 2, 1)
                if ok_version:
                    try:

                        dec = Decoder()
                        imag = dec.load_from(self.image_path)
                        encoder = Encoder(imag, version)

                        encoder.save_to(new_filename)
    
                    except Exception as e:
                        error_dialog = QErrorMessage(self)
                        error_dialog.showMessage(f"Error saving image: {str(e)}")
                        error_dialog.exec()
