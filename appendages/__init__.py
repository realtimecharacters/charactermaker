# appendages are any element that augments the main body modeling on a Character
# appendages are the easiest way to contribute to this open source project
    # no pull requests for genitalia, crude, violent or distasteful elements will be accepted
    # keep it G-rated, people

# helper functions provide utilities for easier generation of geometry
# see helpers file for descriptions of each method
from helpers import *

# sample code for an appendage class
class Appendage():

    # do any setup before building mesh
    # handles in Realtime Characters are empties that are drawn as a circle
    # these empties will be automatically created based on the handle definitions below
    # handles have all the usual transform properties of an empty (location, scale, rotation)
    # handles can lock certain transform properties to allow more restricted control
    self.handles = [

        # the base handle is a common pattern for appendages
        # it specifies the angle and initial shape/scale of the appendage separate from its root
        # this is useful because the root handle simply creates the intersection with the base mesh
        # but has its orientation locked to that of the intersecting faces
        {
            'name': 'base',

            # handle's initial locations are set as ratios of the root handle
            'location': (0,0,0),

            # initial angles are also relative to the root handle
            'rotation': (),

            # child handles' transform properties are relative to the parent handle
            'subhandles': [],
        }
    ]

    # while most property values on appendages are set by dragging handles
    # some properties don't make sense as handles
    # these properties are added to the UI when an appendage is added
    # the UI elements for these properties are created automatically
    # changes to these properties cause a rebuild of the mesh
    self.properties = [

    ]

    # see comments on rig() method
    self.bones = []

    # see comments on texture_groups() method
    self.groups = []

    # root -  handle that specifies the "hole" in the body that is filled by this appendage
            # completed appendages must be "water tight" meaning there are no holes in the meshes
    # handles - the handle definitions defined above determine which handles will be received by this method
    def __init__(self, root, handles=[]):
        print('initializing appendage')

    # the mesh method is called every time a transform property on a handle is changed
    # this allows the model to rebuild itself in realtime while dragging handles
    # this method, therefore, must be very performant or it will create a bad user experience
    # do as much calculation ahead of time as possible (in init)
    # the build method doesn't actually create any geometry in Blender
    # it only calculates the vertex and face locations, then returns those
    # the main script will then create all the geometry at once for better performance
    def mesh(self):
        print('building appendage')

    # called when user moves into the integument / texture stage of character creation
    # unlike the vertex groups for rigging, these vertex groups are used for integuments & textures
    # consider what would be useful beyond the builtin dorsal/ventral, interior/exterior groups
    # for example a claw or tooth would usually have a different texture than the flesh around it
    def texture_groups(self):
        print('texturing appendage')

    # called when the user is ready to rig their Character
    # should return list of bone locations and transforms
    # along with their hierarchical structure
    # generally these should follow some of the handle locations if possible
    # so the user has control over the rig
    # method also returns a mapping of vertex groups to bones with weighted vertices
    # this method call is also the time to create any shape keys
    def rig(self):
        print('rigging appendage')

        return []


register(Appendage)


MYVAR = 'it works!'
