function BaiTap015()
    strData='train-images.idx3-ubyte';
    strDataLabel='train-labels.idx1-ubyte';
    [imgDataTrain,lblDataTrain]=loadData(strData,strDataLabel);
         
    [featuresDataTrain,visualHog]=extractFeaturesHog(imgDataTrain,'CellSize',[2 2]); %%
       
    Mdl=fitcknn(featuresDataTrain',lblDataTrain);
    
    %% Load Data Test
    strData='t10k-images.idx3-ubyte';
    strDataLabel='t10k-labels.idx1-ubyte';
    [imgDataTest, lblDataTest]=loadData(strData,strDataLabel);
    
    featuresDataTest=extractFeaturesHog(imgDataTest);
       
   
    %% Save Result
    
    lblResult=predict(Mdl,featuresDataTest');
    nResult=(lblResult==lblDataTest);
    nCount=sum(nResult);
    fprintf('\n So luong mau khop dung: %d\n',nCount);
     
end