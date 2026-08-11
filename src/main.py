import os
import shutil
import sys

from move_contents import move_contents
from generate_pages_recursive import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main() -> None:
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    print("Copying static files to public directory...")
    move_contents(dir_path_static, dir_path_docs)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs,basepath)
    


if __name__ == "__main__":
    main()