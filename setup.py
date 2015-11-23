from setuptools import setup, find_packages
import press_links


setup(
    name="django-press-links",
    version=press_links.__version__,
    url='https://github.com/citylive/django-press-links',
    license='BSD',
    description="Press app",
    long_description=open('README.rst', 'r').read(),
    author='City Live nv',
    install_requires=['django-parler==1.4', 'django-summernote==0.5.15'],
    packages=find_packages('.'),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
