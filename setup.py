from setuptools import find_packages, setup

import os, sys

exec(open("admin_notification/version.py").read())

github_url = "https://github.com/amirhamiri"
package_name = "django-admin-notification"
package_url = "{}/{}".format(github_url, package_name)
package_path = os.path.abspath(os.path.dirname(__file__))
long_description_file_path = os.path.join(package_path, "README.md")
long_description_content_type = "text/markdown"
long_description = ""
try:
    long_description_file_options = (
        {} if sys.version_info[0] < 3 else {"encoding": "utf-8"}
    )
    with open(long_description_file_path, "r", **long_description_file_options) as f:
        long_description = f.read()
except IOError:
    pass

setup(
    name=package_name,
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    include_package_data=True,
    version=__version__,
    description="django-admin-notification is a Django app to display notification in Django admin panel",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author="Amirhossein Amiri",
    author_email="amirhamiri74@gmail.com",
    url=package_url,
    download_url="{}/archive/{}.tar.gz".format(package_url, __version__),
    project_urls={
        "Documentation": "{}#readme".format(package_url),
        "Issues": "{}/issues".format(package_url),
    },
    keywords=[
        "django",
        "admin",
        "notification"
    ],
    requires=["django(>=1.7)"],
    install_requires=[
        "six >= 1.9.0, < 2.0.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Build Tools",
    ],
    license="MIT",
    test_suite="runtests.runtests",
)