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
        let [x,y]=[
            randint(20)*5,
            randint(20)*5];
        let [w,h]=[ randint(10)*5+20,
            randint(5)*3+5];

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
        // cur.dataset.next_timestamp=0;
        // cur.dataset.distorted=false;
        glitch_box.appendChild(cur);
    }

    return document.getElementsByClassName("glitch-slices");
}

function glitch(node,timestamp){
    if(timestamp<Number(node.dataset.next_timestamp)){
        return;
    }
    if(node.dataset.distorted=="false"){
        node.style.top=`${randint(20)-10}%`;
        node.style.right=`${randint(100)-50}%`;
        var coin=Math.random();
        if(coin<0.4){
            node.style.filter="sepia(1) brightness(200%) hue-rotate(148deg)";
        }else if(coin<0.8){
            node.style.filter="sepia(1) brightness(200%) hue-rotate(300deg)";
        }else if(coin<0.9){
            node.style.filter="invert()";
        }

        node.dataset.distorted=true;
        // duration of glitch
        node.dataset.next_timestamp=timestamp+randint(50)+50;
        
    }else{
        node.style.top='0px';
        node.style.right="0px";
        node.style.filter="";
        
        node.dataset.distorted=false;
        // duration of restore
        node.dataset.next_timestamp=timestamp+randint(3)*50+1000;

    }
}