# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    setup.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/02/17 09:08:45 by pwolff            #+#    #+#             #
#    Updated: 2024/02/17 09:08:45 by pwolff           ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

"""
    Se diriger vers https://pypi.org/ et create un compte
    WOLFF  wpf68  Python  pascalwolff....com


    python3 setup.py sdist bdist_wheel
    pip install twine
    export PATH=$PATH:/home/pwolff/.local/bin
    twine upload dist/*
"""

from setuptools import setup, find_packages


setup(

    name='ft_package',
    version='0.0.1',
    author='pwolff',
    author_email='pwolff@student.42mulhouse.fr',
    license='MIT',
    description='A sample test package',
    packages=find_packages(),
    # classifiers=[
    #     'License :: OSI Approved :: MIT License',
    # ],
    url='https://github.com/wpf68?tab=repositories',

)
