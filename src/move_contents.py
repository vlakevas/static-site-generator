import os 
import shutil

def move_contents(source:str, destination:str) -> None:
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    helper_contents(source,destination)
def helper_contents(source:str, destination:str) -> None:
    
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path,dest_path)
            print(dest_path)
        else:
            os.mkdir(dest_path)
            helper_contents(source_path,dest_path)