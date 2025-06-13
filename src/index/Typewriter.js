
const Typewriter=document.getElementById("Typewriter");
var glitch_slices;
const TITLES=[
    {text:"Codes",colour:"#50d5d0"},// first one
    {text:"Desmos Art",colour:"skyblue"},
    {text:"CAD Model",colour:"#79BA5F"},
    {text:"Origami",colour:"#eee7d7"},
    {text:"Robots",colour:"#DA2E36"}
]

const LETTER_INTERVAL=100;
const WORD_INTERVL=1000;
var prev_timestamp=0;
var current_title=-1; // some indexing issue...

function animate_letter(timestamp){
    if(timestamp-prev_timestamp>LETTER_INTERVAL){
        
        prev_timestamp=timestamp;

        if(Typewriter.textContent.length < TITLES[current_title].text.length ){
            
            Typewriter.textContent+=TITLES[current_title].text[Typewriter.textContent.length];
        }else{
            // console.log(Typewriter.textContent);
            requestAnimationFrame(animate_glitch);
            return
        }
    } 
    requestAnimationFrame(animate_letter);
}


var is_glitching=false;

function animate_glitch(timestamp){
    if(!is_glitching){
        glitch_slices=slice_img(TITLES[current_title].text);
        glitch_slices.forEac
        is_glitching=true;
    }
    if(timestamp-prev_timestamp>WORD_INTERVL){
        requestAnimationFrame(animate_transition)
    }else{

        requestAnimationFrame(animate_glitch);
    }

    // glitch and switch image
}

function animate_transition(timestamp){
    is_glitching=false;
    prev_timestamp=timestamp;
    
    current_title=(current_title+1)%TITLES.length;
    insert_img(TITLES[current_title].text);
    Typewriter.innerText="";
    Typewriter.style.color=TITLES[current_title].colour
    requestAnimationFrame(animate_letter);
}

requestAnimationFrame(
    animate_transition
);

