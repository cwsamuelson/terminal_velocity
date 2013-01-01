from setuptools import setup

setup(
    name="terminal_velocity",
    version="0.1a1",
    author="Sean Hammond",
    packages=["terminal_velocity"],
    scripts=["bin/terminal_velocity"],
    url="https://github.com/seanh/terminal_velocity",
    license="GNU General Public License, Version 3",
    description="A fast note-taking app for the UNIX terminal",
    long_description=open("README.markdown").read(),
    install_requires=[
        "urwid==1.1.1",
        ]
)
