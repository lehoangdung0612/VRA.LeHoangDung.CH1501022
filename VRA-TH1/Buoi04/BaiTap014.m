function BaiTap014()
    strData='train-images.idx3-ubyte';
    strDataLabel='train-labels.idx1-ubyte';
    [imgDataTrain,lblDataTrain]=loadData(strData,strDataLabel);
    
    imgI1D=imgDataTrain(:,1);
    imgI2D=reshape(imgI1D,28,28);
    
    featuresVector=extractHOGFeatures(imgI2D);
    nSize=length(featuresVector);
    nTrainData=size(imgDataTrain,2);
    
    featuresDataTrain=zeros(nSize,nTrainData);
    for i=1:nTrainData
        imgI1D=imgDataTrain(:,i);
        imgI2D=reshape(imgI1D,28,28);
        featuresDataTrain(:,i)=extractHOGFeatures(imgI2D);
    end
    
    Mdl=fitcknn(featuresDataTrain',lblDataTrain);
    
    %% Load Data Test
    strData='t10k-images.idx3-ubyte';
    strDataLabel='t10k-labels.idx1-ubyte';
    [imgDataTest, lblDataTest]=loadData(strData,strDataLabel);
    
    imgI1D=imgDataTest(:,1);
    imgI2D=reshape(imgI1D,28,28);
    
    featuresVector=extractHOGFeatures(imgI2D);
    nSize=length(featuresVector);
    nTestData=size(imgDataTest,2);
    
    featuresDataTest=zeros(nSize,nTestData);
    for i=1:nTestData
        imgI1D=imgDataTest(:,i);
        imgI2D=reshape(imgI1D,28,28);
        featuresDataTest(:,i)=extractHOGFeatures(imgI2D);
    end
    
    
    %% Save Result
    
    lblResult=predict(Mdl,featuresDataTest');
    nResult=(lblResult==lblDataTest);
    nCount=sum(nResult);
    fprintf('\n So luong mau khop dung: %d\n',nCount);
    a=size(lblDataTest);
    k=(nCount\a*100);
 
end