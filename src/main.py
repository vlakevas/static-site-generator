from move_contents import move_contents
from generate_page import generate_page

DIR_PATH_STATIC = "./static"
DIR_PATH_PUBLIC = "./public"

def main():
    
    move_contents(DIR_PATH_STATIC,DIR_PATH_PUBLIC)
    generate_page("./content/index.md","./template.html","./public/index.html")
    

    
    


if __name__ == "__main__":
    main()