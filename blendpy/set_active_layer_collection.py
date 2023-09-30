from typing import Any

import bpy

from .get_layer_collection import get_layer_collection


def set_active_layer_collection(name: str) -> Any:
    """Sets the active layer collection to the one identified by ``name``.

    Args:
        name: the name of the collection to make active.

    Returns:
        A reference to the layer collection that is now active, or ``None`` if
        no layer collection was found with ``name``.
    """
    layer_collection = get_layer_collection(name)

    if layer_collection:
        bpy.context.view_layer.active_layer_collection = layer_collection

    return layer_collection
