import os
from generate_page import generate_page
def generate_pages_recursive(dir_path_content:str, template_path:str, dest_dir_path:str):


    for item in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isdir(source_path):
            generate_pages_recursive(source_path,template_path,dest_path)

        elif item.endswith(".md"):
            
            generate_page(source_path,template_path,dest_path.replace(".md",".html"))



