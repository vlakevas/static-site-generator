import os
import shutil

from move_contents import move_contents
from generate_pages_recursive import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main() -> None:

    print("Copying static files to public directory...")
    move_contents(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    


if __name__ == "__main__":
    main()