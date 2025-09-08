import setuptools

setuptools.setup(
    name="extension_kitten_tts",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="Your Name",
    description="A template extension for TTS Generation WebUI",
    url="https://github.com/rsxdalv/extension_kitten_tts",
    project_urls={},
    scripts=[],
    install_requires=[
        # Add your dependencies here
        # "numpy",
        # "torch",
        # pip install https://github.com/KittenML/KittenTTS/releases/download/0.1/kittentts-0.1.0-py3-none-any.whl
        "kittentts @ https://github.com/KittenML/KittenTTS/releases/download/0.1/kittentts-0.1.0-py3-none-any.whl",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
