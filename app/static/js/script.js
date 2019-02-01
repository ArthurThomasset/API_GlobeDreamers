const vm = new Vue({
          el: '#app',
          data: {
          results: [],
          titles: [],
          tests: ["titre1", "titre2"],
          category: '',
          code_postal: ''

        },
        methods: {

          Search(){  // fonction de recherche 1 avec Catégorie et code postal
            console.log("GO")

                    var urlPrefix;
                    if(window.location.port) {
                        urlPrefix = window.location.protocol + '//' + window.location.hostname + ":" + window.location.port + window.location.pathname
                    } else {
                        urlPrefix = window.location.protocol + '//' + window.location.hostname + window.location.pathname + "/"
                    }

                    console.log(urlPrefix)

                    urlPrefix = "http://127.0.0.1:5000/"    // URL de l'api (serveur ou elle tournera)
                    const bodyFormData = new FormData();
                    bodyFormData.append('category', vm.category);

                    bodyFormData.append('code_postal',vm.code_postal);


                    axios({

                    url: urlPrefix+ 'prediction',
                    method: 'post',
                    headers: {'Content-Type' : 'application/x-www-form-urlencoded'},

                    data: bodyFormData

                })
                    .then(function(response){
                        vm.results  = response.data;


                        console.log(vm.results)
                        console.log(vm.results[0][0][7])
                        console.log(vm.results.length)

                        var mytitles = [];
                        for(var i=0; i< vm.results.length;i++)
                        {
                          mytitles.push(vm.results[i][0][7]);
                        }

                        vm.titles = mytitles;

                      document.getElementById('result').style.display='block';

                        console.log(vm.titles);
                        console.log("title length : "+ vm.titles.length);
                      }).catch(function (error) {

                        console.log(error);
                      })

                    event.preventDefault();

          },

          Search2(){

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
                output.append('<table  id="compactTable" class="table">    <thead class="thead-light"> <tr>  <th>Propects potentiels : </th>  </tr>  </thead>  <tbody>')
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


          },

          ExportCSV(){
            console.log("export csv");
            var dataURL = '';
            var dataRow = '';


                for(var i=0; i< vm.results.length;i++)
                {
                    dataRow = vm.results[i][0][7] + ";" + vm.results[i][0][3] + ";" + vm.results[i][0][0] + ";" + vm.results[i][0][4] + ";" + vm.results[i][0][9] + ";" ;
                    dataURL += dataRow + '\n';
                    dataRow = '';
                }


            $('.btn').attr('href', 'data:text/csv;charset=utf-8;base64,' + btoa(dataURL));
        }


        },
        mounted() {} // Don't touch 
      });
