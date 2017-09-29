function Recognition003_Digits()
    fprintf('\n Load du lieu train');
    imgTrainAll = loadMNISTImages('D:/train-images.idx3-ubyte');
    lblTrainAll = loadMNISTLabels('D:/train-labels.idx1-ubyte');
    
    fprintf('\n Load du lieu test');
    imgTestAll = loadMNISTImages('D:/t10k-images.idx3-ubyte');
    lblTestAll = loadMNISTLabels('D:/t10k-labels.idx1-ubyte');
    
    nTrainImages = size(imgTrainAll, 2);
    
    figure,
    img = imgTrainAll(:, 1);
    img2D = reshape(img, 28, 28); % reshape
    strLabelImage = num2str(lblTrainAll(1));
    imshow(img2D); % show image
    title(strLabelImage);
    
    figure,
    imgLast = imgTrainAll(:, nTrainImages);
    img2DLast = reshape(imgLast, 28, 28); % reshape
    strLabelImage = num2str(lblTrainAll(nTrainImages));
    imshow(img2DLast); % show image
    title(strLabelImage);   
end