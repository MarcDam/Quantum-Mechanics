function cn = getcnEpsilon(x, f, epsilon)

  cn = 0;

  i = 1;

  while norm(cn) < 1 - epsilon
    cn(i) = trapz(x, conj(psi_n(i, x)).*f);
    i++;
  end
