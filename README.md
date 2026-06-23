# project-AMULET // Raspberry Pi Core 🛡️
**Advanced Monitor & Utility for Logical Encryption & Telemetry**

This is the Raspberry Pi Python version of **project-AMULET**. It controls local hardware pins on a Raspberry Pi (e.g., active shield status LEDs) while running an active threat deflection and telemetry monitoring loop.

---

## How It Works
- **Windows Simulation Mode**: If run on a Windows machine (or non-Pi hardware), the script automatically detects the environment, bypasses the GPIO pin initialization, and runs in **Simulation Mode** using custom terminal print fallbacks.
- **Raspberry Pi Hardware Mode**: When run on a Raspberry Pi with the necessary libraries installed, it initializes pin controls to physical GPIO pins to control hardware indicator components.

---

## Project Structure
- `main.py`: The entry point script with simulation fallback.
- `requirements.txt`: Python package list (defines `gpiozero` for hardware management).
- `.gitignore`: Configured to ignore python compilation caches, local environments, and log files.

---

## Running Locally (Windows Simulation)
1. Ensure Python is installed.
2. Open your terminal in this directory and execute the script:
   ```bash
   python main.py
   ```
3. Watch the mock telemetry data streams. Press **Ctrl+C** to safely exit.

---

## Running on your Raspberry Pi
To run this script on your Raspberry Pi:

1. **Transfer the files**:
   Clone this repository directly onto your Pi:
   ```bash
   git clone https://github.com/unity-guy/project-AMULET.git
   cd project-AMULET
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Execute**:
   ```bash
   python main.py
   ```
4. **Hardware indicator**: Connect an LED to GPIO pin 17 to see the Sentinel Shield scanning indicator blink and respond to deflection levels!
