document.addEventListener('mousemove', (event) =>{
   const element = document.getElementById('animateMe');
   const x = event.clientX;
   const y = event.clientY;
   element.style.left = '${x}px';
   element.style.right = '${y}px'; 
});