from setuptools import setup, find_packages

setup(name='get_smarties',
    version='0.01',
    description='dummy variable generation with fit/transform capabilities',
    url='https://github.com/joeddav/get_smarties',
    author='Joe Davison',
    author_email='josephddavison@gmail.com',
    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.

        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='pandas, dummy, fit/transform',

    install_requires=['pandas>=0.23.1', 'numpy'],
)
