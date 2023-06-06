# Fake_News_Detection_Software
<!DOCTYPE html>
<html>
<head>
    <title>Fake News Detection</title>
</head>
<body>
    <h1>Fake News Detection</h1>
    <form id="prediction-form">
        <textarea id="text-input" rows="4" cols="50"></textarea>
        <button type="submit">Predict</button>
    </form>
    <div id="prediction-result"></div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $('#prediction-form').submit(function(e) {
                e.preventDefault();
                var inputData = $('#text-input').val();

                $.ajax({
                    url: '/predict',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ 'text': inputData }),
                    success: function(response) {
                        $('#prediction-result').text('Prediction: ' + response.prediction);
                    },
                    error: function(xhr, status, error) {
                        $('#prediction-result').text('Error: ' + xhr.responseJSON.error);
                    }
                });
            });
        });
    </script>
</body>
</html>
