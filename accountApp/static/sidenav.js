const dashb = document.getElementById('dashb');
const subj = document.getElementById('item');

function activeSubject() {
    subj.classList.add("active");
    dashb.classList.remove("active");
    localStorage.setItem("clicked", true);
}
function activeDashb() {
    dashb.classList.add("active");
    localStorage.removeItem("clicked");
}

window.onload = function () {
    var subject = localStorage.getItem('clicked');
    
    if (subject == 'true') {
        activeSubject();
    }
    else {
        activeDashb();
    }
};