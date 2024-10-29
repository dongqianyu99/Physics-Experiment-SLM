clc,
clear all;
N = 500; res = 1e-6;
X = -N/2:N/2-1; Y = -N/2:N/2-1;
[x0,y0] = meshgrid(X*res,Y*res);
fx = -1/(2*res):1/(N*res):1/(2*res)-1/(N*res);
fy = fx;
[Fx,Fy] = meshgrid(fx,fy);
lam = 0.6328e-6; k =2*pi/lam;
f0 =  5e-3;
R = 1e-3; 
deltaf = 0;
f  = f0+deltaf/R*sqrt(x0.^2+y0.^2);

Ain = 1;
% Ein = Ain*exp(-1i*(pi/(lam))*(sqrt(x0.^2+y0.^2+f0^2)-f0));
Ein = Ain*exp(-1i*(pi/(lam))*((x0.^2+y0.^2)./f));
Nslid =  150;
zd = 0.001+linspace(0,0.005,150);
A1 = zeros(N,N,Nslid);
Exy = zeros(N,N,Nslid);
Eyz = zeros(N,Nslid);
figure('color','white')

for slid = 1:1:Nslid
    [xout,yout] = meshgrid(lam*zd(slid)*fx,lam*zd(slid)*fy);    
    F0(:,:,slid) = exp(1i*k*zd(slid))/(1i*lam*zd(slid))*exp(1i*k/2/zd(slid)*(xout.^2+yout.^2));    
    F(:,:,slid) = exp(1i*pi/(lam*zd(slid)).*(x0.^2+y0.^2));    
    Exy(:,:,slid) = abs(F0(:,:,slid).*fftshift(fft2(fftshift(Ein.*F(:,:,slid)))));    
    Eyz(:,slid)=Exy(N/2+1,:,slid);
    
    subplot 211;  imagesc(xout(1,:),yout(:,1),Exy(:,:,slid));    
    colormap("jet");xlabel('X');ylabel('Y')    
    axis equal;    
    subplot 212; imagesc(zd,yout(:,1),Eyz);

    subplot(2,1,2)    
    colormap("jet");xlabel('Z');ylabel('Y')    
    %           axis equal    
    pause(eps)
end