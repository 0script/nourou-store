const togglesearch=document.querySelector('i#toggle-search');
const search=document.querySelector('div.search');

/* responsive nav menu vars */
const menunav=document.querySelector('ul.links-container')
const bouttonmenu=document.querySelector('i#icon-menu-btn');

togglesearch.addEventListener('click',()=>{

    search.classList.toggle('active');

    if(togglesearch.classList.contains('fa-magnifying-glass')){
        togglesearch.classList.remove('fa-magnifying-glass');
        togglesearch.classList.add('fa-xmark');
    }else{
        togglesearch.classList.remove('fa-xmark');
        togglesearch.classList.add('fa-magnifying-glass');
    }
});

bouttonmenu.addEventListener('click',()=>{

    menunav.classList.toggle('active');
    if(bouttonmenu.classList.contains('fa-bars')){
        bouttonmenu.classList.remove('fa-bars');
        bouttonmenu.classList.add('fa-xmark');
    }else{
        bouttonmenu.classList.remove('fa-xmark');
        bouttonmenu.classList.add('fa-bars');
    }
});