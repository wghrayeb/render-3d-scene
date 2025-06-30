from PIL import Image
from ObjectType import ObjectType



class Object2D3D:

    def __init__(self,
                 name: str = None,
                 tag_id: int = None,
                 image_path: str = None,
                 object_3d_path: str = None):

        self.name = name
        self.tag_id = tag_id
        self.image_path = image_path
        self.object_3d_path = object_3d_path

        self.__center = None # 3d point
        self.__orientation = [0.0, 0.0, 1.0] # 3d vector
        self.__segmentation_2d = None # 2d segmentation mask
        self.__depth_2d = None # 2d depth map
        self.__bbox_2d = None

        if self.tag_id is None and name is not None:
            self.tag_id = ObjectType[name].value

    def get_center(self):
        return self.__center

    def set_center(self, center):
        if isinstance(center, list) and len(center) == 3:
            self.__center = center
        else:
            raise ValueError("Center must be a list of three elements representing a 3D point.")

    def get_orientation(self):
        return self.__orientation

    def set_orientation(self, orientation):
        if isinstance(orientation, list) and len(orientation) == 3:
            self.__orientation = orientation
        else:
            raise ValueError("Orientation must be a list of three elements representing a 3D vector.")


    def show_image(self):
        if self.image_path is not None:
            img = Image.open(self.image_path)
            img.show()
        else:
            raise ValueError("Image path is not set.")

