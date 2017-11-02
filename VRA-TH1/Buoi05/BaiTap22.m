function BaiTap22()
    imgI = imread('cameraman.jpg');
    arrPointI = detectHarrisFeatures(imgI);
    imgJ = imread('cameraman30.jpg');
    arrPointJ = detectHarrisFeatures(imgJ);
    
    [arrFeatureI, arrValidPointI] = extractFeatures(imgI, arrPointI);
    [arrFeatureJ, arrValidPointJ] = extractFeatures(imgJ, arrPointJ);
    
    arrIndexPair = matchFeatures(arrFeatureI, arrFeatureJ);
    arrMatchedPointI = arrValidPointI(arrIndexPair(:,1),:);
    arrMatchedPointJ = arrValidPointJ(arrIndexPair(:,2),:);
    
    figure;
    ax = axes;
    showMatchedFeatures(imgI, imgJ, arrMatchedPointI, arrMatchedPointJ, 'montage', 'Parent', ax);
    title(ax, 'Candidate point matches');
    legend(ax, 'Matched point I', 'Matched point J');
end