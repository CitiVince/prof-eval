$(function () {
    $(document).ready(function() {

        $('#CommentForm').submit(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: 'POST', // GET or POST
                async: false,
                url: '/add_comment/', // the file to call
                success: function(response) { // on success..
                    $('#comment_container').html(response);
                     // update the DIV
                },

            });

            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: 'POST', // GET or POST
                async: false,
                url: '/update_profrating/', // the file to call
                success: function(response) { // on success..
                    $('#rating').html(response);
                     // update the DIV
                },

            });
            return false;
        });

        $('body').ajaxComplete(function() {
              $('#rateButton').modal('hide')
            });
        
      $(function() {
            $( "#slider_easiness" ).slider(
                { max: 100 ,
                 min: 0 ,
                slide: function( event, ui ) {
                $( "#amount_easiness" ).val(ui.value);}
                });

            $( "#amount_easiness" ).val($( "#slider_easiness" ).slider( "value") );

            $( "#slider_clarity" ).slider(
                { max: 100 ,
                 min: 0 ,
                slide: function( event, ui ) {
                $( "#amount_clarity" ).val(ui.value);}
                });

            $( "#amount_clarity" ).val($( "#slider_clarity" ).slider( "value") );

            $( "#slider_interesting" ).slider(
                { max: 100 ,
                 min: 0 ,
                slide: function( event, ui ) {
                $( "#amount_interesting" ).val(ui.value);}
                });

            $( "#amount_interesting" ).val($( "#slider_interesting" ).slider( "value") );

            $( "#slider_niceness" ).slider(
                { max: 100 ,
                 min: 0 ,
                slide: function( event, ui ) {
                $( "#amount_niceness" ).val(ui.value);}
                });

            $( "#amount_niceness" ).val($( "#slider_niceness" ).slider( "value") );
            });
             

    });    
});