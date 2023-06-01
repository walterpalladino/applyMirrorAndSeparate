# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Apply Mirror Modifier and Separate Meshes",
    "author": "Walter Palladino",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Object > Apply > Apply Mirror and Separate",
    "description": "Apply Mirror Modifier and Separate Meshes",
    "warning": "",
    "doc_url": "https://github.com/walterpalladino/applyMirrorAndSeparate#readme",
    "category": "Object",
}


import bpy

context = bpy.context
data = bpy.data



def main(context):
    # Select only Meshes
    selected_objects = [obj  for obj in context.selected_objects if obj.type == 'MESH']

    # Iterate on all the meshes
    for obj in selected_objects:
        # set the object to active
        bpy.context.view_layer.objects.active = obj
        #   Iterate the modifiers
        for modifier in obj.modifiers:
            #   Only apply Mirror modifier
            if (modifier.name == 'Mirror'):
                # Apply Mirror Modifier
                bpy.ops.object.modifier_apply(modifier=modifier.name)
                # Separate if applies
                bpy.ops.mesh.separate(type='LOOSE')


class ApplyMirrorAndSeparate(bpy.types.Operator):
    """Iterate on all selected objects, looks for Mirror modifier and apply it and separate meshes"""
    bl_idname = "object.apply_mirror_and_separate"
    bl_label = "Apply Mirror And Separate"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func_setup(self, context):
    self.layout.operator(ApplyMirrorAndSeparate.bl_idname, text=ApplyMirrorAndSeparate.bl_label)


def register():
    bpy.utils.register_class(ApplyMirrorAndSeparate)
    bpy.types.VIEW3D_MT_object_apply.append(menu_func_setup)


def unregister():
    bpy.utils.unregister_class(ApplyMirrorAndSeparate)
    bpy.types.VIEW3D_MT_object_apply.remove(menu_func_setup)


if __name__ == "__main__":
    register()

