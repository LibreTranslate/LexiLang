import io
import platform
import re
import setuptools

with io.open("README.md", encoding="utf-8") as fr:
    long_description = fr.read()

if __name__ == "__main__":
    setuptools.setup(
        name="LexiLang",
        version="1.0.2",
        author="Piero Toffanin",
        author_email="pt@masseranolabs.com",
        maintainer="Piero Toffanin",
        maintainer_email="pt@masseranolabs.com",
        description="Simple, fast dictionary-based language detector",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="AGPLv3",
        url="https://github.com/LibreTranslate/LexiLang",
        classifiers=[
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Intended Audience :: Developers",
            "Topic :: Text Processing :: Linguistic",
        ],
        packages=["lexilang"],
        package_data={"lexilang": ["data/words.pickle"]}
    )
