const diplay_screen=document.getElementById("output");
const box=document.getElementById("pbox");
var show=1;
var hide=0;

function screen_on(atomic_no,symbol,name,atomic_mass,xpos,ypos,cpk_hex) {
  
  console.log(`Showing Screen`);
  diplay_screen.style.opacity=show;
  box.classList.toggle('blur');

  diplay_screen.innerHTML =atomic_no;
  console.log(atomic_no+"<----- : added");
  diplay_screen.onclick=function() {
    box.classList.toggle("blur");
    console.log(`Disabling Screen`);
    diplay_screen.style.opacity=hide;
    
    
  };
}
