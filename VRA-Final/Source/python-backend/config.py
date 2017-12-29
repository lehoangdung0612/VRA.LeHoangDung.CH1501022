# import the necessary packages
class Config:
    Settings = {
        "SEARCH_RESULT"         : 100
        , "MAX_FILES"           : 1000
        , "FEATURE"             : "sift"
        , "ROOT_DATASET_FOLDER" : "dataset"
        , "TRAIN_DATASET"       : "corel"
        , "FEATURE_FILE"        : "features.bin"
    }
    Features = {
        "SIFT"                  : "sift"
        , "SURF"                : "surf"
        , "ROOTSIFT"            : "rootsift"
    }
    KMeans = {
        "TYPE"                  : 1
        , "NUM_WORDS"           : 500
        , "ITER"                : 5
    }
    Resources = {
        "STATIC_FOLDER"         : "dataset/"
        , "TEMPLATE_FOLDER"     : "templates/"
        , "UPLOAD_FOLDER"       : "dataset/uploaded/"
        , "IMAGE_PATH"          : "uploaded/"
    }