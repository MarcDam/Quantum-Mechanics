clear

nmax = 10;

integrals = zeros(nmax, nmax);

x = linspace(0, 1, 256);

for i=1:nmax
  for j=1:nmax
    integrals(i, j) = trapz(x, conj(psi_n(i, x)).*psi_n(j, x));
  end
end
