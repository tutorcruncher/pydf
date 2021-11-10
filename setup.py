import os
from importlib.machinery import SourceFileLoader
from pathlib import Path

from setuptools import setup
from setuptools.command.install import install

# avoid loading the package before requirements are installed:
version = SourceFileLoader('version', 'pydf/version.py').load_module()

description = 'PDF generation in python using wkhtmltopdf suitable for heroku'
THIS_DIR = Path(__file__).resolve().parent
readme_path = THIS_DIR / 'README.rst'
if readme_path.exists():
    long_description = readme_path.read_text()
else:
    long_description = description


class OverrideInstall(install):
    def run(self):
        install.run(self)
        for filepath in self.get_outputs():
            if filepath.endswith('pydf/bin/wkhtmltopdf'):
                os.chmod(filepath, 0o775)


setup(
    name='python-pdf',
    cmdclass={'install': OverrideInstall},
    version=version.VERSION,
    description=description,
    long_description=long_description,
    author='Samuel Colvin',
    license='MIT',
    author_email='s@muelcolvin.com',
    url='https://github.com/tutorcruncher/pydf',
    packages=['pydf'],
    platforms='any',
    package_data={'pydf': ['bin/*']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        ],
    zip_safe=False
)
