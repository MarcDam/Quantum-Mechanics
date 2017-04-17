function out = Psi_n(n, x, t)
  out = transpose(psi_n(n, x))*exp(-i*n^2*pi^2/2*t);
