# Day 1
After resting ~~g88ning~~ for 4 days, It's time to gte back to work

Tried Tailwind standalone CLI at v4.1.8, most tutorials were on v3 or NPM, so it took a bit of trial and error.

Spent a **massive amount of time to make a navigation bar**

# Day 2
Had Onearena, spent some time to make the typing animation
the cursor is a blinking right border🤣
the text is added one by one using js

Deepseek told me to use `requestanimationframe()` for better performance

Problem: Tailwind only "prepare" classes that are in the static html document,
so **those utility classes that were not in the static html will not be prepared**

# Day 3
Workaround (from stackoverflow):
- Safelist in config file
- Create emity element with these classes
- Directly edit css atrribute (I went with this)

After contemplating, decided on using Image gltich as transition
because miku's color scheme makes me think of glitch
Tutorial link: [https://muffinman.io/blog/css-image-glitch/](https://muffinman.io/blog/css-image-glitch/)

Aspect ratio of image seems to be a pretty big issue.. So when render , need to crop the images into specific aspect raios.

Then it is the positioning issue on the index page.
ATP i just give up making glitches.

**Fixed it by using normal CSS `clip-path:polygon();`**
It:
- Keeps the image's size, so no need to offset
- allows `object-fit:cover;` , so image can automatically adjust size without squashing
- Allow percentage, so no need to calcluate pixels


Image type plz standardise to .png

The *titles* variable might want to move outside as a json file?

Have to create a new repo because neevr gitignore tailwind.exe....
/_ \

# Day 4
Pulled off a all nighter i dont know what for
But anyways the glitch effect is up and I think its quite cool 

Fine-tune the glitch effect (what for bro)
added icon?

Time to write some content i guess?

**Future Problem: Image is loading everytime image switches, need cache.**

did some work on the compiler?

**For Compilier, Definitely want to make a "walk" decorator for different types of operations**

# Day 5 
Some extremely unlegiable 😵‍💫 bullcrap.
So for `scrap_git_project()`, if I directly render a template:
1. The template will be in `src` folder
2. Everytime I want to change the format of github project pages,\
**The scrapping have to be done again (because it is DIRECTLY rendered after scrapping)**

So, big brain me comes up with this solution
1. after scrapped, **store the scrapped content as variables** using `{% set <VARIABLE_NAME> ="" %}`\
2. **directly put into html without rendering**
3. When `render_html()` is executed, it will render 
    1. the `<Project Name>.html`, with content as variables, and extends `GITHUB_TEMPLATE.html`
    2. Then `GITHUB_TEMPLATE.html`, which put in CSS and formatting of Github pages, and is an extension of `TEMPLATE.hmtl`
    3. Then everything into `TEMPLATE.html`
4. Then everything will be saved in the file in the destination folder!

So everytime I edit `GITHUB_PROJECT.html`, scrapping does not need ot be done again !

Styled project card ~~Teto Pear~~
