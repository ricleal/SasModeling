"""
    Setup for SasView
    #TODO: Add checks to see that all the dependencies are on the system
"""
import sys
import os
from setuptools import setup, Extension
from distutils.command.build_ext import build_ext
from distutils.core import Command

try:
    from numpy.distutils.misc_util import get_numpy_include_dirs
    NUMPY_INC = get_numpy_include_dirs()[0]
except:
    try:
        import numpy
        NUMPY_INC = os.path.join(os.path.split(numpy.__file__)[0],
                                 "core", "include")
    except:
        msg = "\nNumpy is needed to build SasModeling. "
        print msg, "Try easy_install numpy.\n  %s" % str(sys.exc_value)
        sys.exit(0)

##############################################################

package_dir = {}
package_data = {}
packages = []
ext_modules = []

# Remove all files that should be updated by this setup
# We do this here because application updates these files from .sansview
# except when there is no such file
# Todo : make this list generic
plugin_model_list = ['polynominal5.py', 'sph_bessel_jn.py',
                     'sum_Ap1_1_Ap2.py', 'sum_p1_p2.py',
                     'testmodel_2.py', 'testmodel.py',
                     'polynominal5.pyc', 'sph_bessel_jn.pyc',
                     'sum_Ap1_1_Ap2.pyc', 'sum_p1_p2.pyc',
                     'testmodel_2.pyc', 'testmodel.pyc', 'plugins.log']
sans_dir = os.path.join(os.path.expanduser("~"), '.sasview')
if os.path.isdir(sans_dir):
    f_path = os.path.join(sans_dir, "sasview.log")
    if os.path.isfile(f_path):
        os.remove(f_path)
    f_path = os.path.join(sans_dir, "serialized_cat.json")
    if os.path.isfile(f_path):
        os.remove(f_path)
    f_path = os.path.join(sans_dir, 'config', "custom_config.py")
    if os.path.isfile(f_path):
        os.remove(f_path)
    f_path = os.path.join(sans_dir, 'plugin_models')
    if os.path.isdir(f_path):
        for f in os.listdir(f_path): 
            if f in plugin_model_list:
                file_path = os.path.join(f_path, f)
                os.remove(file_path)
                    
# 'sys.maxsize' and 64bit: Not supported for python2.5
is_64bits = False
if sys.version_info >= (2, 6):
    is_64bits = sys.maxsize > 2 ** 32
    
    
enable_openmp = True

if sys.platform == 'darwin':
    if not is_64bits:
        # Disable OpenMP
        enable_openmp = False
    else:
        # Newer versions of Darwin don't support openmp
        try:
            darwin_ver = int(os.uname()[2].split('.')[0])
            if darwin_ver >= 12:
                enable_openmp = False
        except:
            print "PROBLEM determining Darwin version"

# Options to enable OpenMP
copt = {'msvc': ['/openmp'],
         'mingw32' : ['-fopenmp'],
         'unix' : ['-fopenmp']}
lopt = {'msvc': ['/MANIFEST'],
         'mingw32' : ['-fopenmp'],
         'unix' : ['-lgomp']}

# Platform-specific link options
platform_lopt = {'msvc' : ['/MANIFEST']}
platform_copt = {}

# Set copts to get compile working on OS X >= 10.9 using clang
if sys.platform == 'darwin':
    try:
        darwin_ver = int(os.uname()[2].split('.')[0])
        if darwin_ver >= 13:
            platform_copt = {'unix' : ['-Wno-error=unused-command-line-argument-hard-error-in-future']}
    except:
        print "PROBLEM determining Darwin version"



class build_ext_subclass(build_ext):
    def build_extensions(self):
        # Get 64-bitness
        c = self.compiler.compiler_type
        print "Compiling with %s (64bit=%s)" % (c, str(is_64bits))
        
        # OpenMP build options
        if enable_openmp:
            if copt.has_key(c):
                for e in self.extensions:
                    e.extra_compile_args = copt[ c ]
            if lopt.has_key(c):
                for e in self.extensions:
                    e.extra_link_args = lopt[ c ]
                    
        # Platform-specific build options
        if platform_lopt.has_key(c):
            for e in self.extensions:
                e.extra_link_args = platform_lopt[ c ]

        if platform_copt.has_key(c):
            for e in self.extensions:
                e.extra_compile_args = platform_copt[ c ]


        build_ext.build_extensions(self)

# Other
numpy_incl_path = os.path.join(NUMPY_INC, "numpy")

# sans module
package_dir["sans"] = os.path.join("src", "sans")
packages.append("sans")



# Sans models
includedir = os.path.join("src", "sans", "models", "include")
igordir = os.path.join("src", "sans", "models", "c_extension", "libigor")
cephes_dir = os.path.join("src", "sans", "models", "c_extension", "cephes")
c_model_dir = os.path.join("src", "sans", "models", "c_extension", "c_models")
smear_dir = os.path.join("src", "sans", "models", "c_extension", "c_smearer")
gen_dir = os.path.join("src", "sans", "models", "c_extension", "c_gen")
wrapper_dir = os.path.join("src", "sans", "models", "c_extension", "python_wrapper", "generated")
model_dir = os.path.join("src", "sans", "models")

