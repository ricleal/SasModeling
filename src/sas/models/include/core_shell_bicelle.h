#if !defined(core_shell_bicelle_h)
#define core_shell_bicelle_h
#include "parameters.hh"

/**
 * Structure definition for core-shell bicelle parameters
 */
//[PYTHONCLASS] = CoreShellBicelleModel
//[DISP_PARAMS] = radius, rim_thick, length, face_thick, axis_theta, axis_phi
//[DESCRIPTION] = <text>P(q,alpha)= scale/Vs*f(q)^(2) + bkg,  where: f(q)= 2(core_sld
//			- solvant_sld)* Vc*sin[qLcos(alpha/2)]
//			/[qLcos(alpha/2)]*J1(qRsin(alpha))
//			/[qRsin(alpha)]+2(shell_sld-solvent_sld)
//			*Vs*sin[q(L+T)cos(alpha/2)][[q(L+T)
//			*cos(alpha/2)]*J1(q(R+T)sin(alpha))
//			/q(R+T)sin(alpha)]
//
//			alpha:is the angle between the axis of
//          the cylinder and the q-vector
//			Vs: the volume of the outer shell
//			Vc: the volume of the core
//			L: the length of the core
//    		shell_sld: the scattering length density
//			of the shell
//			solvent_sld: the scattering length density
//			of the solvent
//			bkg: the background
//			T: the thickness
//    		R+T: is the outer radius
// 		L+2T: The total length of the outershell
//			J1: the first order Bessel function
// 		theta: axis_theta of the cylinder
// 		phi: the axis_phi of the cylinder...
//		</text>
//[FIXED]= <text> axis_phi.width; axis_theta.width; length.width;radius.width; rim_thick.width;face_thick.width</text>
//[ORIENTATION_PARAMS]= axis_phi; axis_theta;axis_phi.width; axis_theta.width

class CoreShellBicelleModel{
public:
  // Model parameters

  /// Core radius [A]
  //  [DEFAULT]=radius=20.0 [A]
  Parameter radius;

  /// Scale factor
  //  [DEFAULT]=scale=1.0
  Parameter scale;

  /// Shell rim thickness [A]
  //  [DEFAULT]=rim_thick=10.0 [A]
  Parameter rim_thick;

  /// Shell face_thick [A]
  //  [DEFAULT]=face_thick=10.0 [A]
  Parameter face_thick;

  /// Core length [A]
  //  [DEFAULT]=length=400.0 [A]
  Parameter length;

  /// Core SLD [1/A^(2)]
  //  [DEFAULT]=core_sld=1.0e-6 [1/A^(2)]
  Parameter core_sld;

  /// Shell face SLD [1/A^(2)]
  //  [DEFAULT]=face_sld=4.0e-6 [1/A^(2)]
  Parameter face_sld;

  /// Shell rim SLD [1/A^(2)]
  //  [DEFAULT]=rim_sld=4.0e-6 [1/A^(2)]
  Parameter rim_sld;

  /// Solvent SLD [1/A^(2)]
  //  [DEFAULT]=solvent_sld=1.0e-6 [1/A^(2)]
  Parameter solvent_sld;

  /// Incoherent Background [1/cm]
  //  [DEFAULT]=background=0 [1/cm]
  Parameter background;

  /// Orientation of the long axis of the core-shell cylinder w/respect incoming beam [deg]
  //  [DEFAULT]=axis_theta=90.0 [deg]
  Parameter axis_theta;

  /// Orientation of the long axis of the core-shell cylinder in the plane of the detector [deg]
  //  [DEFAULT]=axis_phi=0.0 [deg]
  Parameter axis_phi;

  // Constructor
  CoreShellBicelleModel();

  // Operators to get I(Q)
  double operator()(double q);
  double operator()(double qx, double qy);
  double calculate_ER();
  double calculate_VR();
  double evaluate_rphi(double q, double phi);
};

#endif
