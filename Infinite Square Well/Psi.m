function out = Psi(cn, x, t)
  out = zeros(length(x), length(t));

  for j=1:length(cn)
    out += cn(j)*Psi_n(j, x, t);
  end

