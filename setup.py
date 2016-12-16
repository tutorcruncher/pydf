import os
from setuptools import setup
from setuptools.command.install import install
from pydf.version import VERSION

description = 'PDF generation in python using wkhtmltopdf suitable for heroku'
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(THIS_DIR, 'README.rst')) as f:
    long_description = f.read()


class OverrideInstall(install):
    def run(self):
        install.run(self)
        for filepath in self.get_outputs():
            if filepath.endswith('pydf/bin/wkhtmltopdf'):
                os.chmod(filepath, 0o775)


setup(
    name='python-pdf',
    cmdclass={'install': OverrideInstall},
    version=str(VERSION),
    description=description,
    long_description=long_description,
    author='Samuel Colvin',
    license='MIT',
    author_email='S@muelColvin.com',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        ],
    test_suite='tests',
    zip_safe=False
)
