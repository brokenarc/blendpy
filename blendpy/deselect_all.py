import bpy


def deselect_all() -> None:
    """Deselects any selected objects."""
    bpy.ops.object.select_all(action='DESELECT')
