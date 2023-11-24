from balalaika import __version__
from balalaika import __copyright__
from balalaika import __url__


def main() -> None:
    import platform
    import subprocess
    from platform import python_version

    import hikari
    import aiohttp

    java_version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
    java_version = f'\n{" " * 8}- '.join(v for v in java_version.decode().split('\r\n') if v)

    message = f"""
{__copyright__}
Balalaika {__version__}
Github Repository: {__url__}

Python Version: {python_version()}
Platform: {platform.platform()}
Java: {java_version or 'Not installed or not detected'}
Libraries:
    - hikari {hikari.__version__}
    - aiohttp {aiohttp.__version__}
    """

    print(message)
