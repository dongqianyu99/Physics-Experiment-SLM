clc,
clear all;
N = 512;
res = 8e-8;
X = -N/2:N/2-1; 
Y = -N/2:N/2-1;
[x0,y0] = meshgrid(X*res,Y*res);

fx = -1/(2*res):1/(N*res):1/(2*res)-1/(N*res);
fy = fx;
[Fx,Fy] = meshgrid(fx,fy);
lam = 0.532e-9; k =2*pi/lam;
f = 0.5; 

i = imread("triangle_aperture.png");
lev = graythresh(i);
u = im2bw(i, lev);
z1 = 0.4;
a0 = 0.2;
x2 = 0: 1: 511;
y2 = 0: 1: 511;
for i = 1: 1: 512
    for j = 1: 1: 512
        %r(i, j) = sqrt((x2(i) - 216)^2 + (y2(j) - 216)^2 + z1^2);
        U1(i, j) = a0 * exp((-1)^(1/2) * k * z1);
    end
end
Ein = U1.*u;

%Ein = Ain*exp(-1i*(pi/(lam))*((x0.^2+y0.^2)./f)); 

Nslid =  1000;
zd = 0.1+linspace(0,0.3,1000);
A1 = zeros(N,N,Nslid);
Exy = zeros(N,N,Nslid);
Eyz = zeros(N,Nslid);
figure('color','white')


% for slid = 1:1:Nslid
%     [xout,yout] = meshgrid(lam*zd(slid)*fx,lam*zd(slid)*fy);    
%     F0(:,:,slid) = exp(1i*k*zd(slid))/(1i*lam*zd(slid))*exp(1i*k/2/zd(slid)*(xout.^2+yout.^2));  
%     F(:,:,slid) = exp(1i*pi/(lam*zd(slid)).*(x0.^2+y0.^2));    
%     Exy(:,:,slid) = abs(F0(:,:,slid).*fftshift(fft2(fftshift(Ein.*F(:,:,slid)))))^2;    
%     Eyz(:,slid)=Exy(1,:,slid);
% 
%     imagesc(zd,yout(:,1),Eyz);
%     colormap("hot");
%     xlabel('Z');
%     ylabel('Y')    
%     %           axis equal 
%     pause(eps)
% 
% end

z0 = 0.007;
[xout,yout] = meshgrid(lam*z0*fx,lam*z0*fy);    
F0(:,:) = exp(1i*k*z0)/(1i*lam*z0)*exp(1i*k/2/z0*(xout.^2+yout.^2));    
F(:,:) = exp(1i*pi/(lam*z0).*(x0.^2+y0.^2));    
xy(:,:) = abs(F0(:,:).*fftshift(fft2(fftshift(Ein.*F(:,:)))));
%mesh(xy)

imagesc(xout(1,:),yout(:,1),xy(:,:));    
colormap("hot");xlabel('X');ylabel('Y')    
axis equal;
