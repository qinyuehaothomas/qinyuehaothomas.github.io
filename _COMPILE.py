import os.path
import bs4, jinja2,requests,sys
from PIL import Image


DIR=os.path.dirname(__file__)
Jinja_Env=jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(DIR,"src")))


class Project():
    def __init__(self):
        self.date=""
        self.description=""
        self.embed=[]
        self.tags=[]
    def render():
        # Gonna be a tough fight
        pass

class Achievement():
    def __init__(self):
        self.date=""
        self.description=""
        self.tags=[]
    def render():
        # Just image + Description 
        # Then gallery
        # Might wanna have a good gallery
        pass

def scrap_git_projects():
    exclude=["",""]

    pass



def render_html(root_dir):
    
    """Compress images in root_dir and save to media_dir with folder structure"""
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


            if file.lower().endswith(".html") and root!=src_path:
                output_dir=os.path.join(root_dir,os.path.dirname(rel_path))
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, file )
                
                input_path=os.path.join(rel_path,file).replace("\\","/")
                with open(output_file,"w") as f:
                    f.write(Jinja_Env.get_template(input_path).render())
                print(f"Rendered: {src_file} -> {output_file}")


# Vibe Coded !!!!
# I mean its a freaking utility function

def compress_images(root_dir, FORCED=False):
    
    """Compress images in root_dir and save to media_dir with folder structure"""
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
                    if os.path.exists(output_file):
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


if __name__=="__main__":
    # Render Index
    # Render About (Maybe Index will include about)
    # Find all .json in 

    # Compress image to 1280px wide
    # Mirror directory into /meida folder
    # Convert file type to .png
    # Most importantly, vibe coded ╮（╯＿╰）╭
    compress_images(DIR,  True if len(sys.argv)>1 else False)

    render_html(DIR)