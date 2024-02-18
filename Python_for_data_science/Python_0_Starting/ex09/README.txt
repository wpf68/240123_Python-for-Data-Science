
Creation d'un package :

https://python.doctor/page-python-modules-package-module-cours-debutants-informatique-programmation

https://geekflare.com/fr/create-python-packages/



Creer un environnement virtuel:
https://openclassrooms.com/fr/courses/6951236-mettez-en-place-votre-environnement-python/7014018-creez-votre-premier-environnement-virtuel

python3 -m venv env
source env/bin/activate
pip list
pip freeze

pip install wheel
python3 setup.py sdist bdist_wheel

pip install ./dist/ft_package-0.0.1-py3-none-any.whl
pip install ./dist/ft_package-0.0.1.tar.gz

pip3 show -v ft_package

pip install --force-reinstall  ./dist/ft_package-0.0.1-py3-none-any.whl

