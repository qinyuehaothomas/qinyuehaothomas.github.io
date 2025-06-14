
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



const GLITCH_DURATION=3000;
function animate_glitch(timestamp){
    if(timestamp-prev_timestamp>GLITCH_DURATION){
        is_glitching=false;
        prev_timestamp=timestamp;
        requestAnimationFrame(animate_transition);
        return
    }

    [...glitch_slices].forEach(node=>glitch(node,timestamp));
    requestAnimationFrame(animate_glitch);
    // glitch and switch image
}

function animate_transition(timestamp){
    prev_timestamp=timestamp;
    
    current_title=(current_title+1)%TITLES.length;
    insert_img(TITLES[current_title].text);
    glitch_slices=slice_img(TITLES[current_title].text);
    Typewriter.innerText="";
    Typewriter.style.color=TITLES[current_title].colour
    requestAnimationFrame(animate_letter);
}

requestAnimationFrame(
    animate_transition
);

