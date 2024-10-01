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

from pyautogui import position, sleep

from .clear_terminal import clear_terminal


def show_cursor_position(delay: float = 0.1) -> None:
    """Print cursor position after delay

    Args:
        delay (float): delay after update.

    Returns:
        None
    """

    while True:
        print("Use CTRL + C to stop!")
        print(position())
        sleep(delay)
        clear_terminal()
