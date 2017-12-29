# Image Retrievel System

## web-client: web source based on Node JS
    - Template: Pug
    - Css, Javascript

## python-backend:
	- server code with PYTHON

### Node-JS

	* Node v8.9.1

	* How to run:
		- cd web-client
		- npm install
		- npm run watch (localhost:3000)

	* Config
		- Open file config.json
			pyAPI:
				search: API to search image, default is http://localhost:5000/search,
				upload: API to upload image, default is http://localhost:5000/file-upload
			externalUpload: enable to upload image to Python host, default is false,
			searchByAjax: enable to call ajax for searching images to Python host, default is true

### Python
	* Python 2.7.14
	
	* How to run
		- cd python-backend
		- python -m pip install -r requirements.txt
		- python index.py -> preprocess data train
		- python server.py -> start server (localhost:5000)

	* Config
		- Open file config.py
			Settings = {
				"SEARCH_RESULT" 		: 100				// number images are responsed
				, "MAX_FILES" 			: 100				// max length of images to train
				, "FEATURE" 			: "rootsift"		// type of feature
				, "ROOT_DATASET_FOLDER" : "dataset" 		// folder stored train images 
				, "TRAIN_DATASET"		: "oxford5k"		// name of subfolder in ROOT_DATASET_FOLDER
				, "FEATURE_FILE" 		: "features.bin"	// name of stored file
			}
			Features = {
				"SIFT"					: "sift"
				, "SURF"				: "surf"
				, "ROOTSIFT"			: "rootsift"
			}
			KMeans = {
				"TYPE"					: 1					// type of kmean function (1, 2 or 3)
				, "NUM_WORDS" 			: 100		     	// number of k
				, "ITER"				: 1					// number of iterations to run k-times
			}
			Resources = {
				"STATIC_FOLDER"			: "dataset/"
		        , "TEMPLATE_FOLDER"		: "templates/"
		        , "UPLOAD_FOLDER"		: "dataset/uploaded/"  // path to upload images (query)
		        , "IMAGE_PATH"			: "uploaded/"		   // path to images for displaying on web
			}
