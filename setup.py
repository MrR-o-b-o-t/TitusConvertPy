from setuptools import find_packages, setup

setup(
    name='TitusConvertPy',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "autopep8",
        "backcall",
        "click",
        "colorama",
        "debugpy",
        "decorator",
        "et-xmlfile",
        "Flask",
        "gunicorn",
        "ipykernel",
        "ipython",
        "ipython-genutils",
        "itsdangerous",
        "jedi",
        "Jinja2",
        "jupyter-client",
        "jupyter-core",
        "MarkupSafe",
        "matplotlib-inline",
        "numpy",
        "openpyxl",
        "pandas",
        "parso",
        "pickleshare",
        "prompt-toolkit",
        "pycodestyle",
        "Pygments",
        "python-dateutil",
        "pytz",
        "pyzmq",
        "six",
        "toml",
        "tornado",
        "traitlets",
        "wcwidth",
        "Werkzeug"
    ],
    python_requires=">=3.7"
)
