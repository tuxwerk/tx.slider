function tx_slide_remove() {
  if (!window.confirm($(this).attr('data-confirm-text')))
    return false;

  $.get($(this).attr('href') + '?ajax=true', {}, function(data, status) { });
  $(this).closest("li").remove();
  return false;
}

function tx_slide_sortable() {
  $("#tx-slider-widget ul").sortable({
    items: 'li',
    placeholder: 'sortable-placeholder',
    forcePlaceholderSize: true,
    update: function(event, ui) {
      var order = [];
      var slides = $('#tx-slider-widget li');
      for(var i=0; i<slides.length; i++){
        order.push(slides.eq(i).attr('data-index'));
      }
      $.ajax({
        url: $('#tx-slider-widget').attr('data-order-slides-url'),
        type: 'POST',
        data: {
          order: order
        }
      }); 
    }
  });
}

$(document).ready(function(){
  $("#tx-slider-widget a.tx-slide-remove").click(tx_slide_remove);
  tx_slide_sortable();
  // $('.slide-buttons a.slide-edit, .slide-add-buttons a.slide-add').prepOverlay({
  //   subtype: 'ajax',
  //   filter: '#content>*',
  //   formselector: 'form',
  //   config:{expose:{color:'#00f'}}
  // });
});
