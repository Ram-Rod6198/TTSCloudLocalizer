# Tabletop Simulator Cloud Localizer

## Overview
Some assets in **Tabletop Simulator (TTS)** become inaccessible when the original uploader moves or removes them from their cloud database. A notable case was with Modiphius, when they relocated their database in Google Drive, breaking their *Fallout: Wasteland Warfare* mod. I reached out to them to see if I could fix the issue for them. Instead of manually fixing all 572 assets, I was fortunate enough to find someone who had the original assets stored on their PC and I created this tool to automate the process of linking the broken Url with the asset on my drive.

This program scans the **JSON save files** of TTS, grabs the cloud assets, and replaces them with local copies stored in your **Mods** folder.

📌 **Original Mod (Broken):** [Fallout Wasteland Warfare](https://steamcommunity.com/sharedfiles/filedetails/?id=2165945542)  
📌 **Fixed Mod (Reuploaded with Permission):** [Fixed Fallout Mod](https://steamcommunity.com/sharedfiles/filedetails/?id=3214606965)

## Features
- **Scans & Fixes TTS Mod Files:** Replaces URLs of cloud assets with local file paths.
- **Supports All Asset Types:** Works with models, textures, PDFs, and other supported file formats.
- **Recursive Folder Search:** Finds assets even if they are stored in **subfolders**.
- **Modification Summary:** Displays how many assets were successfully fixed and how many were missing.
- **Debug Mode:** Logs warnings when assets cannot be found.

## Supported Asset Types
This tool supports modifying the following TTS asset types:
- `MeshURL`
- `ImageURL`
- `NormalURL`
- `FaceURL`
- `BackURL`
- `ColliderURL`
- `PDFUrl`
- `DiffuseURL`
- `SkyURL`
- `ImageSecondaryURL`

## Requirements
### Dependencies
Ensure you have the following installed before running the script:
- Python 3.7+
- `os`
- `json`

### External Requirements
- A **Tabletop Simulator Mods Folder** containing all required local assets.
- The **TTS JSON Save File** you want to localize.

## Installation
1. **Clone or Download the Repository**
   ```sh
   git clone https://github.com/YourUsername/TTS-Asset-Localizer.git
   cd TTS-Asset-Localizer
   ```

2. **Run the Script**
   ```sh
   python localizer.py
   ```

## Usage
1. **Run the script.** It will prompt you for:
   - The **path to your TTS Mods folder** (e.g., `C:\Users\yourname\Documents\My Games\Tabletop Simulator\Mods`).
   - The **path to your JSON Mod file**.
   - Whether you want to enable all file types or manually select specific ones.
   - If you want to **enable Debug Mode** to log missing files.

2. **The script scans each asset type, replaces missing ones with local files, and updates the JSON.**

3. **At the end, a summary report** will show how many assets were successfully fixed and how many were missing.

## Example Summary Output
```
===== Modification Summary =====
MeshURL: ✅ 35 good | ❌ 0 bad
ImageURL: ✅ 118 good | ❌ 34 bad
NormalURL: ✅ 33 good | ❌ 0 bad
FaceURL: ✅ 92 good | ❌ 0 bad
BackURL: ✅ 92 good | ❌ 0 bad
ColliderURL: ✅ 34 good | ❌ 0 bad
PDFUrl: ✅ 1 good | ❌ 3 bad
DiffuseURL: ✅ 34 good | ❌ 0 bad
SkyURL: ✅ 1 good | ❌ 0 bad
ImageSecondaryURL: ✅ 126 good | ❌ 0 bad
===============================
```

## Known Issues
- **File not found** If the asset does not exist in your folder then this can not link to it.
- **Localizes all files** This tool does not check if a link is good before localizing, it just localizes it so that you can reupload it yourself.

## License
This project is open-source under the **MIT License**. Feel free to use, modify, or expand upon it, but please provide credit.

## Author
[Ram-Rod6198]
