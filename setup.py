from setuptools import setup, find_packages

setup(
    name='fnkauth',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # Choose an appropriate license
    description='A simple Django app',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fakanakavera/fnkauth',  # Update with your GitHub URL
    author='FakaNaKavera',
    author_email='fakanakavera666@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=3.0',  # Adjust the version according to your needs
        'requests',     # Example of an additional package
        'djangorestframework',
        'djangorestframework-simplejwt',
        # Add other dependencies here
    ],
)