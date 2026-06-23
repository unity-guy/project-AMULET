import os
import time
import sys
import random
from dotenv import load_dotenv

# Load configurations from .env file if it exists
load_dotenv()

# Attempt to load Raspberry Pi GPIO libraries
# If running on Windows, it will fallback to Simulation Mode
IS_RASPBERRY_PI = False
try:
    from gpiozero import LED
    IS_RASPBERRY_PI = True
except (ImportError, ModuleNotFoundError):
    # Mocking GPIO classes for local development/testing on Windows
    class MockGPIO:
        def __init__(self, pin):
            self.pin = pin
            self.is_active = False

        def on(self):
            self.is_active = True
            print(f"[SIMULATOR] LED on Pin {self.pin} -> ON (Solid)")

        def off(self):
            self.is_active = False
            print(f"[SIMULATOR] LED on Pin {self.pin} -> OFF")

        def blink(self, on_time=0.5, off_time=0.5, n=None, background=True):
            print(f"[SIMULATOR] LED on Pin {self.pin} -> BLINKING (on: {on_time}s, off: {off_time}s)")
            
    LED = MockGPIO
    print("[SYSTEM] Running in WINDOWS SIMULATION MODE (No Pi hardware detected).")

# Retrieve configuration parameters from environment variables
SHIELD_LED_PIN = int(os.getenv("SHIELD_LED_PIN", 17))
TELEMETRY_INTERVAL = float(os.getenv("TELEMETRY_INTERVAL", 2.0))
DEFLECTION_ALERT_THRESHOLD = int(os.getenv("DEFLECTION_ALERT_THRESHOLD", 85))

def init_hardware():
    """Initializes LEDs and sensors."""
    print(f"[AMULET] Initializing pin controls (Target Pin: GPIO {SHIELD_LED_PIN})...")
    shield_led = LED(SHIELD_LED_PIN)
    return shield_led

def run_telemetry_loop(shield_led):
    """Simulates active telemetry logging and Pi state updates."""
    print("\n[AMULET] Active Threat Deflection Loop started.")
    print(f"Settings: Interval={TELEMETRY_INTERVAL}s | Alert Threshold={DEFLECTION_ALERT_THRESHOLD}%")
    print("Press Ctrl+C to stop the script.\n")
    
    shield_led.blink(on_time=0.2, off_time=0.8) # Blink pattern to show standby/scanning
    
    try:
        while True:
            # Generate dummy telemetry reading
            freq = random.randint(70, 95)
            deflection = random.randint(80, 99)
            
            # Print live console output
            print(f"[TELEMETRY] Frequency: {freq} Hz | Shield Deflection: {deflection}% | Target: STABLE")
            
            # Simple simulation: if deflection gets critically low, pulse the LED faster
            if deflection < DEFLECTION_ALERT_THRESHOLD:
                print(f"[ALERT] Deflection below {DEFLECTION_ALERT_THRESHOLD}%! Overclocking LED warning.")
                shield_led.on()
                time.sleep(0.5)
                shield_led.off()
            
            time.sleep(TELEMETRY_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n[AMULET] Stopping telemetry loop...")
    finally:
        shield_led.off()
        print("[AMULET] Controls released. Exiting clean.")

if __name__ == "__main__":
    print("==================================================")
    print("      project-AMULET // Raspberry Pi Core        ")
    print("==================================================")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Platform: {sys.platform}")
    print(f"Host is Raspberry Pi: {IS_RASPBERRY_PI}")
    print("==================================================")
    
    led_indicator = init_hardware()
    run_telemetry_loop(led_indicator)
