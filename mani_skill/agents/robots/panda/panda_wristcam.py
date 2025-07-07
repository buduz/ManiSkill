import numpy as np
import sapien

from mani_skill import PACKAGE_ASSET_DIR
from mani_skill.agents.registration import register_agent
from mani_skill.sensors.camera import CameraConfig
from mani_skill.utils import sapien_utils

from .panda import Panda


@register_agent()
class PandaWristCam(Panda):
    """Panda arm robot with the real sense camera attached to gripper"""

    uid = "panda_wristcam"
    urdf_path = f"{PACKAGE_ASSET_DIR}/robots/panda/panda_v3.urdf"

    @property
    def _sensor_configs(self):
        return [
            CameraConfig(
                uid="hand_camera",
                pose=sapien.Pose(p=[0, 0, 0], q=[1, 0, 0, 0]),
                width=256,
                height=256,
                fov=np.pi / 2,
                near=0.01,
                far=100,
                mount=self.robot.links_map["camera_link"],
            ),
            # 新增第三视角相机（固定位置）
            CameraConfig(
                uid="4th_view_camera",
                # pose=sapien.Pose(p=[0.6, 0.7, 0.6], q=[0.707, 0, 0.707, 0]),
                pose=sapien_utils.look_at(eye=[0.6, 0.7, 0.6], target=[0.0, 0.0, 0.35]),
                width=256,
                height=256,
                fov=1,
                near=0.01,
                far=100,
                mount=None,  # 不绑定到任何连杆，固定在世界坐标系
            ),
            CameraConfig(
                uid="third_view_camera",
                # pose=sapien.Pose(p=[0.6, 0.7, 0.6], q=[0.707, 0, 0.707, 0]),
                # pose=sapien.Pose(p=[0.6, 0.7, 0.6], q=[0.707, 0, 0.707, 0]),
                pose=sapien_utils.look_at(eye=[0.4, 0.0, 0.3], target=[0.0, 0.0, 0.15]),
                width=256,
                height=256,
                fov=1,
                near=0.01,
                far=100,
                mount=None,  # 不绑定到任何连杆，固定在世界坐标系
            ),
        ]
