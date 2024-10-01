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

from os import system
from sys import platform


def clear_terminal() -> None:
    """Clears the terminal depending on the operating system.

    Clears the terminal using 'cls' on Windows and 'clear' on other platforms.

    Returns:
        None
    """
    if platform == "win32":
        system("cls")
    else:
        system("clear")
