DOCS_ROOT=`pwd`

if [ "$1" == "" ]; then
    echo "Call the script with the path to the server repo."
    exit 1
fi

cd $1
SERVER_ROOT=`pwd`
PY_VER='3.12'

rm dist/*.html
./pythia.sh download_pages production
mkdir -p $DOCS_ROOT/download_pages
cp dist/trial.html $DOCS_ROOT/download_pages/trial.html

./pythia.sh documentation_website
cp -r docs/* $DOCS_ROOT/docs/
cp docs/versions.js $DOCS_ROOT/docs/_static/
cp extension/* $DOCS_ROOT/extension/
cp -r build-py3/lib/python$PY_VER/site-packages/sftpplus_website/sphinx $DOCS_ROOT

echo "Creating extensions for $DOCS_ROOT ..."
mkdir -p $DOCS_ROOT/chevah/server/extension
touch $DOCS_ROOT/chevah/__init__.py
touch $DOCS_ROOT/chevah/server/__init__.py
touch $DOCS_ROOT/chevah/server/extension/__init__.py
cp chevah/server/extension/auth_ldap_noop.py $DOCS_ROOT/chevah/server/extension/

cd $DOCS_ROOT
rm -rf venv/lib/python$PY_VER/site-packages/chevah
cp -r chevah venv/lib/python$PY_VER/site-packages/
sed 's/^templates_path.*/templates_path = ["..\/sphinx"]/'g -i docs/conf.py
sed 's/^html_theme_path.*/html_theme_path = ["..\/sphinx"]/'g -i docs/conf.py

rm -rf deploy
. venv/bin/activate
pip install -r requirements.txt
sphinx-build -b html --keep-going -W docs/ deploy
