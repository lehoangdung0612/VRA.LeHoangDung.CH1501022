function Recognition004_Digits()
    fprintf('\n Load du lieu train');
    imgTrainAll = loadMNISTImages('D:/train-images.idx3-ubyte');
    lblTrainAll = loadMNISTLabels('D:/train-labels.idx1-ubyte');
    
    fprintf('\n Load du lieu test');
    imgTestAll = loadMNISTImages('D:/t10k-images.idx3-ubyte');
    lblTestAll = loadMNISTLabels('D:/t10k-labels.idx1-ubyte');
    
    nTrainImages = size(imgTrainAll, 2);
    nNumber = randi([1 nTrainImages]);
    figure,
    img = imgTrainAll(:, nNumber);
    img2D = reshape(img, 28, 28); % reshape
    strLabelImage = num2str(lblTrainAll(nNumber));
    strLabelImage = [strLabelImage, '(', num2str(nNumber), ')'];
    imshow(img2D); % show image
    title(strLabelImage);
    
    nTestImages = size(imgTestAll, 2);
    nNumber = randi([1 nTestImages]);
    figure,
    img = imgTestAll(:, nNumber);
    img2D = reshape(img, 28, 28); % reshape
    strLabelImage = num2str(lblTestAll(nNumber));
    strLabelImage = [strLabelImage, '(', num2str(nNumber), ')'];
    imshow(img2D); % show image
    title(strLabelImage);   
end