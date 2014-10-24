#if !defined(sc_h)
#define sc_h
#include "parameters.hh"

/**
 * Structure definition for SC_ParaCrystal parameters
 */
//[PYTHONCLASS] = SCCrystalModel
//[DISP_PARAMS] = radius,phi, psi, theta
//[DESCRIPTION] =<text>P(q)=(scale/Vp)*V_lattice*P(q)*Z(q)+bkg where scale is the volume
//					 fraction of sphere,
//				Vp = volume of the primary particle,
//				V_lattice = volume correction for
//					for the crystal structure,
//				P(q)= form factor of the sphere (normalized),
//				Z(q)= paracrystalline structure factor
//					for a simple cubic structure.
//				[Simple Cubic ParaCrystal Model]
//				Parameters;
//				scale: volume fraction of spheres
//				bkg:background, R: radius of sphere
//				dnn: Nearest neighbor distance
//				d_factor: Paracrystal distortion factor
//				radius: radius of the spheres
//				sldSph: SLD of the sphere
//				sldSolv: SLD of the solvent
//
//		</text>
//[FIXED]=  radius.width;phi.width;psi.width; theta.width
//[ORIENTATION_PARAMS]= <text> phi;psi; theta; phi.width;psi.width; theta.width</text>



class SCCrystalModel{
public:
  // Model parameters
  /// Scale factor
  //  [DEFAULT]=scale= 1.0
  Parameter scale;

  /// Nearest neighbor distance [A]
  //  [DEFAULT]=dnn=220.0 [A]
  Parameter dnn;

  /// Paracrystal distortion factor g
  //  [DEFAULT]=d_factor=0.06
  Parameter d_factor;

  /// Radius of sphere [A]
  //  [DEFAULT]=radius=40.0 [A]
  Parameter radius;

  /// sldSph [1/A^(2)]
  //  [DEFAULT]=sldSph= 3.0e-6 [1/A^(2)]
  Parameter sldSph;

  /// sldSolv [1/A^(2)]
  //  [DEFAULT]=sldSolv= 6.3e-6 [1/A^(2)]
  Parameter sldSolv;

  /// Incoherent Background [1/cm]
  //  [DEFAULT]=background=0 [1/cm]
  Parameter background;
  /// Orientation of the a1 axis w/respect incoming beam [deg]
  //  [DEFAULT]=theta=0.0 [deg]
  Parameter theta;
  /// Orientation of the a2 in the plane of the detector [deg]
  //  [DEFAULT]=phi=0.0 [deg]
  Parameter phi;
  /// Orientation of the a3 in the plane of the detector [deg]
  //  [DEFAULT]=psi=0.0 [deg]
  Parameter psi;

  // Constructor
  SCCrystalModel();

  // Operators to get I(Q)
  double operator()(double q);
  double operator()(double qx, double qy);
  double calculate_ER();
  double calculate_VR();
  double evaluate_rphi(double q, double phi);
};

#endif
