from move_contents import move_contents


def main():
    DIR_PATH_STATIC = "./static"
    DIR_PATH_PUBLIC = "./public"
    move_contents(DIR_PATH_STATIC,DIR_PATH_PUBLIC)
    
    


if __name__ == "__main__":
    main()