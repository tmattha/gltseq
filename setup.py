import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()

test_deps = ['pytest~=7.1.2', 'hypothesis~=6.52.1']

extras = {
    'test': test_deps,
}

setuptools.setup(
    name="gltseq",
    version="0.0.1",
    author="Tilmann Matthaei",
    description=r'Various code dealing with GLT matrix sequences for the Seminar "Wissenschaftliches Rechnen und Hochleistungsrechnen".',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tmattha/glt-seq-code",
    package_dir={"": "src"},
    packages=["gltseq"],
    install_requires=[
        'numpy~=1.23.1',
        'scipy~=1.8.1',
        'matplotlib~=3.5.2',
        'PyQt5~=5.15.6',       # rendering backend for matplotlib
    ],
    tests_require=test_deps,
    extras_require=extras,
    python_requires=">=3.8"
)
