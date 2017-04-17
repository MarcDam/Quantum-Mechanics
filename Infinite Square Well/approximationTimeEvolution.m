clear

x = linspace(0, 1, 2^8);
t = linspace(0, 1, 2^8);

f = x.^3.*(1-x);

A = 1/sqrt(trapz(x, abs(f).^2));

f = A*f;

cn = getcn(x, f, 10);

f = Psi(cn, x, t);

figure(1)
figure(2)

for i=1:length(t)
  figure(1)
  plot(x, real(f(:,i)), '-b', x, imag(f(:,i)), '-r', x, conj(f(:,i)).*f(:,i), '-g')
  axis([0 1 -2 3.2])
  grid
  figure(2)
  plot3(x, real(f(:,i)), imag(f(:,i)))
  axis([0 1 -2 2 -2 2])
  grid
  xlabel('x')
  ylabel('Re')
  zlabel('Im')
  pause(0.05)
end
