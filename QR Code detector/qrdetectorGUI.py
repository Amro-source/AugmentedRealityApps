
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

class QRCodeDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Detector")
        self.image = None

        # Create a button to load an image
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        # Create a label to display the image
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Create a button to detect QR codes
        self.detect_button = tk.Button(root, text="Detect QR Codes", command=self.detect_qr_codes)
        self.detect_button.pack()

    def load_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png .bmp")])

        # Load the selected image
        self.image = cv2.imread(file_path)

        # Display the loaded image
        self.display_image()

    def detect_qr_codes(self):
        # Detect QR codes in the loaded image
        if self.image is not None:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            qr_codes, decoded_info, _ = cv2.QRCodeDetector().detectAndDecode(gray)

            # Display the detected QR codes
            if qr_codes is not None:
                for i, qr_code in enumerate(qr_codes):
                    cv2.drawContours(self.image, [qr_code], -1, (0, 255, 0), 2)

                self.display_image()

    def display_image(self):
        # Convert the image to RGB format
        rgb_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        # Display the image
        self.image_label.config(image=tk.PhotoImage(image=tk.BitmapImage(data=cv2.imencode('.png', rgb_image)[1].tobytes())))

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeDetectorApp(root)
    root.mainloop()
