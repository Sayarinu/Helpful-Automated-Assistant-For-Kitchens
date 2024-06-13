import json

def read_json_file():
    cuisines = {}
    with open("Back-end Files/text_files/cuisines.json", "r") as file:
        cuisines = json.loads(file.readline())
    file.close()
    return cuisines

def write_json_file(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

cuisines = read_json_file()

while True:
    new_key = input("Enter a new key: ")
    if new_key == "exit":
        break
    new_value = input("Enter a value for the new key: ")
    cuisines[new_key] = new_value

write_json_file(cuisines, "Back-end Files/text_files/cuisines.json")

print("Updated JSON data has been saved.")
