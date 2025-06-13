# Idea
Pre-render static site before deployment
Use json file to describe Achievement & Projects, Then render them with file structure
- PIL for image compression
- requests for taking down .md
- Jinja for HTML templating
- Tailwindcss for styling

To make my life easier, I'll embed my posts elsewhere into the site?
Those without external post will rely on **image carousell**

# Compiling
- **REMEBER TO GITIGNORE tailwind.exe!!!**
- Achievement
Go under `src\Achievement\<EVENT NAME>`, get description from `details.json`, and put up all the pictures in the folder

- Images please format in`.png`

# Deployment
First, download tailwind standalone cli (file too large cannot upload)
put in root directory
Run
```console
./tailwindcss -i src/style.css -o src/rendered.css -w
```
to render tailwind css

Run
```console
python _COMPILE.py
```
to render templates