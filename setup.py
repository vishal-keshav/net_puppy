import setuptools

with open("README.md", "r") as f:
    desc = f.read()

setuptools.setup(
    name="net-puppy",
    version="0.0.1",
    author="Vishal Keshav",
    author_email="vishal.keshav.1993@gmail.com",
    description="A network controlled terminal interface",
    long_description = desc,
    long_description_content_type="text/markdown",
    url="https://github.com/vishal-keshav/net_puppy",
    packages=setuptools.find_packages(),
    install_requires=['requests', 'websocket', 'json'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Permissive license :: MIT",
        "Operating system :: Linux",
    ],
)