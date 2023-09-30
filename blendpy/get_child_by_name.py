from collections.abc import Iterable
from typing import Any


def get_child_by_name(root: Any, name: str):
    """Search an object's children for an item with the given ``name``.

    The algorithm will recursively search the given object's ``children``
    attribute and each of their ``children`` attributes.

    Args:
        root: any item that has both ``children`` and ``name`` attributes
        name: the item name to search for

    Returns:
        The first item found with the given ``name``, or ``None`` if no item
        was found.
    """
    if getattr(root, 'name', None) == name:
        return root

    children = getattr(root, 'children', None)
    if isinstance(children, Iterable):
        for child in children:
            found = get_child_by_name(child, name)
            if found:
                return found

    return None
