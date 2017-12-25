var express = require('express');
var path 	= require('path');
var router 	= require('./router/router');

var app = express();

app.use(express.static(path.join(__dirname, '/public')));
app.use('/', router);
app.set('views', __dirname + '/views');
app.set('view engine', 'pug');

var server = app.listen(process.env.PORT || 3000, function () {
  console.log('Listening on http://localhost:' + (process.env.PORT || 3000))
});
