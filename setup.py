import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

_version_ = "0.0.0"

REPO_NAME = "E2E-ML-project"
AUTHOR_USER_NAME = "srsuveer1807"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "srsuveer9896@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,  # fixed case
    long_description_content_type="text/markdown",  # fixed case and corrected key
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # fixed unicode issue
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
