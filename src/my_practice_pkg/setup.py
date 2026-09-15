from setuptools import find_packages, setup

package_name = 'my_practice_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='vpfmtldk2003@gmail.com',
    description='실습용 패키지: 직접 작성하는 Publisher/Subscriber',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_publisher = my_practice_pkg.my_publisher:main',
            'my_subscriber = my_practice_pkg.my_subscriber:main',
        ],
    },
)
