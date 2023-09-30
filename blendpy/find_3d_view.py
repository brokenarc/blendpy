from typing import Any

import bpy


def find_3d_view() -> Any:
    """Returns the first screen area with type 'VIEW_3D'

    Returns:
        A reference to the 3D view.
    """
    for area in bpy.data.window_managers[0].windows[0].screen.areas:
        if area.type == "VIEW_3D":
            return area.spaces[0]

    return bpy.context.space_data
