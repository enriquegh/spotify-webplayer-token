from setuptools import setup

with open('README.rst') as rd:
    long_description = rd.read()

with open("requirements.txt") as rq:
    requirements = rq.read().splitlines()

setup(
    name='spotify_token',
    py_modules=['spotify_token'],
    version='0.1.3',
    description='Python wrapper for Spotify Webplayer access token',
    author='Enrique Gonzalez',
    author_email='egonzalezh94@gmail.com',
    license='MIT',
    url='https://github.com/enriquegh/spotify-webplayer-token',
    install_requires=requirements,
    long_description=long_description,
    keywords=['wrapper', 'spotify'],
    classifiers=["Programming Language :: Python :: 3",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Topic :: Software Development :: Libraries",
                 "Topic :: Utilities"],
)
