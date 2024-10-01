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

from typing import Callable, Optional

import pyautogui
from pyautogui import Point, linear


class MouseCursor:
    """A class that controls mouse cursor operations using PyAutoGUI."""

    @property
    def position(self) -> Point:
        """Returns the current position of the mouse cursor as a Point(x, y)."""
        return pyautogui.position()

    def move_relative_current_position(
        self,
        x_offset: int,
        y_offset: int,
        duration: float = 0.0,
        tween: Callable = linear,
        log_screenshot: bool = False,
    ) -> None:
        """Moves the mouse relative to its current position."""
        pyautogui.move(
            xOffset=x_offset,
            yOffset=y_offset,
            duration=duration,
            tween=linear,
            logScreenshot=log_screenshot,
        )

    def move_to(
        self,
        x: int,
        y: int,
        duration: float = 0.0,
        tween: Callable = linear,
        log_screenshot: bool = False,
    ) -> None:
        """Moves the mouse cursor to specific coordinates."""
        pyautogui.moveTo(
            x=x,
            y=y,
            duration=duration,
            tween=tween,
            logScreenshot=log_screenshot,
        )

    def drag_relative_current_position(
        self,
        x_offset: int,
        y_offset: int,
        duration: float = 0.0,
        tween: Callable = linear,
        mouse_button: str = "left",
        log_screenshot: bool = False,
        mouse_down_up: bool = True,
    ) -> None:
        """Drags the mouse from the current position by the given offsets."""
        pyautogui.drag(
            xOffset=x_offset,
            yOffset=y_offset,
            duration=duration,
            tween=tween,
            button=mouse_button,
            logScreenshot=log_screenshot,
            mouseDownUp=mouse_down_up,
        )

    def drag_to(
        self,
        x: int,
        y: int,
        duration: float = 0.0,
        tween: Callable = linear,
        mouse_button: str = "left",
        log_screenshot: bool = False,
        mouse_down_up: bool = True,
    ) -> None:
        """Drags the mouse to specific coordinates."""
        pyautogui.dragTo(
            x=x,
            y=y,
            duration=duration,
            tween=tween,
            button=mouse_button,
            logScreenshot=log_screenshot,
            mouseDownUp=mouse_down_up,
        )

    def click(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        duration: float = 0.0,
        tween: Callable = linear,
        clicks_qty: int = 1,
        interval: int | float = 0.0,
        mouse_button: str = "left",
        log_screenshot: bool = False,
    ) -> None:
        """Clicks at the specified position or the current position."""
        pyautogui.click(
            x=x,
            y=y,
            duration=duration,
            tween=tween,
            clicks=clicks_qty,
            interval=interval,
            button=mouse_button,
            logScreenshot=log_screenshot,
        )

    def click_by_image(
        self,
        path_to_image: str,
        duration: float = 0.0,
        tween: Callable = linear,
        clicks_qty: int = 1,
        interval: int | float = 0.0,
        mouse_button: str = "left",
        log_screenshot: bool = False,
    ) -> None:
        """Locates an image on the screen and clicks on it."""
        pyautogui.click(
            path_to_image,
            duration=duration,
            tween=linear,
            clicks=clicks_qty,
            interval=interval,
            button=mouse_button,
            logScreenshot=log_screenshot,
        )

    def left_click(
        self,
        x: int,
        y: int,
        interval: int | float = 0.0,
        duration: float = 0.0,
        tween: Callable = linear,
        log_screenshot: bool = False,
    ) -> None:
        """Performs a left-click at the specified coordinates."""
        pyautogui.leftClick(
            x=x,
            y=y,
            duration=duration,
            tween=linear,
            interval=interval,
            logScreenshot=log_screenshot,
        )

    def right_click(
        self,
        x: int,
        y: int,
        interval: int | float = 0.0,
        duration: float = 0.0,
        tween: Callable = linear,
        log_screenshot: bool = False,
    ) -> None:
        """Performs a right-click at the specified coordinates."""
        pyautogui.rightClick(
            x=x,
            y=y,
            duration=duration,
            tween=linear,
            interval=interval,
            logScreenshot=log_screenshot,
        )

    def double_click(
        self,
        x: int,
        y: int,
        duration: float = 0.0,
        interval: int | float = 0.0,
        mouse_button: str = "left",
        tween: Callable = linear,
        log_screenshot: bool = False,
    ) -> None:
        """Performs a double-click at the specified coordinates."""
        pyautogui.doubleClick(
            x=x,
            y=y,
            duration=duration,
            tween=linear,
            interval=interval,
            button=mouse_button,
            logScreenshot=log_screenshot,
        )

    def triple_click(
        self,
        x: int,
        y: int,
        duration: float = 0.0,
        interval: int | float = 0.0,
        mouse_button: str = "left",
        tween: Callable = linear,
        log_screenshot: bool = False,
    ) -> None:
        """Performs a triple-click at the specified coordinates."""
        pyautogui.tripleClick(
            x=x,
            y=y,
            duration=duration,
            tween=linear,
            interval=interval,
            button=mouse_button,
            logScreenshot=log_screenshot,
        )

    def middle_click(
        self,
        x: int,
        y: int,
        duration: float = 0.0,
        interval: int | float = 0.0,
        tween: Callable = linear,
        log_screenshot: bool = False,
    ) -> None:
        """Performs a middle-click at the specified coordinates."""
        pyautogui.middleClick(
            x=x,
            y=y,
            duration=duration,
            tween=linear,
            interval=interval,
            logScreenshot=log_screenshot,
        )

    def scroll(
        self,
        offset: int | float,
        x: Optional[int] = None,
        y: Optional[int] = None,
        log_screenshot: bool = False,
    ) -> None:
        """Scrolls the mouse vertically."""
        pyautogui.scroll(
            offset,
            x=x,
            y=y,
            logScreenshot=log_screenshot,
        )

    def hscroll(
        self,
        offset: int | float,
        x: Optional[int] = None,
        y: Optional[int] = None,
        log_screenshot: bool = False,
    ) -> None:
        """Scrolls the mouse horizontally."""
        pyautogui.hscroll(
            offset,
            x=x,
            y=y,
            logScreenshot=log_screenshot,
        )

    def vscroll(
        self,
        offset: int | float,
        x: Optional[int] = None,
        y: Optional[int] = None,
        log_screenshot: bool = False,
    ) -> None:
        """Scrolls the mouse vertically."""
        pyautogui.vscroll(
            offset,
            x=x,
            y=y,
            logScreenshot=log_screenshot,
        )


mouse_cursor = MouseCursor()
