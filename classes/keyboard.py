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

import pyautogui


class Keyboard:
    """A class to handle keyboard automation.

    This class provides methods to type text, press hotkeys, and simulate key presses
    with optional interval and screenshot logging.
    """

    def typewrite(
        self, message: str, interval: float = 0.0, log_screenshot: bool = False
    ) -> None:
        """Types a string as if manually typing with a keyboard.

        Args:
            message (str): The message to type.
            interval (float): The time in seconds between each character typed.
            log_screenshot (bool): If True, logs a screenshot before typing.

        Returns:
            None
        """
        pyautogui.typewrite(
            message=message,
            interval=interval,
            logScreenshot=log_screenshot,
        )

    def hotkey(self, *keys: str, interval: float = 0.0) -> None:
        """Presses multiple keys in sequence to simulate a hotkey combination.

        Args:
            *keys (str): The keys to press in sequence.
            interval (float): The time in seconds between key presses.

        Returns:
            None
        """
        pyautogui.hotkey(*keys, interval=interval)

    def press_key(
        self,
        keys: str | list,
        presses_qty: int = 1,
        interval: float = 0.0,
        log_screenshot: bool = False,
    ) -> None:
        """Simulates pressing one or multiple keys.

        Args:
            keys (str | list): The key or list of keys to press.
            presses_qty (int): Number of times to press the key(s).
            interval (float): The time in seconds between key presses.
            log_screenshot (bool): If True, logs a screenshot before pressing the key(s).

        Returns:
            None
        """
        if keys == "super":
            keys = "winleft"

        pyautogui.press(
            keys=keys,
            presses=presses_qty,
            interval=interval,
            logScreenshot=log_screenshot,
        )


keyboard = Keyboard()
