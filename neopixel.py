import machine # Used to control hardware like pins
import neopixel # The library for controlling NeoPixel (WS2812B) LEDs
import time # Used for delays (e.g., to pause between color changes)

# --- CONFIGURATION ---
# IMPORTANT: Connect your NeoPixel data line to this pin on the Raspberry Pi Pico.
# GP0 (Pin 1) is a good starting point.
NEOPIXEL_PIN = 18

# Set this to the number of NeoPixels you have connected.
# If you have just one LED, keep it as 1.
NUM_PIXELS = 1

# --- NEOPIXEL INITIALIZATION ---
# This line sets up the NeoPixel object.
# It tells MicroPython which pin is connected to the data line and how many pixels there are.
np = neopixel.NeoPixel(machine.Pin(NEOPIXEL_PIN), NUM_PIXELS)

# --- HELPER FUNCTION: SET COLOR WITH BRIGHTNESS (GRB Order) ---
# This function makes it easy to set the color and brightness of your NeoPixel.
# It assumes your NeoPixel is a GRB (Green, Red, Blue) type.
def set_pixel_grb(target_g, target_r, target_b, brightness=1.0):
    """
    Sets all connected NeoPixels to a specific GRB color with adjustable brightness.

    Args:
        target_g (int): Desired Green component (0-255).
        target_r (int): Desired Red component (0-255).
        target_b (int): Desired Blue component (0-255).
        brightness (float): How bright the LED should be (0.0 = off, 1.0 = full brightness).
                                   Default is 1.0 (full brightness).
    """
    # Check if the brightness factor is within a valid range
    if not 0.0 <= brightness <= 1.0:
        print("Warning: Brightness factor must be between 0.0 and 1.0. Using default 1.0.")
        brightness = 1.0

    # Apply the brightness factor to each color component
    # We use int() to convert the result to a whole number
    g = int(target_g * brightness)
    r = int(target_r * brightness)
    b = int(target_b * brightness)

    # Ensure values are strictly within the 0-255 range (safety check)
    g = max(0, min(255, g))
    r = max(0, min(255, r))
    b = max(0, min(255, b))

    # Loop through all pixels (even if it's just one) and set their color
    for i in range(NUM_PIXELS):
        # We send the color in GRB order to the NeoPixel
        np[i] = (g, r, b)

    # After setting the colors in memory, we "write" them to the actual LEDs
    np.write()

# --- MAIN PROGRAM LOOP ---
# This is a "while True" loop, meaning it will run forever
# until the Pico is powered off or the program is stopped manually (e.g., in Thonny).
print("Starting NeoPixel demonstration loop...")
while True:
    # --- RED COLOR ---
    print("Showing RED at full brightness...")
    # For a GRB LED, Red is (G=0, R=255, B=0)
    set_pixel_grb(0, 255, 0, 1.0) # Full brightness
    time.sleep(1) # Wait for 1 second

    # --- DIM RED COLOR ---
    print("Showing DIM RED (50% brightness)...")
    set_pixel_grb(0, 255, 0, 0.5) # 50% brightness
    time.sleep(1) # Wait for 1 second

    # --- GREEN COLOR ---
    print("Showing GREEN at full brightness...")
    # For a GRB LED, Green is (G=255, R=0, B=0)
    set_pixel_grb(255, 0, 0, 1.0)
    time.sleep(1) # Wait for 1 second

    # --- BLUE COLOR ---
    print("Showing BLUE at full brightness...")
    # For a GRB LED, Blue is (G=0, R=0, B=255)
    set_pixel_grb(0, 0, 255, 1.0)
    time.sleep(1) # Wait for 1 second

    # --- MAGENTA (RED + BLUE) ---
    print("Showing MAGENTA...")
    # Red (0, 255, 0) + Blue (0, 0, 255) = (0, 255, 255) in GRB
    set_pixel_grb(0, 255, 255, 1.0)
    time.sleep(1)

    # --- WHITE COLOR (all colors on) ---
    print("Showing WHITE...")
    # White is all colors on full. For GRB: (G=255, R=255, B=255)
    set_pixel_grb(255, 255, 255, 1.0)
    time.sleep(1)

    # --- DIM WHITE COLOR ---
    print("Showing DIM WHITE (10% brightness)...")
    set_pixel_color_grb(255, 255, 255, 0.1)
    time.sleep(1)

    # --- TURN OFF (BLACK) ---
    print("Turning LED OFF...")
    set_pixel_color_grb(0, 0, 0, 0.0) # All components 0, or brightness 0.0
    time.sleep(2) # Wait a bit longer when off before repeating
