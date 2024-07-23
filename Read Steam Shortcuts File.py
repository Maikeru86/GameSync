import vdf
import os

def read_shortcuts_vdf(shortcuts_file):
    if os.path.exists(shortcuts_file):
        with open(shortcuts_file, 'rb') as f:
            shortcuts = vdf.binary_load(f)
            return shortcuts
    else:
        print(f"File {shortcuts_file} not found.")
        return None

def display_shortcuts(shortcuts):
    if shortcuts:
        for idx, shortcut in shortcuts['shortcuts'].items():
            print(f"Shortcut {idx}:")
            print(f"  App ID: {shortcut.get('appid')}")
            print(f"  App Name: {shortcut.get('appname')}")
            print(f"  Executable: {shortcut.get('exe')}")
            print(f"  Start Directory: {shortcut.get('StartDir')}")
            print(f"  Icon: {shortcut.get('icon')}")
            print(f"  Launch Options: {shortcut.get('LaunchOptions')}")
            print(f"  Tags: {shortcut.get('tags')}")
            print()

if __name__ == "__main__":
    # Specify the path to your shortcuts.vdf file
    steam_user_data_path = "C:\\Program Files (x86)\\Steam\\userdata\\<USER ID>\\config" #ADD YOUR STEAM CONFIG FOLDER HERE
    shortcuts_file = os.path.join(steam_user_data_path, 'shortcuts.vdf')

    # Read shortcuts.vdf file
    shortcuts_data = read_shortcuts_vdf(shortcuts_file)

    # Display shortcuts in a human-readable format
    if shortcuts_data:
        display_shortcuts(shortcuts_data)
