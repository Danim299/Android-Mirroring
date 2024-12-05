# Scrcpy Wi-Fi/USB Connection Manager

This script provides a simple interface to manage connections and start the [Scrcpy](https://github.com/Genymobile/scrcpy) screen mirroring tool. It supports both USB and Wi-Fi connection methods for Android devices.

## Features
- Check for necessary tools (`adb` and `scrcpy`) in the specified directory.
- Disconnect all existing ADB connections before starting a new one.
- Connect to an Android device via USB or Wi-Fi.
- Automatically start Scrcpy once the connection is established.
- User-friendly menu for selecting connection methods.

## Prerequisites
1. Download the [Scrcpy prebuilt package](https://github.com/Genymobile/scrcpy/releases) for Windows and extract it.
2. Place the `scrcpy-win64-v3.0` folder (or the correct version folder) in the same directory as this script. (Make sure to edit the version in the python script)
3. Ensure Python is installed on your system.

## Usage
1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script using Python:
   ```bash
   python script_name.py
