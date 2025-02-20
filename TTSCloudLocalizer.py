import json
import os
LOCAL_PROMPT = "Enter the path of the TTS Mods Folder. Default is here C:-Users-userName-Documents-My Games-Tabletop Simulator-Mods"
JSON_PROMPT = "Enter the full path of the JSON TTS File you would like to localize"
def get_directory(message):
    while True:
        print(message)
        path = input()
        print("The path you entered is:" + path)
        print("Is this the correct path? (Y/N)")
        response = input()
        if response == "Y" or response == "y":
            return path
def validate_Json(self, file_path):
    if not os.path.exists(file_path):
        print("The file does not exist")
        return False
    
class FileTypeSelection():
    def __init__(self):
        self.file_options = {
            "MeshURL": True,
            "ImageURL": True,
            "NormalURL": True,
            "FaceURL": True,
            "BackURL": True,
            "ColliderURL": True,
            "PDFUrl": True,
            "DiffuseURL": True,
            "SkyURL": True,
            "ImageSecondaryURL": True
        }
        self.localPath = ""
        self.nonLocalPath = ""
        self.JSONPath = ""
        self.keyWords = list(self.file_options.keys())
        self.modification_counts = {key: {"good": 0, "bad": 0} for key in self.file_options}
        self.debugMode = False
    def set_localPath(self, path):
        new_path = "file:///" + path
        self.localPath = new_path
    def set_nonLocalPath(self, path):
        self.nonLocalPath = path
    def set_JSONPath(self, path):
        self.JSONPath = path
    def print_File_Options(self):
        for fileType, value in self.file_options.items():
            print(fileType + ": " + str(value))
    def set_File_Options(self):
        self.ready_Check = False
        while not self.ready_Check:
            print("Would you like to enable all file types? (Y/N)")
            response = input().strip().lower()
            if response == "y":
                self.enable_All_File_Options()
                self.ready_Check = True
            else:
                self.set_custom_file_options()
                self.print_File_Options()
                print("Are these the correct file options? (Y/N)")
                response = input().strip().lower()
                if response == "y":
                    self.ready_Check = True
    def set_custom_file_options(self):
        for fileType in self.file_options.keys():
            print("Would you like to enable " + fileType + "? (Y/N)")
            self.file_options[fileType] = input().strip().lower() == 'y'
    def enable_All_File_Options(self):
        for fileType in self.file_options:
            self.file_options[fileType] = True     
    def setKeyWords(self):
        self.keyWords = [fileType for fileType, enabled in self.file_options.items() if enabled]
    def convert_url(self, url, file_type):
        if url.startswith("http://cloud-3.steamusercontent.com/ugc/"):
            cleaned_url = url.replace("http://cloud-3.steamusercontent.com/ugc/", "").replace("/", "")
            file_name = "httpcloud3steamusercontentcomugc" + cleaned_url

            local_dir = self.localPath.replace("file:///", "")
            matched_file = None

            for root, _, files in os.walk(local_dir):
                for file in files:
                    if file.startswith(file_name):
                        matched_file = os.path.join(root, file)
                        break
                if matched_file:
                    break

            if matched_file:
                self.modification_counts[file_type]["good"] += 1
                return "file:///" + matched_file.replace("/", "\\")
            else:
                self.modification_counts[file_type]["bad"] += 1
                if self.debugMode:
                    print(f"File not found for: {url}")
        
        return url
    def modify_urls_recursive(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key in self.file_options and self.file_options[key] and isinstance(value, str):
                    data[key] = self.convert_url(value, key)
                elif isinstance(value, (dict, list)):
                    self.modify_urls_recursive(value)
    def process_json(self, file_path):
        if not os.path.isfile(file_path):
            print(f"Error: The JSON file '{file_path}' does not exist. Please provide a valid file path.")
            return
        try:
            with open(file_path, "r", encoding="utf-8") as json_file:
                lines = json_file.readlines()
            updated_lines = []
            for line in lines:
                for file_type in self.file_options:
                    if self.file_options[file_type] and f'"{file_type}":' in line and "http://cloud-3.steamusercontent.com/ugc/" in line:
                        start_index = line.find("http://cloud-3.steamusercontent.com/ugc/")
                        end_index = line.find('"', start_index + 1)
                        cloud_url = line[start_index:end_index]
                        converted_url = self.convert_url(cloud_url, file_type)
                        line = line.replace(cloud_url, converted_url)
                updated_lines.append(line)
            with open(file_path, "w", encoding="utf-8") as json_file:
                json_file.writelines(updated_lines)
            print("\n===== Modification Summary =====")
            for file_type, counts in self.modification_counts.items():
                if self.file_options[file_type]:
                    print(f"{file_type}: ✅ {counts['good']} good | ❌ {counts['bad']} bad")
            print("===============================")
            print("JSON file has been updated successfully.")
        except Exception as e:
            print("An error occurred while processing the JSON file:", str(e))
    def setDebugMode(self):
        print("Would you like to enable debug mode? (Y/N)")
        response = input().strip().lower()
        self.debugMode = response == "y"
if __name__ == "__main__":
    Object = FileTypeSelection()
    Object.set_localPath(get_directory(LOCAL_PROMPT))
    Object.set_JSONPath(get_directory(JSON_PROMPT))
    Object.set_File_Options()
    Object.setDebugMode()
    Object.process_json(Object.JSONPath)
    print("Press any key to exit")
