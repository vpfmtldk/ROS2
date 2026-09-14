from setuptools import find_packages, setup

package_name = 'my_first_pkg'

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
    description='ROS2 학습용 첫 패키지: 간단한 publisher/subscriber 예제',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_publisher = my_first_pkg.my_publisher:main',
            'my_subscriber = my_first_pkg.my_subscriber:main',
        ],
    },
)
