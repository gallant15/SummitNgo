const mainMenu = document.querySelector('.mainMenu');
const closeMenu = document.querySelector('#closemenu');
const openMenu = document.querySelector('#openmenu');




function show(){
    mainMenu.style.display = 'flex';
    mainMenu.style.top = '0';
    
    closeMenu.style.display = "block"
    openMenu.style.display = "none"
}
function close(){
    mainMenu.style.top = '-100%';
    closeMenu.style.display = "none"
    openMenu.style.display = "block"

}

closeMenu.addEventListener('click', close);
openMenu.addEventListener('click', show);
