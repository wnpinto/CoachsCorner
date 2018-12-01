function PlayerController(player) {
        this.player = player;
        this.submitAjaxRequest = function(){
            $.ajax({
                url : "playerinfo",
                type : "GET",
                //data : { the_post : $('#post-text').val() },

                // handle a successful response
                success : function( data ) {
                            console.log( data ); // log the returned json to the console

                            $( "#player_info" ).replaceWith(data);

                            console.log("success player info"); // another sanity check
                },

                // handle a non-successful response
                error : function(xhr,errmsg,err) {
                            alert("Encountered error while submitting ajax request for player info.");
                }
            });

        };
};

