import os


def add_path(path):
    with open(os.getenv("GITHUB_PATH"), "a") as github_path:
        print(path, file=github_path)


def get_input(name):
    return os.getenv(f"INPUT_{name}".upper())


def set_output(name, value):
    print(f"::set-output name={name}::{_escape_data(value)}")


def set_env(name, value):
    with open(os.getenv("GITHUB_ENV"), "a") as env:
        print(f"{name}={_escape_data(value)}", file=env)


def debug(message):
    print(f"::debug::{_escape_data(message)}")


def warning(message):
    print(f"::warning::{_escape_data(message)}")


def error(message):
    print(f"::error::{_escape_data(message)}")


def group(title):
    print(f"::group::{title}")


def end_group():
    print("::endgroup::")


def add_mask(value):
    print(f"::add-mask::{_escape_data(value)}")


def stop_commands():
    print("::stop-commands::pause-commands")


def resume_commands():
    print("::pause-commands::")


def get_state(name):
    return os.getenv(f"STATE_{name}")


def save_state(name, value):
    print(f"::save-state name={name}::{_escape_data(value)}")


def _escape_data(value: str):
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
