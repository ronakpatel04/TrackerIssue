import time
import threading
import keyboard

# Initialize counter variable
key_press_count = 0

# Function to perform background activity and update display
def background_activity():
    while True:
        # Perform background activity here
        # For demonstration, let's print something
        print("Background activity running...")

        # Update display or perform other tasks as needed
        update_display()

        # Sleep for 2 minutes
        time.sleep(120)

# Function to update display
def update_display():
    # Perform display update here
    # For demonstration, let's print something
    print("Display updated.")

# Function to simulate key press
def simulate_key_press():
    while True:
        # Simulate pressing the 'q' key
        keyboard.press('q')
        # Sleep for a short duration before releasing the key
        time.sleep(60)
        # Release the key
        keyboard.release('q')

        # Increment the key press count
        global key_press_count
        key_press_count += 1
                

if __name__ == "__main__":
    # Start the background activity thread
    background_thread = threading.Thread(target=background_activity)
    background_thread.start()

    # Start simulating key press
    key_press_thread = threading.Thread(target=simulate_key_press)
    key_press_thread.start()

    # Continuous loop to check and print the key press count
    while True:
        print(f"'q' key pressed {key_press_count} times.")
        time.sleep(60)  # Print count every minute
        