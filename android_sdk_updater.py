import subprocess
import re
import sys
import os

android_sdkmanager_path = "{0}/tools/bin/sdkmanager".format(os.environ["ANDROID_HOME"])


def get_sdkmanager_output_lines():
    sdkmanager_output = subprocess.check_output("echo y | {0} --list".format(android_sdkmanager_path),
                                                shell=True, stderr=subprocess.STDOUT)
    return sdkmanager_output.decode('utf8')


def get_sdkmanager_output_available_packages(get_sdkmanager_output_lines):
    sdkmanager_output_available_packages = re.search("(?s)(?<=Available Packages:)(.*)",
                                                     get_sdkmanager_output_lines)
    return sdkmanager_output_available_packages.group().split("\n")


def get_sdkmanager_output_installed_packages(get_sdkmanager_output_lines):
    sdkmanager_output_installed_packages = re.search("(?s)(?<=Installed packages:)(.*?)(?=Available Packages:)",
                                                     get_sdkmanager_output_lines)
    return sdkmanager_output_installed_packages.group().split("\n")


def get_build_tools_to_installation(get_sdkmanager_output_lines):
    build_tools_to_installation = []
    all_build_tools = filter(lambda x: "build-tools;" in x, get_sdkmanager_output_available_packages(
        get_sdkmanager_output_lines))
    for build_tool in all_build_tools:
        build_tool_versions = re.search("(build-tools;.*?)(?=\s)", build_tool)
        build_tool_version = build_tool_versions.group(0)
        if not any(build_tool_version in s for s in get_sdkmanager_output_installed_packages(
                get_sdkmanager_output_lines)):
            build_tools_to_installation.append(build_tool_version)
    return build_tools_to_installation


def get_sdk_packages_to_installation(get_sdkmanager_output_lines):
    android_sdk_packages_to_installation_file_path = "{0}/android_sdk_packages_to_installation".format(os.getcwd())
    sdk_packages_to_installation = []
    with open(android_sdk_packages_to_installation_file_path) as packages_file:
        for packages_file_line in packages_file:
            if not any(packages_file_line.rstrip() in s for s in get_sdkmanager_output_installed_packages(
                    get_sdkmanager_output_lines)):
                sdk_packages_to_installation.append(packages_file_line.rstrip())
    return sdk_packages_to_installation


def generate_packages_to_installation(get_sdkmanager_output_lines):
    sdk_packages_to_installation = list(filter(None, get_sdk_packages_to_installation(
        get_sdkmanager_output_lines)))
    build_tools_to_installation = list(filter(None, get_build_tools_to_installation(
        get_sdkmanager_output_lines)))

    if sdk_packages_to_installation and build_tools_to_installation:
        return " ".join("\"{0}\"".format(w) for w in sdk_packages_to_installation + build_tools_to_installation)
    elif sdk_packages_to_installation:
        return " ".join("\"{0}\"".format(w) for w in sdk_packages_to_installation)
    elif build_tools_to_installation:
        return " ".join("\"{0}\"".format(w) for w in build_tools_to_installation)
    else:
        return None


def main():
    generated_packages_to_installation = generate_packages_to_installation(get_sdkmanager_output_lines())
    update_sdk_command = 'echo y | {0} --update'.format(android_sdkmanager_path)
    print("Update SDK command: {0}".format(update_sdk_command))
    subprocess.call(update_sdk_command, shell=True)
    if generated_packages_to_installation:
        installation_command = 'echo y | {0} {1}'.format(android_sdkmanager_path,
                                                         generated_packages_to_installation)
        print("Installation command: {0}".format(installation_command))
        installation_command_returncode = subprocess.call(installation_command, shell=True)
        sys.exit(installation_command_returncode)
    else:
        print("There is nothing to install")
        sys.exit()


if __name__ == "__main__":
    main()
