'''OpenGL extension KHR.robust_buffer_access_behavior

This module customises the behaviour of the 
OpenGL.raw.GLES2.KHR.robust_buffer_access_behavior to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension specifies the behavior of out-of-bounds buffer and
	array accesses. This is an improvement over the existing
	KHR_robustness extension which states that the application should
	not crash, but that behavior is otherwise undefined. This extension
	specifies the access protection provided by the GL to ensure that
	out-of-bounds accesses cannot read from or write to data not owned
	by the application. All accesses are contained within the buffer
	object and program area they reference. These additional robustness
	guarantees apply to contexts created with the robust access flag
	set.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/KHR/robust_buffer_access_behavior.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.KHR.robust_buffer_access_behavior import *
from OpenGL.raw.GLES2.KHR.robust_buffer_access_behavior import _EXTENSION_NAME

def glInitRobustBufferAccessBehaviorKHR():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION