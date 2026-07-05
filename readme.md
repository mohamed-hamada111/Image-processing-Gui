# Image Processing Application using PyQt5 and OpenCV

## Overview

This project is a desktop image processing application developed using **PyQt5** for the graphical user interface and **OpenCV** for image processing operations.

The application allows users to upload an image and apply a variety of image processing techniques through an interactive GUI.

---

## Features

### Image Management
- Upload image from the local computer.
- Display the selected image.
- Clear the displayed image.

---

## Edge Detection

### 1. Sobel Filter
Detects image edges in both horizontal and vertical directions.

Features:
- Adjustable kernel size using a slider.
- Displays:
  - Sobel X
  - Sobel Y
  - Combined Sobel image

---

### 2. Prewitt Filter
Performs edge detection using Prewitt kernels.

Displays:
- Prewitt X
- Prewitt Y
- Combined result

---

### 3. Canny Edge Detection
Detects edges using the Canny algorithm.

Parameters:
- Lower Threshold
- Upper Threshold

---

### 4. Laplacian Filter
Detects edges using the Laplacian operator.

Features:
- Adjustable kernel size
- Gaussian smoothing before applying Laplacian

---

## Image Smoothing

### Gaussian Blur

Applies Gaussian filtering to reduce image noise.

Parameters:
- Kernel Size
- Sigma X
- Sigma Y

---

## Image Transformations

### Rotation

Rotate the image by any angle.

Features:
- Angle selection using a SpinBox
- Rotation performed using:
  - `cv2.getRotationMatrix2D()`
  - `cv2.warpAffine()`

---

### Flipping

Flip the image in different directions.

Supported modes:
- Horizontal
- Vertical
- Both

Uses:

```python
cv2.flip()
```

---

## Thresholding & Segmentation

### Global Threshold

Binary thresholding using a user-defined threshold value.

---

### Adaptive Threshold

Adaptive thresholding using Gaussian neighborhood.

Parameters:
- Block Size
- Constant (C)

Uses:

```python
cv2.adaptiveThreshold()
```

---

### Otsu Thresholding

Automatic threshold selection using image histogram.

Uses:

```python
cv2.threshold(..., cv2.THRESH_OTSU)
```

---

## Technologies Used

- Python 3.x
- PyQt5
- OpenCV
- NumPy

---

## Project Structure

```
Project/
│
├── main.py
├── ui_mainWindow.py
├── Sobel.py
├── perweit.py
├── Laplace.py
├── Gaussian.py
├── Rotate.py
├── Flip.py
├── Adaptive.py
├── Otsu.py
├── resources/
│
└── README.md
```

---

## Installation

Install the required libraries:

```bash
pip install pyqt5
pip install opencv-python
pip install numpy
```

or

```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
python main.py
```

---

## Application Workflow

1. Launch the application.
2. Click **Upload Image**.
3. Choose an image.
4. Select any image processing operation.
5. Adjust parameters (if available).
6. View the processed result.

---

## OpenCV Functions Used

| Operation | Function |
|-----------|----------|
| Read Image | `cv2.imread()` |
| Color Conversion | `cv2.cvtColor()` |
| Sobel | `cv2.Sobel()` |
| Prewitt | `cv2.filter2D()` |
| Laplacian | `cv2.Laplacian()` |
| Gaussian Blur | `cv2.GaussianBlur()` |
| Canny | `cv2.Canny()` |
| Rotate | `cv2.getRotationMatrix2D()` |
| Affine Transform | `cv2.warpAffine()` |
| Flip | `cv2.flip()` |
| Threshold | `cv2.threshold()` |
| Adaptive Threshold | `cv2.adaptiveThreshold()` |
| Histogram Equalization (Optional) | `cv2.equalizeHist()` |
| CLAHE (Optional) | `cv2.createCLAHE()` |

---

## GUI Components

- QPushButton
- QLabel
- QDialog
- QSlider
- QSpinBox
- QFileDialog

---

## Future Improvements

- Histogram display using Matplotlib
- Brightness and contrast adjustment
- Image resizing
- Image cropping
- Morphological operations
- Fourier Transform
- Hough Line Detection
- Saving processed images
- Undo/Redo functionality
- Dark Mode UI

---

## Author

**Mohamed**

Faculty of Engineering

Image Processing Project using **PyQt5** and **OpenCV**.