import os
import subprocess
import sys

SCRCPY_DIR = os.path.join(os.path.dirname(__file__), "scrcpy-win64-v3.0")
ADB_PATH = os.path.join(SCRCPY_DIR, "adb.exe")
SCRCPY_PATH = os.path.join(SCRCPY_DIR, "scrcpy.exe")

def check_tools():
    """Checks if adb and scrcpy are available."""
    if not os.path.exists(ADB_PATH):
        print("Error: adb is not found in the scrcpy folder.")
        sys.exit(1)
    if not os.path.exists(SCRCPY_PATH):
        print("Error: scrcpy is not found in the scrcpy folder.")
        sys.exit(1)

def disconnect_all():
    """Disconnects all previous ADB connections."""
    print("Disconnecting all previous ADB connections...")
    subprocess.run([ADB_PATH, "disconnect"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def connect_via_wifi(ip_address, port="5555"):
    """Connects to the device via Wi-Fi."""
    print(f"Connecting to the device at {ip_address}:{port}...")
    result = subprocess.run([ADB_PATH, "connect", f"{ip_address}:{port}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if "connected" in result.stdout.lower():
        print("Wi-Fi connection established successfully.")
    else:
        print("Error connecting via Wi-Fi. Check the IP address and network.")
        print("adb connect output:", result.stdout)
        sys.exit(1)

def run_scrcpy():
    """Runs scrcpy."""
    print("Starting scrcpy...")
    subprocess.run([SCRCPY_PATH])

def show_menu():
    """Displays the menu options to the user."""
    print("Select the connection method:")
    print("1. USB Connection")
    print("2. Wi-Fi Connection (IP only)")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ").strip()
    return choice

def main():
    check_tools()
    disconnect_all()

    while True:
        choice = show_menu()
        if choice == "1":
            devices = subprocess.run([ADB_PATH, "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.strip()
            if "device" not in devices:
                print("No device connected via USB detected. Please connect your device.")
                continue
            run_scrcpy()
            break
        elif choice == "2":
            ip_address = input("Enter the device's IP address (e.g., 192.168.1.100): ").strip()
            if not ip_address:
                print("No IP address entered. Returning to menu...")
                continue
            connect_via_wifi(ip_address)
            run_scrcpy()
            break
        elif choice == "3":
            print("Exiting the program...")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
