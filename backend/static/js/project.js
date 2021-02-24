/* Project specific Javascript goes here. */


$(document).ready(function(){

  $('input[class="datetimeinput form-control"]').attr("type", "search").attr("autocomplete", "off") ;
  $('input[class="datetimeinput form-control"]').daterangepicker({
    autoUpdateInput: false,
    locale : {"format" : "DD/MM/YYYY"},
    opens: 'left'
  });

 $('input[class="datetimeinput form-control"]').on('apply.daterangepicker', function(ev, picker) {
      $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
  });

    const urlParams = new URLSearchParams(window.location.search);
    const date = urlParams.get('date') ;
    const dueDate = urlParams.get('due_date')
    $('input[name="date"]').val(date);
    $('input[name="due_date"]').val(dueDate);

});
