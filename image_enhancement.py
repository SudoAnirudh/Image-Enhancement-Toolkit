import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFileDialog, QPushButton, QSlider
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt

class ImageEnhancementApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Image Enhancement ToolKit")
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()
        
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.image_label)
        
        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)
        
        self.blur_slider = QSlider(Qt.Orientation.Horizontal)
        self.blur_slider.setMinimum(1)
        self.blur_slider.setMaximum(50)
        self.blur_slider.setValue(1)
        self.blur_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.blur_slider.setTickInterval(1)
        self.blur_slider.valueChanged.connect(self.apply_blur)
        self.layout.addWidget(self.blur_slider)
        
        self.save_button = QPushButton("Save Image")
        self.save_button.clicked.connect(self.save_image)
        self.layout.addWidget(self.save_button)
        
        self.setLayout(self.layout)
        
        self.image = None
        self.processed_image = None
        
    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.image = cv2.imread(file_path)
            self.display_image(self.image)
            
    def display_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        bytes_per_line = channel * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_image).scaled(600, 400, Qt.AspectRatioMode.KeepAspectRatio))
        
    def apply_blur(self):
        if self.image is not None:
            ksize = self.blur_slider.value()
            if ksize % 2 == 0:
                ksize += 1
            self.processed_image = cv2.GaussianBlur(self.image, (ksize, ksize), 0)
            self.display_image(self.processed_image)
            
    def save_image(self):
        if self.processed_image is not None:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
            if file_path:
                cv2.imwrite(file_path, self.processed_image)
                print("Image saved successfully!", file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEnhancementApp()
    window.show()
    sys.exit(app.exec())