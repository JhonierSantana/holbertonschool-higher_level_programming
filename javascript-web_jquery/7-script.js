
$.getJSON('https://swapi-api.hbtn.io/api/people/6/?format=json', (data) => {
    $('DIV#character').text(`${data.name}`);
});