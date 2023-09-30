# Blender Python snippets

Assorted Python code snippets for use with Blender.

## Snippets

The code snippets are located in the `blendpy` directory. To avoid code
duplication, some snippets may depend on other snippets in the collection. Take
note of those dependencies in the list below and in the source files.

* `deselect_all.py` - Deselects any selected objects.
* `find_3d_view.py` - Returns the first screen area with type 'VIEW_3D'.
* `get_child_by_name.py` - Search an object's children for an item with a given
  name.
* `get_layer_collection.py` - Gets the layer collection identified by a given
  name. Depends on `get_child_by_name`.
* `set_active_layer_collection.py` - Sets the active layer collection to the one
  identified by a given name. Depends on `get_layer_collection`.

## License

All files are MIT licensed unless otherwise noted in the file's docstrings.
