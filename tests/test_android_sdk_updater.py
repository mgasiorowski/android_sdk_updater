import re

from .. import android_sdk_updater


class TestAndroidSdkUpdater:

    def test_if_string_is_in_available_packages(self, sdkmanager_output_sdk_packages_build_tools_file_content):
        sdkmanager_output_available_packages = android_sdk_updater.get_sdkmanager_output_available_packages(
            sdkmanager_output_sdk_packages_build_tools_file_content)
        string_to_search = "emulator"
        found_strings = re.search("(?s)(?<=\s)({0})(?=\s)".format(string_to_search),
                                  str(sdkmanager_output_available_packages))
        assert found_strings is not None, \
            "There is no {0} string in sdkmanager_output_sdk_packages_build_tools".format(string_to_search)

    def test_if_string_is_in_installed_packages(self, sdkmanager_output_sdk_packages_build_tools_file_content):
        sdkmanager_output_installed_packages = android_sdk_updater.get_sdkmanager_output_installed_packages(
            sdkmanager_output_sdk_packages_build_tools_file_content)
        string_to_search = "tools"
        found_strings = re.search("(?s)(?<=\s)({0})(?=\s)".format(string_to_search),
                                  str(sdkmanager_output_installed_packages))
        assert found_strings is not None, \
            "There is no {0} string in sdkmanager_output_sdk_packages_build_tools".format(string_to_search)

    def test_if_string_is_in_build_tools_to_installation(self, sdkmanager_output_sdk_packages_build_tools_file_content):
        build_tools_to_installation = android_sdk_updater.get_build_tools_to_installation(
            sdkmanager_output_sdk_packages_build_tools_file_content)
        string_to_search = "build-tools;19.1.0"
        assert string_to_search in build_tools_to_installation, \
            "There is no {0} string in build_tools_to_installation".format(string_to_search)

    def test_if_string_is_in_sdk_packages_to_installation(self, sdkmanager_output_sdk_packages_build_tools_file_content):
        sdk_packages_to_installation = android_sdk_updater.get_sdk_packages_to_installation(
            sdkmanager_output_sdk_packages_build_tools_file_content)
        string_to_search = "extras;android;m2repository"
        assert string_to_search in sdk_packages_to_installation, \
            "There is no {0} string in build_tools_to_installation".format(string_to_search)

    def test_if_generate_sdk_packages_and_build_tools_to_installation(self, sdkmanager_output_sdk_packages_build_tools_file_content):
        generate_packages_to_installation = android_sdk_updater.generate_packages_to_installation(
            sdkmanager_output_sdk_packages_build_tools_file_content)
        string_to_search = '"extras;android;m2repository" "build-tools;19.1.0"'
        assert string_to_search in str(generate_packages_to_installation), \
            "There is no {0} string in sdk_packages_to_installation".format(string_to_search)

    def test_if_generate_sdk_packages_to_installation(self, sdkmanager_output_sdk_packages_file_content):
        generate_packages_to_installation = android_sdk_updater.generate_packages_to_installation(
            sdkmanager_output_sdk_packages_file_content)
        string_to_search = "extras;android;m2repository"
        assert string_to_search in str(generate_packages_to_installation), \
            "There is no {0} string in sdk_packages_to_installation".format(string_to_search)

    def test_if_generate_build_tools_to_installation(self, sdkmanager_output_build_tools_file_content):
        generate_packages_to_installation = android_sdk_updater.generate_packages_to_installation(
            sdkmanager_output_build_tools_file_content)
        string_to_search = "build-tools;19.1.0"
        assert string_to_search in str(generate_packages_to_installation), \
            "There is no {0} string in sdk_packages_to_installation".format(string_to_search)

    def test_if_generate_nothing__to_installation(self, sdkmanager_output_nothing_to_install_file_content):
        generate_packages_to_installation = android_sdk_updater.generate_packages_to_installation(
            sdkmanager_output_nothing_to_install_file_content)
        assert None is generate_packages_to_installation
