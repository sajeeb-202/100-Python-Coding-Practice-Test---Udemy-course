import os
import shutil
def copy_file(source_path, destination_path):
    try:
        if not isinstance(source_path, str) or not isinstance(destination_path, str):
            return False
        
        if not os.path.isfile(source_path):
            return False
        
        shutil.copyfile(source_path, destination_path)

        return True
    
    except Exception:
        return False