from distutils.core import setup

long_description = open('README.markdown').read()

setup(
    name='django-shortcuts',
    version="0.1.0",
    package_data={'shortcuts': ['templates/shortcuts/*.html']},
    package_dir={'shortcuts': 'shortcuts'},
    packages=['shortcuts'],
    description='Django shortcut (redirect) application',
    author='Jeremy Carbaugh',
    author_email='jcarbaugh@sunlightfoundation.com',
    license='BSD License',
    url='http://github.com/sunlightlabs/django-shortcuts/',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
