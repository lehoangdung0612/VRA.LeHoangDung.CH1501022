function BaiTap20()
    imgI = imread('cameraman.jpg');
    arrPointI = detectHarrisFeatures(imgI);
    [arrFeatureI, arrValidPointI] = extractFeatures(imgI, arrPointI);
    figure;
    imshow(imgI);
    arrSubValidPointI = arrValidPointI.selectStrongest(20);
    hold on;
    plot(arrSubValidPointI);
end