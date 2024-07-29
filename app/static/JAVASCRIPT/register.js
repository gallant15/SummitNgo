const password1 = document.querySelector("#password1")
const password2 = document.querySelector("#password2")

const message = document.querySelector(".message")
const explorer = document.querySelector(".explorer")


const toggle = document.querySelector(".toggle")
const toggle2 = document.querySelector(".toggle2")


// addEventListener

toggle.addEventListener("click", toggleEvent1);
toggle2.addEventListener("click", toggleEvent2);
explorer.addEventListener("click", pwdvalidation);



function toggleEvent1(){
    const p1 = password1.getAttribute("type") === "password" ? "text" : "password"
    password1.setAttribute("type", p1)


    this.classList.toggle("fa-eye-slash");
}

function toggleEvent2(){
    const p2 = password2.getAttribute("type") === "password" ? "text" : "password"
    password2.setAttribute("type", p2)


    this.classList.toggle("fa-eye-slash");
}


// function pwdvalidation(){
//     var password1 = document.getElementById("password1").value
//     var password2 = document.getElementById("password2").value
//     console.log(password1)
//     console.log(password2)

//     if (password1 == password2){
//         message.classList.add("alert-sucess")
//         message.innerHTML = "Password Match"
//     }
//     else{
//         message.innerHTML = "Password Don't Match"
//     }
// }