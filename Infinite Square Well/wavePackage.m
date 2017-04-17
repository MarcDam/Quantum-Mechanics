clear

x = linspace(0, 1, 2^12);
t = linspace(0, 0.1, 2^10);

x0 = 0.5;
sigma = 0.1;
k0 = 100;

f = exp(-1/2*(x-x0).^2/sigma^2).*exp(-i*k0*x);

A = 1/sqrt(trapz(x, abs(f).^2));
(sigma^2*pi)^(-1/4) - A

f = A*f;

cn = getcnEpsilon(x, f, 10^-7);

n = 1:length(cn);

En = n.^2*pi^2/2;

plot(En, abs(cn).^2, '-o')

grid

return

f = Psi(cn, x, t);

figure(1)
figure(2)

for i=1:length(t)
  figure(1)
  plot(x, real(f(:,i)), '-b', x, imag(f(:,i)), '-r', x, conj(f(:,i)).*f(:,i), '-g')
  axis([0 1 -2 4])
  grid
  figure(2)
  plot3(x, real(f(:,i)), imag(f(:,i)))
  axis([0 1 -3 3 -3 3])
  grid
  xlabel('x')
  ylabel('Re')
  zlabel('Im')
  pause(0.05)
end
