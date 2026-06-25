import os
import sys

# Add the parent directory to the path so we can import main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

def test_environment_defaults():
    """Verify that default settings or env variables are correctly parsed."""
    assert isinstance(main.SHIELD_LED_PIN, int)
    assert isinstance(main.TELEMETRY_INTERVAL, float)
    assert isinstance(main.DEFLECTION_ALERT_THRESHOLD, int)

def test_mock_gpio_led():
    """Verify that the Mock LED has the expected methods and active states."""
    led = main.LED(17)
    
    # Verify properties exist
    assert hasattr(led, 'is_active')
    assert hasattr(led, 'on')
    assert hasattr(led, 'off')
    assert hasattr(led, 'blink')
    
    # Test states
    assert led.is_active is False
    led.on()
    assert led.is_active is True
    led.off()
    assert led.is_active is False

def test_init_hardware():
    """Verify that hardware initialization hooks up the LED controller."""
    led = main.init_hardware()
    assert led is not None
    assert led.pin == main.SHIELD_LED_PIN
