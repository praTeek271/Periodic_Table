const diplay_screen=document.getElementById("output");
var counter=0;

function screen_on(atomic_no) {
  var val=counter%2;
  console.log(val);
  diplay_screen.style.opacity=val;

  counter+=1;
  diplay_screen.innerHTML =atomic_no;
  console.log(atomic_no+"<----- : added");
}
