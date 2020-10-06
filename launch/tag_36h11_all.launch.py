import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

# detect all 36h11 tags
cfg_16h5 = {
    "image_transport": "raw",
    "family": "36h11",
    "size": 0.1559,
    "max_hamming": 0,
    "z_up": True,
    "tag_ids": [0,1,2,3,4,5,6,7],
    "tag_frames": ["tag_0","tag_1","tag_2","tag_3","tag_4","tag_5","tag_6","tag_7"],
}

def generate_launch_description():
    composable_node = ComposableNode(
        name='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[("/apriltag/image", "/camera/image_raw"), ("/apriltag/camera_info", "/camera/camera_info")],
        parameters=[cfg_16h5])
    container = ComposableNodeContainer(
        name='tag_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[composable_node],
        output='screen'
    )

    return launch.LaunchDescription([container])
