var express 	= require('express');
var path 		= require('path');
var bodyParser 	= require('body-parser');
var formidable 	= require('formidable');
var util 		= require('util');
var request 	= require('request');
var fs 			= require('fs-extra');
var config 		= require('../config.json');

var router 		= express.Router();

router.use(bodyParser.urlencoded({ extended: false }));
router.use(bodyParser.json());

router.get('/', function(req, res) {
    try {
    	res.render('index', { 
    		title: 'Home',
    		urlAction: config.externalUpload ? config.pyAPI.upload : '/file-upload',
    		urlSearch: config.externalUpload ? config.pyAPI.search : null,
    		externalUpload: config.externalUpload,
    		searchByAjax: config.searchByAjax
    	});
    } catch (e) {
        console.log('Request error: ', e);
    }
});

/// Request to upload file to this host, not call api
//
router.post('/file-upload', function(req, res) {
    try {
		// creates a new incoming form.
		var httpOrigin = req.get('origin');
		var form = new formidable.IncomingForm();
		//parse a file upload
		form.parse(req, function(err, fields, files) {
        	res.render('partials/image-viewer', {
        		urlAction: config.searchByAjax ? config.pyAPI.search : '/search',
        		imgPath: httpOrigin + '/uploaded/' + files.file.name,
        		imgFile: httpOrigin + '/uploaded/' + files.file.name,
        		searchByAjax: config.searchByAjax
        	});
		});

		form.on('end', function() {
			var temp_path = this.openedFiles[0].path;
			var file_name = this.openedFiles[0].name;
			var new_location = path.join(__dirname, '../public/uploaded/');
			fs.copy(temp_path, new_location + file_name, function(err) {  
			    if (err) {
			        console.error(err);
			    } else {
			        console.log("Upload successfully!")
			    }
			});
		});
		return;
    } catch (e) {
        console.log('Request error: ', e);
    }
});

router.post('/search', function(req, res) {
    try {
    	var options = {};
    	options.q = req.body.q;
    	options.cx = req.body.cx;
    	options.cy = req.body.cy;
    	options.cw = req.body.cw;
        options.ch = req.body.ch;
    	options.feature = req.body.feature;
    	request.post(config.pyAPI.search, { form: options }, function (error, response, body) {
			if (!error && response.statusCode == 200) {
				var result = JSON.parse(body);
				if (result.error) {
                    res.render('result', { data: [] });
				} else {
        			res.render('result', { data: result.data });
				}
			}
		})
		return;
    } catch (e) {
        console.log('Request error: ', e);
    }
});




module.exports = router;