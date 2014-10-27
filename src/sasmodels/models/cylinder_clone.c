real form_volume(real radius, real length);
real Iq(real q, real sld, real solvent_sld, real radius, real length);
real Iqxy(real qx, real qy, real sld, real solvent_sld, real radius, real length, real theta, real phi);


// twovd = 2 * volume * delta_rho
// besarg = q * R * sin(alpha)
// siarg = q * L/2 * cos(alpha)
real _cyl(real twovd, real besarg, real siarg, real alpha);
real _cyl(real twovd, real besarg, real siarg, real alpha)
{
    const real bj = (besarg == REAL(0.0) ? REAL(0.5) : J1(besarg)/besarg);
    const real si = (siarg == REAL(0.0) ? REAL(1.0) : sin(siarg)/siarg);
    return twovd*si*bj;
}

real form_volume(real radius, real length)
{
    return M_PI*radius*radius*length;
}
real Iq(real q,
    real sldCyl,
    real sldSolv,
    real radius,
    real length)
{
    const real qr = q*radius;
    const real qh = q*REAL(0.5)*length;
    const real twovd = REAL(2.0)*(sldCyl-sldSolv)*form_volume(radius, length);
    real total = REAL(0.0);
    // real lower=0, upper=M_PI_2;
    for (int i=0; i<76 ;i++) {
        // translate a point in [-1,1] to a point in [lower,upper]
        //const real alpha = ( Gauss76Z[i]*(upper-lower) + upper + lower )/2.0;
        const real alpha = REAL(0.5)*(Gauss76Z[i]*M_PI_2 + M_PI_2);
        real sn, cn;
        SINCOS(alpha, sn, cn);
        const real fq = _cyl(twovd, qr*sn, qh*cn, alpha);
        total += Gauss76Wt[i] * fq * fq * sn;
    }
    // translate dx in [-1,1] to dx in [lower,upper]
    //const real form = (upper-lower)/2.0*total;
    return REAL(1.0e8) * total * M_PI_4;
}

real Iqxy(real qx, real qy,
    real sldCyl,
    real sldSolv,
    real radius,
    real length,
    real cyl_theta,
    real cyl_phi)
{
    real sn, cn; // slots to hold sincos function output

    // Compute angle alpha between q and the cylinder axis
    SINCOS(cyl_theta*M_PI_180, sn, cn);
    // # The following correction factor exists in sasview, but it can't be
    // # right, so we are leaving it out for now.
    const real spherical_integration = fabs(cn)*M_PI_2;
    const real q = sqrt(qx*qx+qy*qy);
    const real cos_val = cn*cos(cyl_phi*M_PI_180)*(qx/q) + sn*(qy/q);
    const real alpha = acos(cos_val);

    const real qr = q*radius;
    const real qh = q*REAL(0.5)*length;
    const real twovd = REAL(2.0)*(sldCyl-sldSolv)*form_volume(radius, length);
    SINCOS(alpha, sn, cn);
    const real fq = _cyl(twovd, qr*sn, qh*cn, alpha);
    return REAL(1.0e8) * fq * fq * spherical_integration;
}
