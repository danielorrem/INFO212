function transfer_new() {
    $('#qrcode').html('');
}

$('#lithird').click(function() {

    var qrcode = new QRCode("qrcode");

    function makeCode() {

        function randomNumber(len) {
            var randomNumber;
            var n = '';

            for (var count = 0; count < len; count++) {
                randomNumber = Math.floor(Math.random() * 10);
                n += randomNumber.toString();
            }
            return n;
        }

        var value = randomNumber(13);

        var elText = value;

        qrcode.makeCode(elText);
    }

    makeCode();

});