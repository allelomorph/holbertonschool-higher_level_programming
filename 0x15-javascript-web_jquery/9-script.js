$.ajax({
  url: 'http://jsonip.com?callback=?',
  dataType: 'json',
  success: function (ipData) {
    const lang = navigator.language;
    const ip = ipData.ip;
    const helloURL = `https://fourtonfish.com/hellosalut/?lang=${lang}&ip=${ip}`;
    $.getJSON(helloURL, function (helloData) {
      $('DIV#hello').text(helloData.hello);
    });
  }
});
