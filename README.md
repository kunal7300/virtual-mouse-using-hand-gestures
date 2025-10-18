

# 🖐️ AI Virtual Mouse – Hand Gesture Controlled Cursor

Control your computer’s mouse using hand gestures through your webcam!
This project uses **Python**, **OpenCV**, **MediaPipe**, and **PyAutoGUI** to recognize hand movements in real time and simulate mouse actions such as **cursor movement**, **clicks**, and **exit**.

---

## 🚀 Features

* Real-time **hand tracking** using MediaPipe
* Move cursor using your **index finger**
* **Left click** → index + middle fingers up
* **Right click** → only index finger up
* **Exit** → make a fist (no fingers up)
* Works completely **contactless**, ideal for accessibility or touchless interfaces

---

## 🧠 Tech Stack

| Component     | Description                                                      |
| ------------- | ---------------------------------------------------------------- |
| **Language**  | Python 3.12                                                      |
| **Libraries** | OpenCV, MediaPipe, PyAutoGUI                                     |
| **Concepts**  | Computer Vision, Hand Tracking, Human-Computer Interaction (HCI) |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone (https://github.com/kunal7300/virtual-mouse-using-hand-gestures.git)
cd virtual-mouse-using-hand-gestures
```

### 2. Install dependencies

Make sure you have **Python 3.12** (MediaPipe is not yet compatible with 3.13).

Then install the required libraries:

```bash
python -m pip install --upgrade pip
python -m pip install opencv-python mediapipe pyautogui
```

> 💡 If you use the `py` launcher on Windows:
>
> ```bash
> py -3.12 -m pip install opencv-python mediapipe pyautogui
> ```

---

## ▶️ Usage

1. Run the Python script:

   ```bash
    py -3.12 main.py //version filename.py

   ```
2. Allow camera access when prompted.
3. Perform gestures in front of the webcam:

| Gesture                         | Action       |
| ------------------------------- | ------------ |
| ☝️ One finger (index)           | Right Click  |
| ✌️ Two fingers (index + middle) | Left Click   |
| ✊ Fist                          | Exit program |

Press **Q** to quit manually.

---

## 🧩 Code Overview

The script:

* Initializes MediaPipe’s **Hand Tracking** model.
* Tracks hand landmarks (fingertip positions).
* Maps the index finger’s position to the screen coordinates.
* Detects gesture patterns based on the number of fingers raised.
* Uses PyAutoGUI to trigger mouse events.

---



## ⚠️ Requirements

* Webcam
* Windows/macOS/Linux
* Python 3.12
* Stable lighting conditions for best accuracy

---

 contact

🌐 (https://github.com/kunal7300)
📧 (kunal39190@gmail.com)


### 💬 Contributions

Pull requests are welcome!
If you find a bug or have an idea for improvement, feel free to **open an issue** or **submit a PR**.

---
