
(function ($) {
  'use strict';

jQuery(document).ready(function($) {
  

  //OWL CAROUSEL VARIABLES

  var carousel_post_type3  = $('.carousel_post_type3');
  var carousel_post2_type3 = $('.carousel_post2_type3');
  var widget4_carousel     = $('.widget4_carousel');
  var carousel_posts1      = $('.carousel_posts1');
  var gicarousel           = $('.gicarousel');
  var feature_carousel     = $('.feature_carousel');
  var post_type2_carousel  = $('.post_type2_carousel');
  var single_mix_carousel  = $('.single_mix_carousel');
  var popular_carousel     = $('.popular_carousel');
  var sports_carousel      = $('.sports_carousel');
  var feature3_carousel    = $('.feature3_carousel');
  var business_carousel    = $('.business_carousel');
  var image_carousel       = $('.image_carousel');
  var science_carousel     = $('.science_carousel');
  var gallary_carousel     = $('.gallary_carousel');
  var top_carousel         = $('.top_carousel');
  var trancarousel         = $('.trancarousel');



    var stellarnav = $('.stellarnav');
    
    stellarnav.stellarNav({
      theme: 'light',
      breakpoint: 960,
      position: 'right',

    });


  trancarousel.owlCarousel({
    loop:true,
    nav:true,
    items:1,
    margin:30,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
    
  })

  top_carousel.owlCarousel({
    loop:true,
    nav:true,
    items:1,
    margin:30,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
  })



  if ($('.slider_demo2').length > 0) {
    var slider_demo2 = $('.slider_demo2');
    var slider_demo1 = $('.slider_demo1');
    slider_demo2.slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      fade: true,
      asNavFor: '.slider_demo1'
    });
    slider_demo1.slick({
      slidesToShow:7,
      slidesToScroll: 1,
      asNavFor: '.slider_demo2',
      dots: false,
      prevArrow:"<div class='slider_arrow arrow_left'><i class='fal fa-angle-left'></i></div>",
      nextArrow:"<div class='slider_arrow arrow_right'><i class='fal fa-angle-right'></i></div>",
      centerMode: true,
      focusOnSelect: true,
      responsive: [
        {
          breakpoint: 10000,
          settings: {
            slidesToShow: 7,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 1300,
          settings: {
            slidesToShow: 6,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 7,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        }
      ]
    });
  }

  
  if ($('.wlc_slider_demo2').length > 0) {
    
    var wlc_slider_demo2 = $('.wlc_slider_demo2');
    var wlc_slide_demo1  = $('.wlc_slide_demo1');

    wlc_slider_demo2.slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      fade: true,
      asNavFor: '.wlc_slide_demo1'
    });

    wlc_slide_demo1.slick({
      asNavFor: '.wlc_slider_demo2',
      dots: false,
      prevArrow:"<div class='slider_arrow4 arrow_left'><i class='fal fa-angle-left'></i></div>",
      nextArrow:"<div class='slider_arrow4 arrow_right'><i class='fal fa-angle-right'></i></div>",
      centerMode: true,
      focusOnSelect: true,
      dots: false,
      responsive: [
        {
          breakpoint: 10000,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });
  }


  gallary_carousel.owlCarousel({
    loop:true,
    nav:false,
    dots:true,
    margin:30,
    items:1,
  })

  science_carousel.owlCarousel({
    loop:true,
    nav:true,
    margin:30,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
    responsive:{
      0:{
        items:1
      },
      700:{
        items:2
      }
    }
  })


  image_carousel.owlCarousel({
    loop:true,
    nav:true,
    margin:30,
    items:1,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
  })


  business_carousel.owlCarousel({
    loop:true,
    nav:true,
    margin:30,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
    responsive:{
      0:{
        items:1
      },
      600:{
        items:1
      },
      1200:{
        items:2
      }
    }
  })

  feature3_carousel.owlCarousel({
    loop:true,
    nav:true,
    margin:30,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
    responsive:{
      0:{
        items:1
      },
      600:{
        items:3
      },
      1200:{
        items:3
      }
    }
  })

  sports_carousel.owlCarousel({
    items:1,
    loop:true,
    nav:true,
    margin:30,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
  })


  popular_carousel.owlCarousel({
    items:1,
    loop:true,
    nav:true,
    margin:30,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"]
  })

  single_mix_carousel.owlCarousel({
    loop:true,
    nav:true,
    margin:30,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
    responsive:{
      0:{
        items:1,
      },
      1000:{
        items:2
      }
    }
  })


  carousel_post_type3.owlCarousel({
    items:1,
    loop:true,
    nav:true,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"]
  })

  post_type2_carousel.owlCarousel({
    items:1,
    loop:true,
    nav:true,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"]
  })

  carousel_post2_type3.owlCarousel({

    loop:true,
    margin:30,
    nav:true,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
    responsive:{
      0:{
        items:1
      },
      800:{
        items:2
      }
    }
  })
  
  widget4_carousel.owlCarousel({
    items:1,
    loop:true,
    nav:true,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"]
  })

  carousel_posts1.owlCarousel({
    loop:true,
    nav:true,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
    responsive:{
      0:{
        items:1
      },
      600:{
        items:2
      },
      1000:{
        items:3
      }
    }
  })

  gicarousel.owlCarousel({
    loop:true,
    nav:true,
    margin:2,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
    responsive:{
      0:{
        items:3
      },
      600:{
        items:5
      },
      1000:{
        items:7

      }
    }
  })

  feature_carousel.owlCarousel({
    loop:true,
    nav:true,
    margin:2,
    margin:30,
    navText:["<i class=\'fal fa-angle-left\'></i>", "<i class=\'fal fa-angle-right\'></i>"],
    responsive:{
      0:{
        items:1
      },
      600:{
        items:2
      },
      1000:{
        items:3

      },
      1300:{
        items:4

      }
    }
  })


  var c4 = $('.first_circle.circle');
  c4.circleProgress({
    startAngle: -Math.PI / 4 * 3,
    value: 0.5,
    size: 36,
    thickness:4,
    lineCap: 'round',
    fill: {
      color: '#FF5555',
    }
  });

  var c4 = $('.second_circle.circle');
  c4.circleProgress({
    startAngle: -Math.PI / 4 * 3,
    value: 0.7,
    size: 36,
    thickness:4,
    lineCap: 'round',
    fill: {
      color: '#FF5555',
    }
  });

  var c4 = $('.third_circle.circle');
  c4.circleProgress({
    startAngle: -Math.PI / 4 * 3,
    value: 0.2,
    size: 36,
    thickness:4,
    lineCap: 'round',
    fill: {
      color: '#FF5555',
    }
  });

  var c4 = $('.fourth_circle.circle');
  c4.circleProgress({
    startAngle: -Math.PI / 4 * 3,
    value: 0.5,
    size: 36,
    thickness:4,
    lineCap: 'round',
    fill: {
      color: '#FF5555',
    }
  });

  var c4 = $('.fifth_circle.circle');
  c4.circleProgress({
    startAngle: -Math.PI / 4 * 3,
    value: 0.4,
    size: 36,
    thickness:4,
    lineCap: 'round',
    fill: {
      color: '#FF5555',
    }
  });



  var search4        = $('.search4');
  var search4_close  = $('.search4_close');
  var searching_area = $('.searching_area');

  search4.on('click', function(){
    searching_area.addClass('active');
  })

  search4_close.on('click', function(){
    searching_area.removeClass('active');
  })

  var play_btn = $(".play_btn");
  play_btn.modalVideo();

  var search_btn = $('.search_btn');
  var searching = $('.searching');
  var close_btn = $('.close_btn');

  search_btn.on('click', function(){
    searching.addClass('active');
  });

  close_btn.on('click', function(){
     searching.removeClass('active');
  })


   

    if ($('#header').length > 0) {
      function fixed_nav(){
        window.onscroll = function() {myFunction()};
        
        var header = document.getElementById("header");
        var sticky = header.offsetTop;

        function myFunction() {
          if (window.pageYOffset > sticky) {
            header.classList.add("sticky");
          } else {
            header.classList.remove("sticky");
          }
        }
      };
      fixed_nav();
    }else{
      return false;
    }

    /*

    if ($('#scroll').length > 0) {

      var scrollers = $('#scroll a[href*="#"], a.up_btn');


      scrollers.on('click', function(e) {
        e.preventDefault()

        $('html, body').animate(
          {
            scrollTop: $($(this).attr('href')).offset().top
          },
          1000,
          'linear'
        )
      })

    }else{
      return false;
    }
*/

/*    if ($('img').length > 0) {

        var img = $('img');
        img.each(function() {
          $(this).width(($(this).width()/2));
          $(this).height(($(this).height()/2));
      });

    }else{
      return false;
    }

     */



 });



  //JQUERY LOEAD FUNCTION
  jQuery(window).on("load", function() {
     
      function handlePreloader() {
          var preloader = $('.preloader');
          if(preloader.length){
          preloader.delay(200).fadeOut(500);
          }
      }
      handlePreloader(); 
  });


}(jQuery));
