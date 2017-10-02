function savenprime(n)
    rArray = findnprime(n);
    strFileName = ['D:\prime', num2str(n), '.mat'];
    save(strFileName, 'rArray');
end