from setuptools import setup, find_packages


setup(
    name='Cube Translator',
    version='0.1.0',
    description='Traslate subtitles from one language to another',
    author='Cube Estrada',



    packages=find_packages(),
    install_requires=['pysrt','requests'],
    entry_points={
        'console_scripts': [
            'cbsrt = cb_translator.cli:cli',
        ],

    },
)
