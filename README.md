
#  Emotional Attention Tracker

An AI-powered computer vision application that detects faces and eyes in real time to track visual attention and provide insights into user engagement. Built using Python, OpenCV, Haar Cascade classifiers, and Flask, the project demonstrates real-time face and eye detection through a web interface.

---

##  Features

-  **Real-Time Eye Detection** — Detect eyes using OpenCV and Haar Cascade classifiers.
-  **Face Detection** — Identify faces from camera input.
-  **Attention Tracking** — Analyze eye and face detection to support basic attention tracking.
-  **Web Interface** — Access the application through a Flask-powered web interface.
-  **Lightweight Computer Vision** — Uses Haar Cascade models for efficient detection.
-  **Modular Architecture** — Separates tracking logic, utility functions, and web templates.

> **Note:** The current implementation uses face and eye detection as indicators for attention tracking. Face and eye detection alone cannot reliably determine a person's emotions, concentration, or mental state.

---

##  Tech Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Detection Models | Haar Cascade Classifiers |
| Backend | Flask |
| Frontend | HTML Templates |
| Application Type | Real-Time Computer Vision |

---

##  Project Structure

```text
EMOTIONAL-ATTENTION-TRACKER/
│
├── haarcascades/
│   └── # Face and eye detection models
│
├── templates/
│   └── # HTML templates for the web interface
│
├── main.py
│   └── # Flask application entry point
│
├── tracker.py
│   └── # Attention and detection tracking logic
│
├── utils.py
│   └── # Helper functions and utilities
│
├── .gitignore
│   └── # Files and folders excluded from Git
│
└── README.md
    └── # Project documentation
```

---

## ⚙️ Installation and Setup

###  Clone the Repository

```bash
git clone https://github.com/Nivedithagowda2/EMOTIONAL-ATTENTION-TRACKER.git
```

Navigate to the project directory:

```bash
cd EMOTIONAL-ATTENTION-TRACKER
```

> **Note:** Update the repository URL if your GitHub repository uses a different name or URL.

---

###  Create a Virtual Environment (Recommended)

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

---

###  Install Dependencies

Install the required Python packages:

```bash
pip install flask opencv-python
```

If your project includes a `requirements.txt` file, use:

```bash
pip install -r requirements.txt
```

---

##  Run the Application

Start the Flask application:

```bash
python main.py
```

Once the application starts, open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

##  How It Works

```text
Camera Input
     │
     ▼
OpenCV Frame Processing
     │
     ▼
Face Detection
     │
     ▼
Eye Detection
     │
     ▼
Attention Tracking Logic
     │
     ▼
Flask Web Interface
     │
     ▼
Real-Time Results
```

### Processing Workflow

1. **Capture Input:** Obtain frames from the camera or another supported input source.
2. **Face Detection:** Use Haar Cascade classifiers to locate faces.
3. **Eye Detection:** Detect eyes within the detected face regions.
4. **Tracking Analysis:** Process detection results using the tracking logic.
5. **Web Display:** Present the results through the Flask application.

---

##  Application Preview

Add screenshots or a demo video of your application here.

```markdown
![Application Screenshot](screenshots/demo.png)
```

You can replace the example image path with the actual screenshot stored in your repository.

---

##  Future Improvements

- [ ] Improve attention tracking using additional visual features.
- [ ] Add head pose estimation for more detailed attention analysis.
- [ ] Integrate facial expression recognition with a suitable model.
- [ ] Add real-time tracking dashboards and session summaries.
- [ ] Improve robustness under different lighting conditions.
- [ ] Add configurable detection thresholds.
- [ ] Support session-based attention statistics.
- [ ] Add automated testing for tracking and utility functions.

---

##  Privacy and Responsible Use

- Process camera data responsibly and inform users when camera access is active.
- Avoid storing facial images or video without appropriate consent.
- Treat attention indicators as approximate computer vision signals, not definitive measurements of a person's mental state or emotions.
- Avoid using the system to make high-stakes decisions about individuals.

---

##  Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Commit your updates.
5. Open a pull request.

Example:

```bash
git checkout -b feature/improve-tracking
git add .
git commit -m "Improve attention tracking"
git push origin feature/improve-tracking
```

---

## 👤 Author

**Niveditha**

- GitHub: [Nivedithagowda2](https://github.com/Nivedithagowda2)

---



Contributions, suggestions, and feedback are welcome.
