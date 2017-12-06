import os
import pytest


@pytest.fixture()
def sdkmanager_output_sdk_packages_build_tools_file_content():
    with open("{0}/tests/resources/sdkmanager_output_sdk_packages_build_tools".format(os.getcwd())) as sdkmanager_output_lines_file:
        sdkmanager_output_lines = sdkmanager_output_lines_file.read()
    return sdkmanager_output_lines


@pytest.fixture()
def sdkmanager_output_sdk_packages_file_content():
    with open("{0}/tests/resources/sdkmanager_output_sdk_packages".format(os.getcwd())) as sdkmanager_output_lines_file:
        sdkmanager_output_lines = sdkmanager_output_lines_file.read()
    return sdkmanager_output_lines


@pytest.fixture()
def sdkmanager_output_build_tools_file_content():
    with open("{0}/tests/resources/sdkmanager_output_build_tools".format(os.getcwd())) as sdkmanager_output_lines_file:
        sdkmanager_output_lines = sdkmanager_output_lines_file.read()
    return sdkmanager_output_lines


@pytest.fixture()
def sdkmanager_output_nothing_to_install_file_content():
    with open("{0}/tests/resources/sdkmanager_output_nothing_to_install".format(os.getcwd())) as sdkmanager_output_lines_file:
        sdkmanager_output_lines = sdkmanager_output_lines_file.read()
    return sdkmanager_output_lines
