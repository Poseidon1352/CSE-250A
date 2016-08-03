dr = [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 3, 3, 2, 0, 0, 2, 0, 3, 3, 0, 0, 2, 0, 0, 3, 3, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 3, 3, 3, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
img = imread('mazePlain.jpg');
imshow(img)
hold on
for i = 1:81
    c = floor(i/9); r = mod(i-1,9);
    [u,v,x,y] = proc_dir(dr(i),c,r,67);
    quiver(u,v,x,y,'LineWidth',2,'color','r','MaxHeadSize',4);
end
set(gca,'position',[0 0 1 1],'units','normalized')