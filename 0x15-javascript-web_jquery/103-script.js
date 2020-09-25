$(function () {
  const supported = [
    'ar', 'az', 'be', 'bg', 'bn', 'bs', 'cs', 'da', 'de', 'dz', 'el', 'en',
    'en-gb', 'en-us', 'es', 'et', 'fa', 'fi', 'fil', 'fr', 'he', 'hi', 'hr',
    'hu', 'hy', 'id', 'is', 'it', 'ja', 'ka', 'kk', 'km', 'ko', 'lb', 'lo',
    'lt', 'lv', 'mk', 'mn', 'ms', 'my', 'ne', 'no', 'pl', 'pt', 'ro', 'ru',
    'sk', 'sl', 'sq', 'sr', 'sv', 'sw', 'th', 'tk', 'uk', 'vi', 'zh'
  ];
  $('INPUT#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === 13) {
      $('INPUT#btn_translate').click();
    }
    event.stopPropagation();
  });
  $('INPUT#btn_translate').click(function () {
    var lang = $('INPUT#language_code').val().toLowerCase();
    if ($.inArray(lang, supported)) {
      const helloURL = `https://fourtonfish.com/hellosalut/?lang=${lang}`;
      $.getJSON(helloURL, function (Data) {
        $('DIV#hello').text(Data.hello);
      });
    }
  });
});
