import setuptools

install_requires = [
    "requests",
    "python-dotenv",
    "psycopg2-binary",
    "urllib3",
    "beautifulsoup4",
    "pandas",
    "oauth2client",
    "paramiko",
    "boto3"
]

setuptools.setup(
    name="llmr",
    version="0.1.1",
    author="Suyeol Yun",
    author_email="syyun@mit.edu",
    packages=setuptools.find_packages(),
    description="",
    url="https://github.com/syyunn/llmr",
    install_requires=install_requires,
)
