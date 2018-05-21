from setuptools import setup

setup(name='speaksee',
      version='0.1',
      description='Captioning and cross-modal retrieval algorithms',
      url='http://github.com/aimagelab/speaksee',
      author='Lorenzo Baraldi, Marcella Cornia',
      author_email='lorenzo.baraldi@unimore.it',
      license='MIT',
      packages=['speaksee'],
      install_requires=[
          'torch',
          'torchvision',
          'numpy',
          'h5py',
          'tqdm',
          'requests',
      ],
      zip_safe=False)