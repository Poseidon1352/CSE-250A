function [u,v,x,y] = proc_dir(dr,c,r,siz)
if dr == 0
    v = (r + 0.5)*siz; y = 0;
    u = (c+1)*siz; x = -siz;
elseif dr == 1
    v = (r+1)*siz; y = -siz;
    u = (c+0.5)*siz; x = 0;
elseif dr == 2
    v = (r+0.5)*siz; y = 0;
    u = c*siz; x = siz;
else
    v = r*siz; y = siz;
    u = (c+0.5)*siz; x = 0;
end 