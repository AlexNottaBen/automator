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

import pyautogui  # noqa


class AutomatorConfigurator:
    """A class to configure settings for automation.

    This class provides methods to set the pause duration between actions
    and to enable or disable the fail-safe feature.
    """

    def set_pause_between_action(self, delay: int) -> None:
        """Sets the pause duration between actions.

        Args:
            delay (int): The number of seconds to pause between actions.

        Returns:
            None
        """
        pyautogui.PAUSE = delay

    def set_failsafe(self, is_failsafe_enabled: bool) -> None:
        """Enables or disables fail-safe mode.

        When fail-safe mode is enabled, moving the mouse to the upper-left corner
        of the screen will raise a FailSafeException, which can abort
        the program.

        Args:
            is_failsafe_enabled (bool): If True, fail-safe mode is enabled;
            otherwise, it is disabled.

        Returns:
            None
        """
        pyautogui.FAILSAFE = is_failsafe_enabled


configurator = AutomatorConfigurator()
