function BaiTap027
    [imgTrainAll, lblTrainAll] = loadData('train-images.idx3-ubyte', 'train-labels.idx1-ubyte');
	
	nBins = 256;
	nTrainImages = size(imgTrainAll, 2);
	imgTrainAll_hist = zeros(nBins, nTrainImages);
	for i=1:nTrainImages
		imgTrainAll_hist(:, i) = imhist(imgTrainAll(:, i), nBins);
	end

	Mdl = fitcecoc(imgTrainAll_hist', lblTrainAll);
    
    [imgTestAll, lblTestAll] = loadData('t10k-images.idx3-ubyte', 't10k-labels.idx1-ubyte');
   
   	nTestImages = size(imgTestAll, 2);
    imgTestAll_hist = zeros(nBins, nTestImages);
    for i=1:nTestImages
		imgTestAll_hist(:, i) = imhist(imgTestAll(:, i), nBins);
	end

    lblResult = predict(Mdl, imgTestAll_hist');
	nResult = (lblResult == lblTestAll);
    nCount = sum(nResult);
    fprintf('\nSo luong mau dung: %d\n', nCount);
end