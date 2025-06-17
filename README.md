# Temporary: TODO

It's the end of june hols and i havnt start studying 💀

Gotta hold my horses bud

Here are the **TODO** s:
1.  `projects_json_collapse()` function (now is a brute force placeholder)
    1. Description for github projects
    1. Re-write cover page with typed.js
    1. Desmos
    1. CAD
    1. Origami
    1. Robotics
    1. Project filter
1. Achievements
    1. it's corrisponding functions
    1. dates and statements
    1. timeline
1. Self-statements
1. Add images

good luck have fun 💀

# Idea
Pre-render static site before deployment
Use json file to describe Achievement & Projects, Then render them with file structure
- PIL for image compression
- requests for taking down .md
- Jinja for HTML templating
- Tailwindcss for styling

To make my life easier, I'll embed my posts elsewhere into the site?
Those without external post will rely on **image carousell**

# Reminders
- **REMEBER TO GITIGNORE tailwind.exe!!!**

- The html paths is confusing,
basically `root/src/a/b/c/c.html` (The template)\
becomes `root/a/b/c.html`

- projects.json format:
``` json
{
    "projects":[
        "title":"", // Name of project
        "link":"", // Link to page
        "tags":[ // tags
            ("github","miku-green")
        ]
        "description":"" // short description
    ]
}

// Unless specified, thumbnail located in the folder, as "thumbnail.png"
```


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
Will render all html templates, and compress any new image

- `python _COMPILE.py -git`  scrapes github and compile `/src/projects/github/projects.json`
- `python _COMPILE.py -img`  **forces all** image conversion and compression
