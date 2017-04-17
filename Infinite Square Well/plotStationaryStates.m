clear

x = linspace(0, 1, 256);

nmax = 6;

for n=1:nmax
  plot(x, psi_n(n, x))
  title(['Time-independent wave-function with n = ' int2str(n)])
  grid
  pause(1)
end