if os.path.isdir(wrapper_dir):
    for file in os.listdir(wrapper_dir): 
        file_path = os.path.join(wrapper_dir, file)
        os.remove(file_path)
else:
    os.makedirs(wrapper_dir)
sys.path.append(os.path.join("src", "sans", "models", "c_extension", "python_wrapper"))
from wrapping import generate_wrappers
generate_wrappers(header_dir=includedir,
                  output_dir=model_dir,
                  c_wrapper_dir=wrapper_dir)

IGNORED_FILES = [".svn"]
if not os.name == 'nt':
    IGNORED_FILES.extend(["gamma_win.c", "winFuncs.c"])

EXTENSIONS = [".c", ".cpp"]

def append_file(file_list, dir_path):
    """
    Add sources file to sources
    """
    for f in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, f)):
            _, ext = os.path.splitext(f)
            if ext.lower() in EXTENSIONS and f not in IGNORED_FILES:
                file_list.append(os.path.join(dir_path, f)) 
        elif os.path.isdir(os.path.join(dir_path, f)) and \
                not f.startswith("."):
            sub_dir = os.path.join(dir_path, f)
            for new_f in os.listdir(sub_dir):
                if os.path.isfile(os.path.join(sub_dir, new_f)):
                    _, ext = os.path.splitext(new_f)
                    if ext.lower() in EXTENSIONS and\
                         new_f not in IGNORED_FILES:
                        file_list.append(os.path.join(sub_dir, new_f)) 
        
model_sources = []
append_file(file_list=model_sources, dir_path=igordir)
append_file(file_list=model_sources, dir_path=c_model_dir)
append_file(file_list=model_sources, dir_path=wrapper_dir)

smear_sources = []
append_file(file_list=smear_sources, dir_path=smear_dir)
        
package_dir["sans.models"] = model_dir
package_dir["sans.models.sans_extension"] = os.path.join("src", "sans", "models", "sans_extension")
package_data['sans.models'] = [os.path.join('media', "*.*")]
package_data['sans.models'] += [os.path.join('media', 'img', "*.*")]
packages.extend(["sans.models", "sans.models.sans_extension"])
    
smearer_sources = [os.path.join(smear_dir, "smearer.cpp"),
                  os.path.join(smear_dir, "smearer_module.cpp")]
geni_sources = [os.path.join(gen_dir, "sld2i_module.cpp")]
if os.name == 'nt':
    smearer_sources.append(os.path.join(igordir, "winFuncs.c"))
    geni_sources.append(os.path.join(igordir, "winFuncs.c"))

c_models = [ 
    Extension("sans.models.sans_extension.c_models",
        sources=model_sources,
        include_dirs=[
            igordir, includedir, c_model_dir, numpy_incl_path, cephes_dir
        ],
    ),

    # Smearer extension
    Extension("sans.models.sans_extension.smearer",
        sources=smearer_sources,
        include_dirs=[igordir, smear_dir, numpy_incl_path],
    ),
                    
    Extension("sans.models.sans_extension.smearer2d_helper",
        sources=[
            os.path.join(smear_dir, "smearer2d_helper_module.cpp"),
            os.path.join(smear_dir, "smearer2d_helper.cpp"),
        ],
        include_dirs=[smear_dir, numpy_incl_path],
    ),
                    
    Extension("sans.models.sans_extension.sld2i",
        sources=[
            os.path.join(gen_dir, "sld2i_module.cpp"),
            os.path.join(gen_dir, "sld2i.cpp"),
            os.path.join(c_model_dir, "libfunc.c"),
            os.path.join(c_model_dir, "librefl.c"),
        ],
        include_dirs=[gen_dir, includedir, c_model_dir, numpy_incl_path],
    ),
]

# Comment out the following to avoid rebuilding all the models
ext_modules.extend(c_models)

# SasView

# package_dir["sans.sansview"] = "sansview"
# package_data['sans.sansview'] = ['images/*', 'media/*', 'test/*', 
#                                  'default_categories.json']
# packages.append("sans.sansview")

# required = [
#     'bumps>=0.7.5.2', 'periodictable>=1.3.1', 'pyparsing<2.0.0',
# 
#     # 'lxml>=2.2.2',
#     'lxml', 
# 
#     ## The following dependecies won't install automatically, so assume them
#     ## The numbers should be bumped up for matplotlib and wxPython as well.
#     # 'numpy>=1.4.1', 'scipy>=0.7.2', 'matplotlib>=0.99.1.1',
#     # 'wxPython>=2.8.11', 'pil',
#     ]
# 
# if os.name=='nt':
#     required.extend(['html5lib', 'reportlab'])
# else:
#     required.extend(['pil'])

required = []
   
# Set up SasView    
setup(
    name="sasmodeling",
    version="0.1",
    description="SAS Modeling Package",
    author="University of Tennessee",
    author_email="sansdanse@gmail.com",
    url="http://sasview.org",
    license="PSF",
    keywords="small-angle x-ray and neutron scattering analysis",
    download_url="https://sourceforge.net/projects/sansviewproject/files/",
    package_dir=package_dir,
    packages=packages,
    package_data=package_data,
    ext_modules=ext_modules,
    install_requires=required,
    zip_safe=False,
    cmdclass={'build_ext': build_ext_subclass}
    )   
