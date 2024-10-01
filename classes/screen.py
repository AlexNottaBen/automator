# Copyright 2024 AlexNottaBen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from os import mkdir, path
from typing import List, Optional

import pyautogui
from PIL import Image
from pyautogui import Size

from .types import LocationProperties


@dataclass
class ScreenResolution:
    """Represents the screen resolution in terms of width and height."""

    width: int
    height: int


class Screen:
    """Class for handling screen operations such as resolution,
    size, screenshots, and object location."""

    @property
    def size(self) -> Size:
        """Returns the screen resolution as a tuple."""
        return pyautogui.size()

    @property
    def resolution(self) -> ScreenResolution:
        """Returns the current screen size as a ScreenResolution object."""
        width, height = pyautogui.size()
        return ScreenResolution(width=width, height=height)

    def create_screenshot(
        self,
        picture_name: str,
        save_to="screenshots/",
        region: Optional[LocationProperties] = None,
    ) -> Image:
        """Takes a screenshot and saves it to the specified folder.

        Args:
            picture_name (str): Name of the screenshot file.
            save_to (str): The directory to save the screenshot in.
            region (Optional[tuple]): The region of the screen to capture.

        Returns:
            Image: The screenshot as an Image object.

        Requires:
            scrot (for GNU/Linux systems without native screenshot support).
        """
        if not path.isdir(save_to):
            mkdir(save_to)

        return pyautogui.screenshot((save_to + picture_name), region=region)

    def locate_object(self, path_to_image: str) -> Optional[LocationProperties]:
        """Locate an object on the screen using an image template.

        Args:
            path_to_image (str): The file path to the image used for locating the object.

        Returns:
            Optional[LocationProperties]: The location of the object as a LocationProperties
            or None if not found.
        """
        return pyautogui.locateOnScreen(path_to_image)

    def locate_center_object(self, path_to_image: str) -> Optional[tuple]:
        """Locate the center of an object on the screen using an image template.

        Args:
            path_to_image (str): The file path to the image used for locating the object.

        Returns:
            Optional[tuple]: The (x, y) coordinates of the center of the object
            or None if not found.
        """
        return pyautogui.locateCenterOnScreen(path_to_image)

    def locate_all_objects(self, path_to_image: str) -> List[LocationProperties]:
        """Locate all instances of an object on the screen using an image template.

        Args:
            path_to_image (str): The file path to the image used for locating the objects.

        Returns:
            List[LocationProperties]: A list of locations where the object was found.
        """
        return pyautogui.locateAllOnScreen(path_to_image)


screen = Screen()
