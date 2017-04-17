clear

x = linspace(0, 1, 256);

nmax = 6;

figure
hold on

for n=1:nmax
  plot(x, psi_n(n, x))
end

hold off 
title(['Time-independent wave-function with n ranging from 1 to ' int2str(n)])
grid

