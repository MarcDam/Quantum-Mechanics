clear

x = linspace(0, 1, 2^10);

f = x.^3.*(1-x);

A = 1/sqrt(trapz(x, abs(f).^2));

f = A*f;

plot(x, f)

for n = 1:100
  plot(x, Psi(getcn(x, f, n), x, 0), 'r')
  hold on
  plot(x, f, 'b')
  hold off
  axis([0 1 -2 8])
  grid
  title(["n = " num2str(n)])
  pause(0.3)
end

cn = getcn(x, f, 10);

norm(cn)


