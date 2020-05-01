function CarouselRight(){
    $('.carousel.carousel-slider').carousel('next');
    clearTimeout(carouselTimeout);
    carouselTimeout = setTimeout(autoplay, 10000, false);
}
function CarouselLeft(){
    $('.carousel.carousel-slider').carousel('prev');
    clearTimeout(carouselTimeout);
    carouselTimeout = setTimeout(autoplay, 10000, false);
}
function autoplay(isFirst) {
    if (!isFirst) $('.carousel').carousel('next');
    carouselTimeout = setTimeout(autoplay, 10000, false);
}