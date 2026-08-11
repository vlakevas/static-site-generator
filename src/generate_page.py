import os
from markdown_to_htmlnode import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path:str, template_path:str, dest_path:str,basepath:str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    ffrom = open(from_path,"r")
    from_path_contents = ffrom.read()
    ffrom.close()
    
    content = markdown_to_html_node(from_path_contents).to_html()
    title = extract_title(from_path_contents)

    ftemplate = open(template_path,"r")
    template_html = ftemplate.read()
    final_html = template_html.replace("{{ Title }}",title).replace("{{ Content }}",content).replace('href="/',f'href="{basepath}').replace('src="/',f'src="{basepath}')
    ftemplate.close()

    dir_path = os.path.dirname(dest_path)
    if dir_path:
        os.makedirs(dir_path,exist_ok=True)
    fdest = open(dest_path,"w")
    fdest.write(final_html)
    fdest.close()


