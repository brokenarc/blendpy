from typing import Any

import bpy

from .get_child_by_name import get_child_by_name


def get_layer_collection(name: str) -> Any:
    """Gets the layer collection identified by ``name``.

    The layer collections will be traversed recursively, and the first one
    found matching ``name`` sill be returned.

    Args:
        name: the name of the collection to make active.

    Returns:
        A reference to the named layer collection, or ``None`` if no layer
        collection was found with ``name``.
    """
    return get_child_by_name(bpy.context.view_layer.layer_collection, name)
