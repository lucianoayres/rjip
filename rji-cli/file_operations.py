def file_exists(file_path):
    """Check if a file exists"""
    try:
        with open(file_path, 'r') as f:
            return True
    except FileNotFoundError:
        return False