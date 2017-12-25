# import the necessary packages
class Config:
	Settings = {
		"SEARCH_THRESHOLD" 		: 0.7
		, "MAX_FILES" 			: 500
		, "FEATURE" 			: "sift"
		, "ROOT_DATASET_FOLDER" : "dataset"
		, "TRAIN_DATASET"		: "oxford5k"
		, "FEATURE_FILE" 		: "features.bin"
	}
	Features = {
		"SIFT"					: "sift"
		, "SURF"				: "surf"
		, "ROOTSIFT"			: "rootsift"
	}
	KMeans = {
		"TYPE"					: 1
		, "NUM_WORDS" 			: 100
		, "ITER"				: 1
	}
	Resources = {
		"STATIC_FOLDER"			: "dataset/"
        , "TEMPLATE_FOLDER"		: "templates/"
        , "UPLOAD_FOLDER"		: "dataset/uploaded/"
        , "IMAGE_PATH"			: "uploaded/"
	}