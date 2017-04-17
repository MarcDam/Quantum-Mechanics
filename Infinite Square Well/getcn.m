function cn = getcn(x, f, nmax)

  cn = zeros(1, nmax);

  for i=1:nmax
    cn(i) = trapz(x, conj(psi_n(i, x)).*f);
  end
