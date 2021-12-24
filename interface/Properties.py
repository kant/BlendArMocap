import bpy
from bpy.props import StringProperty, EnumProperty, IntProperty
from bpy.types import PropertyGroup


class MyProperties(PropertyGroup):
    # BUTTONS
    button_start_detection: StringProperty(
        name="",
        description="Detects features and record results in blender.",
        default="Start Detection"
    )

    button_transfer_animation: StringProperty(
        name="",
        description="Armature as target for detected results.",
        default="Start Transfer"
    )

    # DATA SELECTION
    selected_rig: StringProperty(
        name="",
        description="Select an armature for animation transfer.",
        default="Armature"
    )

    selected_driver_collection: StringProperty(
        name="",
        description="Select a collection of Divers.",
        default="Drivers"
    )
    # ENUMS
    # ("HOLISTIC", "Holistic", ""),
    enum_detection_type: EnumProperty(
        name="Target",
        description="Select detection type for motion tracking.",
        items=(
            ("HAND", "Hands", ""),
            ("FACE", "Face", ""),
            ("POSE", "Pose", ""),
        )
    )

    enum_fps: EnumProperty(
        name="FPS",
        description="Select Scene FPS",
        items=(
            ("24", "24", ""),
            ("25", "25", ""),
            ("30", "30", ""),
            ("60", "60", "")
        )
    )

    enum_synchronize: EnumProperty(
        name="Update",
        description="Select detection update type.",
        items=(
            ("SYNC", "synchronous", ""),
            ("ASYNC", "asynchronous", "")
        )
    )

    # Integer Input
    webcam_input_device: IntProperty(
        name="Webcam Device Slot",
        description="Select Webcam device.",
        min=0,
        max=4,
        default=0
    )

    data_path: StringProperty(
        name="File Path",
        description="File path to .mov file.",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )


def get_user():
    return bpy.context.scene.m_cgtinker_mediapipe