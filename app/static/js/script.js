
$(document).ready(function(){
    $("#predict").click(
    function predict(event) {
        var selectors = ["category"];
        var values = selectors.map((sel)=>document.getElementById(sel).value);
        console.log(values);
        var urlPrefix;
        if(window.location.port) {
            urlPrefix = window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + window.location.pathname
        } else {
            urlPrefix = window.location.protocol + '//' + window.location.hostname + window.location.pathname + "/"
        }
        console.log(urlPrefix);
        $.ajax({
            url: urlPrefix+"prediction",
            type: "POST",
            data: {
              category : values[0]
            },
            success: function(response) {
                var output = $("#output");
                output.html(null);
                output.append('<table  id="compactTable" class="table">    <thead class="thead-light"> <tr>  <th>Result</th>  </tr>  </thead>  <tbody>')
                for(var i =0; i < response.length; i++){

                output.append('<li class="list-group-item">'+response[i]+'</li>');


                 }
                 output.append('</tbody> </table>')
                console.log(response);
            },
            error: function(response) {
                console.log("===== ERROR =====");
                console.log(response);
            }
        });
        event.preventDefault();
    });
});
