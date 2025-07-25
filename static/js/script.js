document.addEventListener('DOMContentLoaded',()=>{
  M.FormSelect.init(document.querySelectorAll('select'));
  M.Materialbox.init(document.querySelectorAll('.materialboxed'));
  M.Modal.init(document.querySelectorAll('.modal'));

  //post
  chooseFile(document.getElementById('doc'),document.getElementById('docPlace'));


});

//change input file
function chooseFile(input,place){
  input.onchange = ()=>{
    place.style.display = 'block';
    place.textContent = input.value;
  }
}

let links = document.querySelectorAll('.post-link');
let  posts = document.querySelectorAll('.post');
let  tables = document.querySelectorAll('.post-details');
let  backs = document.querySelectorAll('.back-to-post');

links.forEach(link=>{
   link.onclick = ()=>{
     posts.forEach(post=>{
       post.style.display = 'none';
     });
     tables.forEach(table=>{
       if(table.id == link.id){
          table.style.display = 'block';
       }
     });
  }
})

backs.forEach(back=>{
  back.onclick  = ()=>{
     posts.forEach(post=>{
       post.style.display = 'block';
     });
     tables.forEach(table=>{
       if(table.id == link.id){
          table.style.display = 'none';
       }
     });
  }
})
