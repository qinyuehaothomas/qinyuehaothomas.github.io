const hero_img=document.getElementById("hero-img");
const Observer = new IntersectionObserver((entries) => {entries.forEach(
    entry=>{
        // console.log(entry.intersectionRect);
        if(entry.target.parentElement.id=="hero-img"){
            
            if(entry.isIntersecting){
                hero_img.style.opacity=1;
                hero_img.style.bottom="0px";
            }else{
                hero_img.style.opacity=0;
                hero_img.style.bottom="";

            }
        }else{
            if(entry.isIntersecting){
                entry.target.parentElement.style.right=0;
                // hero_img.style.opacity=1;
                // hero_img.style.bottom="0px";
            }else{
                entry.target.parentElement.style.right="";
                // hero_img.style.opacity=0;
                // hero_img.style.bottom="";

            }
        }
    }
);
});
// start observing
[...document.getElementsByClassName("intro-scroll-show")].forEach(
    target=>{
        let trigger=document.createElement('span');
        trigger.className="trigger absolute size-[10%] -right-[10%]  ";
        target.appendChild(trigger);
        Observer.observe(trigger);
    }
);

Observer.observe(hero_img.firstElementChild);
