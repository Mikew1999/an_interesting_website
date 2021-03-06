$(document).ready(function(){
    // Pushes main section down below navbars
    function setPaddingMain() {
        let main = $('#main');
        main.css('margin-top', $('#top-nav').height());
        let mainHeight = $(window).height() - $('#top-nav').height();
        main.css('min-height', mainHeight);
    }
    setPaddingMain();

    // Shows back to top button on all pages if scrolled down
    $(window).scroll(function(){
        scrollToTop = $('#scroll-top');
        if ($(window).scrollTop() > 200) {
            scrollToTop.css('display', 'block');
        }
        else {
            scrollToTop.css('display', 'none');
        }
    })

    // Scrolls to top of page
    $('#scroll-top-button').click(function(){
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    })
})