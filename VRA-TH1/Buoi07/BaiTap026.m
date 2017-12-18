function BaiTap026
    [imgTrainAll, lblTrainAll] = loadData('train-images.idx3-ubyte', 'train-labels.idx1-ubyte');
    
    %% fitcecoc: xay dung mot siêu ph?ng
    Mdl = fitcecoc(imgTrainAll', lblTrainAll);
    
    [imgTestAll, lblTestAll] = loadData('t10k-images.idx3-ubyte', 't10k-labels.idx1-ubyte');
    lblResult = predict(Mdl, imgTestAll');
    nResult = (lblResult == lblTestAll);
    nCount = sum(nResult);
    fprintf('\nSo luong mau dung: %d\n', nCount);
end