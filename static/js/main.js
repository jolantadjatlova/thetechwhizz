document.addEventListener('DOMContentLoaded', function() {
    var testimonialsLink = document.querySelector('a[href="/#testimonials"]');
    if (testimonialsLink) {
        testimonialsLink.addEventListener('click', function(e) {
            var target = document.getElementById('testimonials');
            if (target) {
                e.preventDefault();
                var top = target.getBoundingClientRect().top + window.scrollY - 20;
                window.scrollTo({ top: top, behavior: 'smooth' });
            }
        });
    }
});