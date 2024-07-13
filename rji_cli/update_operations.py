import json 

def update_last_pick_json(last_pick_json_file_path, new_item):
    """Update last pick JSON file."""
    with open(last_pick_json_file_path, 'r+') as file:
        data = json.load(file)
        data.append(new_item)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()