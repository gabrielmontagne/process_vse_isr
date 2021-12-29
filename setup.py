from setuptools import setup

setup(
    name='process_vse_isr',
    author='Gabriel Montagné Láscaris-Comneno',
    author_email='gabriel@tibas.london',
    license='MIT',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'process_vse_isr = process_vse_isr.__main__:main'
        ]
    }
)
