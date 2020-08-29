$('[data-toggle="slide-collapse"]').on('click', function() {
  let $navMenuCont = $($(this).data('target'));
  $navMenuCont.animate({
    'width': 'toggle'
  }, 350);
});