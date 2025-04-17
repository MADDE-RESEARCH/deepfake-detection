from setuptools import setup, find_packages

def load_requirements(filename="requirements.txt"):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name='deepfake_detection',
    version='0.1.1',
    description='Deepfake detection model by Yermakov et. al(2025)',
    author='madde-research',
    author_email='purewater0901@gmail.com',
    url='https://github.com/madde-research/deepfake-detection.git',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=load_requirements("requirements.txt"),
)