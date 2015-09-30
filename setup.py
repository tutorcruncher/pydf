import sys
import os
from setuptools import setup
from setuptools.command.install import install

description = 'PDF generation in python using wkhtmltopdf suitable for heroku'
long_description = description
if 'upload' in sys.argv or 'register' in sys.argv:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')


class OverrideInstall(install):
    def run(self):
        install.run(self)
        for filepath in self.get_outputs():
            if filepath.endswith('pydf/bin/wkhtmltopdf'):
                os.chmod(filepath, 0775)


setup(
    name='python-pdf',
    cmdclass={'install': OverrideInstall},
    version='0.21',
    description=description,
    long_description=long_description,
    author='Samuel Colvin',
    license='MIT',
    author_email='S@muelColvin.com',
    url='https://github.com/samuelcolvin/pydf',
    packages=['pydf'],
    platforms='any',
    package_data={'pydf': ['bin/*']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    test_suite='tests',
    zip_safe=False
)
