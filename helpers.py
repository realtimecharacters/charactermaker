# helper functions provide utilities for easier generation of geometry

# generates a series of three dimensional tuples
# that follow the radius of a circle
def points_on_circle(radius=1.0, count=7, z=0.0):
    return []

# generates a series of three dimensional tuples
# that follow a quadratic ease between two points and their vector handles
# this method is used to smooth the transitions between handles
def ease_in_out(point1a, point1b, point2a, point2b):
    return []


# generates tubular series of vertices and faces
# based on two points, 
def make_tube(start, end, circle_point_count=7, close_end=False):
    verts = []
    faces = []
    return verts, faces

# generates a tuple representing a single quad face
# receives the column number and row number for a given face in a grid
# uses total rows count to calculate the vertex indices for the current face
# exclude_limbs allows to ignore certain vertex sets
def face(column, row, rows, exclude_limbs=None):
    """ Create a single face """

    v1 = column* rows + row
    v2 = (column + 1) * rows + row
    v3 = (column + 1) * rows + 1 + row
    v4 = column * rows + 1 + row

    if exclude_limbs:
        for limb in exclude_limbs:
            ev = limb['verts']
            if v1 in ev and v2 in ev and v3 in ev and v4 in ev:
                return None

    return (v1, v2, v3, v4)

# generates a tuple representing a single triangular face
# uses the column and row indices along with total row count
# to calculate vertex indices for the face
def triface(column, row, rows, tip):
    return (column* rows + row,
            tip,
            column * rows + 1 + row,
            )
