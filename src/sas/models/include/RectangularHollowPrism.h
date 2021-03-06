#if !defined(RectangularHollowPrism_h)
#define RectangularHollowPrism_h
#include "parameters.hh"

/** Structure definition for RectangularHollowPrism parameters
 * [PYTHONCLASS] = RectangularHollowPrismModel
 * [DISP_PARAMS] = short_side, b2a_ratio, c2a_ratio, thickness
   [DESCRIPTION] = <text> Form factor for a hollow rectangular prism with uniform scattering length density.
		scale:Scale factor
		short_side: shortest side of the rectangular prism  [A]
		b2a_ratio: ratio b/a [adim]
		c2a_ratio: ratio c/a [adim]
		thickness: thickness of the walls [A]
		sldPipe: Pipe_sld
		sldSolv: solvent_sld
		background:Incoherent Background [1/cm]
		</text>
	[FIXED]= <text> short_side.width; b2a_ratio.width; c2a_ratio.width; thicness.width; </text>

 **/

class RectangularHollowPrismModel{
public:
  // Model parameters
  
  /// Scale factor
  //  [DEFAULT]=scale=1.0
  Parameter scale;
  
  ///  Shortest side of rectangular prism [A]
  //  [DEFAULT]=short_side=35 [A]
  Parameter short_side;
  
  ///  Ratio b/a [adim]
  //  [DEFAULT]=b2a_ratio=1 [adim]
  Parameter b2a_ratio;
  
  ///  Ratio c/a [adim]
  //  [DEFAULT]=c2a_ratio=1 [adim]
  Parameter c2a_ratio;
  
  ///  Thickness of walls [A]
  //  [DEFAULT]=thickness=1 [A]
  Parameter thickness;
  
  /// SLD_Pipe [1/A^(2)]
  //  [DEFAULT]=sldPipe=6.3e-6 [1/A^(2)]
  Parameter sldPipe;
  
  /// sldSolv [1/A^(2)]
  //  [DEFAULT]=sldSolv=1.0e-6 [1/A^(2)]
  Parameter sldSolv;

  /// Incoherent Background [1/cm]
  //  [DEFAULT]=background=0.0 [1/cm]
  Parameter background;
  
  // Constructor
  RectangularHollowPrismModel();

  // Operators to get I(Q)
  double operator()(double q);
  double operator()(double qx, double qy);
  double calculate_ER();
  double calculate_VR();
  double evaluate_rphi(double q, double phi);
};
#endif
