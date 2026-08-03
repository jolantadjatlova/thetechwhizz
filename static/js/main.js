document.addEventListener('DOMContentLoaded', function () {
    var navbarCollapse = document.getElementById('navbarNav');
    if (!navbarCollapse) return;

    var navLinks = navbarCollapse.querySelectorAll('.nav-link:not(.dropdown-toggle), .dropdown-item');

    navLinks.forEach(function (link) {
        link.addEventListener('click', function () {
            if (navbarCollapse.classList.contains('show')) {
                var bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse) || new bootstrap.Collapse(navbarCollapse, { toggle: false });
                bsCollapse.hide();
            }
        });
    });
});

function setNavbarOffset() {
    var nav = document.querySelector('.site-navbar');
    if (!nav) return;
    var navHeight = nav.offsetHeight;
    document.body.style.paddingTop = navHeight + 'px';
    document.documentElement.style.setProperty('--navbar-height', navHeight + 'px');
}

window.addEventListener('load', setNavbarOffset);
window.addEventListener('resize', setNavbarOffset);