const glitch_box=document.getElementById("glitch-box")

// url="https://preview.redd.it/why-is-teto-pear-so-addicting-v0-gxac6cd20m0f1.jpeg?auto=webp&s=93cdd52a6524daf1a299b8012f4f3d2e3465808a"

const randint=(n)=>Math.floor(Math.random()*n);

const image_src=(title)=>`/media/index/${title}.png`

function insert_img(title){

    glitch_box.innerHTML=`<img src="${image_src(title)}" class="hero-bg-image">`
}


function slice_img(title){
    const MAX_FRAGMENT=20;
    // glitch_box.className+=` bg-[url${img_src}]`


    for(let i=0;i<20;i++){
        // generate radom coordinates
        let [x,y]=[randint(100),randint(100)];
        let [w,h]=[ Math.max(0,randint(100-x)),
            Math.max(0,randint(20))];

        var cur=document.createElement('img');
        cur.src=image_src(title);
        cur.className="hero-bg-image glitch-slices";
        cur.setAttribute("style",
            `clip-path:polygon(\
            ${x}% ${y}%,\
            ${x+w}% ${y}%,\
            ${x+w}% ${y+h}%,\
            ${x}% ${y+h}%\
        );`);
        glitch_box.appendChild(cur);
    }

    return document.getElementsByClassName("glitch-slices");
}

function set_glitch_animation(node){
    return
}