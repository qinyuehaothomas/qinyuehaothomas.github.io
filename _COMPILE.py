import os.path
import bs4, jinja2,requests,sys
from PIL import Image

DIR=os.path.dirname(__file__)
Jinja_Env=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(DIR,"src")))

def scrap_git_projects():
    """
    Scrap the readme and turn into template
    Don't render
    Discluded Github project under here

    This injects the html into a template
    """

    # space is _
    EXCLUDE=["qinyuehaothomas.github.io","Desmos_Synthesizer","BoatyMacBoatFace"]
    USERNAME="qinyuehaothomas"

    # scrapped templates (to be rendered)
    github_dir=os.path.join(DIR,"src/projects/github")
    os.makedirs(github_dir, exist_ok=True)

    repo_list=requests.get(f"https://api.github.com/users/{USERNAME}/repos")
    for repo in repo_list.json():
        repo['name']=repo['name'].replace(" ","_").replace("-","_")
        projects_dir=os.path.join(DIR,f"src/projects/github/{repo['name']}")

        output_dir = os.path.join( projects_dir , f"{ repo['name'] }.html" )
        
        if repo[ 'name' ] in EXCLUDE : 
            print(f"Discluded : {repo['name']}")
            continue
        if os.path.exists(output_dir): 
            print(f"Already Scrapped : {repo['name']}")
            continue
        
        os.makedirs(projects_dir, exist_ok=True)
        
        print(f"Scrapping {repo['name']}")
        
        try:
            repo_respond=requests.get(repo["html_url"])
            soup=bs4.BeautifulSoup(repo_respond.text,"html.parser")
            README=soup.find("article",class_="markdown-body")
            for child in README.find_all(recursive=True):

                if child.get("src"):
                    child["src"] = "https://github.com"+child["src"] if "https://" not in child["src"] else ""
                if child.get("href"):
                    child["href"] += "https://github.com"+child["href"] if "https://" not in child["href"] else ""
            
            to_jinja="\n".join(line.lstrip() for line in f"""\
            {{% extends 'GITHUB_TEMPLATE.html' %}}
                               
            {{% set title = ''' {repo['name'].replace("_"," ")} '''  %}}

            {{% set content =  ''' {README.prettify().replace("'",'"')} '''  %}}
            """.split("\n"))

            with open(output_dir,"w",encoding='utf-8') as f:
                    # dir to GITHUB template
                    # GITHUB_TEMPLATE=os.path.join(os.path.join(DIR,"src"),"GITHUB_TEMPLATE.html")
                    # print(to_jinja)
                    f.write(to_jinja)
                    print(f"Scrapping Finished {repo['name']}")
        except Exception as e:
            print(f"Error Scrapping {repo['name']}: {str(e)}")

def render_html(root_dir):  
    """
    Modified from compress_image()
    The html paths is confusing,
    basically root/src/a/b/c/c.html (The template)
    becomes root/a/b/c.html
    """
    # Validate directory exists
    src_path = os.path.join(root_dir, 'src')
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Source directory not found: {src_path}")
    
        
    # Process all images
    for root, _, files in os.walk(src_path):
        for file in files:
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(root, src_path)

            

            if file.lower().endswith(".html") and root!=src_path:
                output_dir=os.path.join(root_dir,os.path.dirname(rel_path))
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, file )
                
                print(f"Rendering Source: {src_file} ")
                
                input_path=os.path.join(rel_path,file).replace("\\","/")
                with open(output_file,"w",encoding="utf-8") as f:
                    f.write(Jinja_Env.get_template(input_path).render())
                print(f"Finished Rendering: {output_file}")

def compress_images(root_dir, FORCED=False):  
    """
    Vibe Coded !!!!
    I mean its a freaking utility function

    Compress image in root_dir to 1280px wide
    and save to media_dir with folder structure
    Convert file type to .png
    Most importantly, vibe coded ╮（╯＿╰）╭
    """
    # Validate directory exists
    src_path = os.path.join(root_dir, 'src')
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Source directory not found: {src_path}")
    
    # Create media directory
    media_path = os.path.join(root_dir, 'media')
    os.makedirs(media_path, exist_ok=True)
    
    # Supported image extensions
    img_exts = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')
    
    # Process all images
    for root, _, files in os.walk(src_path):
        for file in files:
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(root, src_path)

            if file.lower().endswith(img_exts):
                # Get paths
                media_dir = os.path.join(media_path, rel_path)
                output_file = os.path.join(media_dir, os.path.splitext(file)[0] + '.png')
                
                # Create output directory structure
                os.makedirs(media_dir, exist_ok=True)
                
                # Process image
                try:
                    if os.path.exists(output_file) and not FORCED:
                        print(f"Already Exist: {output_file}")
                        continue
                    with Image.open(src_file) as img:
                        # Resize if wider than 1280px
                        if img.width > 1280:
                            ratio = 1280 / img.width
                            new_height = int(img.height * ratio)
                            img = img.resize((1280, new_height), Image.LANCZOS)
                        
                        # Save as PNG
                        img.save(output_file, 'PNG', optimize=True)
                        print(f"Compressed: {src_file} -> {output_file}")
                
                except Exception as e:
                    print(f"Error processing {src_file}: {str(e)}")

# Means force a render even when destination exists
# for updates
if __name__=="__main__":
    # Render Index
    # Render About (Maybe Index will include about)
    # Find all .json in 

    force_image=len(sys.argv)>1
    force_=len(sys.argv)>1
    FORCE_IMG=len(sys.argv)>1
    if "-git" in sys.argv : scrap_git_projects()
    compress_images(DIR,"-img" in sys.argv)
    render_html(DIR)