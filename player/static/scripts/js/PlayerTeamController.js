function PlayerTeamController(player) {
        this.player = player;
        this.submitAjaxRequest = function(){
        $.ajax({
        url : "playerteams", // the endpoint
        type : "GET", // http method
        //data : { the_post : $('#post-text').val() },

        // handle a successful response
        success : function( data ) {
            console.log( data ); // log the returned json to the console

            $( "#player_teams_info" ).replaceWith(data);

            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            alert("Encountered error while submitting ajax request for player team info.");
        }
    });

    };

$('#create-team-button').click(function(event)
{
   $.ajax({
        url : "createnewteam", // the endpoint
        type : "GET", // http method
        //data : { the_post : $('#post-text').val() },

        // handle a successful response
        success : function( data ) {
            console.log( data ); // log the returned json to the console

            $( "#create-new-team-form" ).replaceWith(data);

            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            alert("Encountered error while submitting ajax request for player team info.");
        }
    });
});
}