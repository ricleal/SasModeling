##############################################################################
# This software was developed by the University of Tennessee as part of the
# Distributed Data Analysis of Neutron Scattering Experiments (DANSE)
# project funded by the US National Science Foundation.
#
# If you use DANSE applications to do scientific research that leads to
# publication, we ask that you acknowledge the use of the software with the
# following sentence:
#
# This work benefited from DANSE software developed under NSF award DMR-0520547
#
# Copyright 2008-2011, University of Tennessee
##############################################################################

""" 
Provide functionality for a C extension model

.. WARNING::

   THIS FILE WAS GENERATED BY WRAPPERGENERATOR.PY
   DO NOT MODIFY THIS FILE, MODIFY
   src/sans/models/include/core_shell.h
   AND RE-RUN THE GENERATOR SCRIPT
"""

from sans.models.BaseComponent import BaseComponent
from sans.models.sans_extension.c_models import CCoreShellModel

def create_CoreShellModel():
    """
       Create a model instance
    """
    obj = CoreShellModel()
    # CCoreShellModel.__init__(obj) is called by
    # the CoreShellModel constructor
    return obj

class CoreShellModel(CCoreShellModel, BaseComponent):
    """ 
    Class that evaluates a CoreShellModel model. 
    This file was auto-generated from src/sans/models/include/core_shell.h.
    Refer to that file and the structure it contains
    for details of the model.
    
    List of default parameters:

    * radius          = 60.0 [A]
    * scale           = 1.0 
    * thickness       = 10.0 [A]
    * core_sld        = 1e-06 [1/A^(2)]
    * shell_sld       = 2e-06 [1/A^(2)]
    * solvent_sld     = 3e-06 [1/A^(2)]
    * background      = 0.0 [1/cm]
    * M0_sld_shell    = 0.0 [1/A^(2)]
    * M_theta_shell   = 0.0 [deg]
    * M_phi_shell     = 0.0 [deg]
    * M0_sld_core     = 0.0 [1/A^(2)]
    * M_theta_core    = 0.0 [deg]
    * M_phi_core      = 0.0 [deg]
    * M0_sld_solv     = 0.0 [1/A^(2)]
    * M_theta_solv    = 0.0 [deg]
    * M_phi_solv      = 0.0 [deg]
    * Up_frac_i       = 0.5 [u/(u+d)]
    * Up_frac_f       = 0.5 [u/(u+d)]
    * Up_theta        = 0.0 [deg]

    """
        
    def __init__(self, multfactor=1):
        """ Initialization """
        self.__dict__ = {}
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        #apply(CCoreShellModel.__init__, (self,)) 

        CCoreShellModel.__init__(self)
        self.is_multifunc = False
		        
        ## Name of the model
        self.name = "CoreShellModel"
        ## Model description
        self.description = """
        Form factor for a monodisperse spherical particle with particle
		with a core-shell structure:
		
		The form factor is normalized by the
		total particle volume.
		
		radius: core radius, thickness: shell thickness
		
		Ref: Guinier, A. and G. Fournet,
		John Wiley and Sons, New York, 1955.
        """
       
        ## Parameter details [units, min, max]
        self.details = {}
        self.details['radius'] = ['[A]', None, None]
        self.details['scale'] = ['', None, None]
        self.details['thickness'] = ['[A]', None, None]
        self.details['core_sld'] = ['[1/A^(2)]', None, None]
        self.details['shell_sld'] = ['[1/A^(2)]', None, None]
        self.details['solvent_sld'] = ['[1/A^(2)]', None, None]
        self.details['background'] = ['[1/cm]', None, None]
        self.details['M0_sld_shell'] = ['[1/A^(2)]', None, None]
        self.details['M_theta_shell'] = ['[deg]', None, None]
        self.details['M_phi_shell'] = ['[deg]', None, None]
        self.details['M0_sld_core'] = ['[1/A^(2)]', None, None]
        self.details['M_theta_core'] = ['[deg]', None, None]
        self.details['M_phi_core'] = ['[deg]', None, None]
        self.details['M0_sld_solv'] = ['[1/A^(2)]', None, None]
        self.details['M_theta_solv'] = ['[deg]', None, None]
        self.details['M_phi_solv'] = ['[deg]', None, None]
        self.details['Up_frac_i'] = ['[u/(u+d)]', None, None]
        self.details['Up_frac_f'] = ['[u/(u+d)]', None, None]
        self.details['Up_theta'] = ['[deg]', None, None]

        ## fittable parameters
        self.fixed = ['thickness.width',
                      'radius.width']
        
        ## non-fittable parameters
        self.non_fittable = []
        
        ## parameters with orientation
        self.orientation_params = ['M0_sld_shell',
                                   'M_theta_shell',
                                   'M_phi_shell',
                                   'M0_sld_core',
                                   'M_theta_core',
                                   'M_phi_core',
                                   'M0_sld_solv',
                                   'M_theta_solv',
                                   'M_phi_solv',
                                   'Up_frac_i',
                                   'Up_frac_f',
                                   'Up_theta']

        ## parameters with magnetism
        self.magnetic_params = ['M0_sld_shell', 'M_theta_shell', 'M_phi_shell', 'M0_sld_core', 'M_theta_core', 'M_phi_core', 'M0_sld_solv', 'M_theta_solv', 'M_phi_solv', 'Up_frac_i', 'Up_frac_f', 'Up_theta']

        self.category = None
        self.multiplicity_info = None
        
    def __setstate__(self, state):
        """
        restore the state of a model from pickle
        """
        self.__dict__, self.params, self.dispersion = state
        
    def __reduce_ex__(self, proto):
        """
        Overwrite the __reduce_ex__ of PyTypeObject *type call in the init of 
        c model.
        """
        state = (self.__dict__, self.params, self.dispersion)
        return (create_CoreShellModel, tuple(), state, None, None)
        
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(CoreShellModel())   
       	
    def run(self, x=0.0):
        """ 
        Evaluate the model
        
        :param x: input q, or [q,phi]
        
        :return: scattering function P(q)
        
        """
        return CCoreShellModel.run(self, x)
   
    def runXY(self, x=0.0):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q, or [qx, qy]
        
        :return: scattering function P(q)
        
        """
        return CCoreShellModel.runXY(self, x)
        
    def evalDistribution(self, x):
        """ 
        Evaluate the model in cartesian coordinates
        
        :param x: input q[], or [qx[], qy[]]
        
        :return: scattering function P(q[])
        
        """
        return CCoreShellModel.evalDistribution(self, x)
        
    def calculate_ER(self):
        """ 
        Calculate the effective radius for P(q)*S(q)
        
        :return: the value of the effective radius
        
        """       
        return CCoreShellModel.calculate_ER(self)
        
    def calculate_VR(self):
        """ 
        Calculate the volf ratio for P(q)*S(q)
        
        :return: the value of the volf ratio
        
        """       
        return CCoreShellModel.calculate_VR(self)
              
    def set_dispersion(self, parameter, dispersion):
        """
        Set the dispersion object for a model parameter
        
        :param parameter: name of the parameter [string]
        :param dispersion: dispersion object of type DispersionModel
        
        """
        return CCoreShellModel.set_dispersion(self,
               parameter, dispersion.cdisp)
        
   
# End of file

