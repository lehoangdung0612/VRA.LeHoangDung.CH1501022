function Recognition001_Digits()
    fprintf('\n Load du lieu train');
    imgTrainAll = loadMNISTImages('D:/train-images.idx3-ubyte');
    lblTrainAll = loadMNISTLabels('D:/train-labels.idx1-ubyte');
    
    fprintf('\n Load du lieu test');
    imgTestAll = loadMNISTImages('D:/t10k-images.idx3-ubyte');
    lblTestAll = loadMNISTLabels('D:/t10k-labels.idx1-ubyte');
    
    fprintf('\n Ket thuc.\n');
end