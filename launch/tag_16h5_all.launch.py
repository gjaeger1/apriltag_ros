import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

# detect all 16h5 tags
cfg_16h5 = {
    "image_transport": "raw",
    "family": "16h5",
    "size": 0.151,
    "max_hamming": 0,
    "z_up": True
}

def generate_launch_description():
    composable_node = ComposableNode(
        name='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[("/apriltag/image", "/camera/rgb/image_raw"), ("/apriltag/camera_info", "/camera/rgb/camera_info")],
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
