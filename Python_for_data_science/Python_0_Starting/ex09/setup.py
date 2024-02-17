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
    version='1.0.0',
    author='pwolff',
    author_email='pwolff@student.42mulhouse.fr',
    description='The count_in_list(list, string) method returns the number\
        of times the specified element appears in the list.',
    packages=find_packages(),

)

