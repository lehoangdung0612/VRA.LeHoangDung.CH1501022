function Example001()
    a = rand();
    fprintf('\n 1. Tao ngau nhien mot so thuc trong doan [0..1]: [%8.3f]', a);
    
    r = randi([1 10]);
    fprintf('\n 2. Tao ngau nhien mot so nguyen trong doan [1 10]: [%d]', r);
    
    rArray = randi([-10 10], 1, 10);
    fprintf('\n 3. So cot cua ma tran: %d.', size(rArray, 2));
    fprintf('\n Mang duoc tao la: ');
    fprintf('[%2d]', rArray);
end
    
    