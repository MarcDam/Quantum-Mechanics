function Phi = getPhi(x, t, p, f)

  Phi = zeros(length(t), length(p));

  for n=1:length(p)
    Phi(n) = trapz(x, 1/sqrt(2*pi)*conj(exp(i*p(n)*x).*f);
  end
