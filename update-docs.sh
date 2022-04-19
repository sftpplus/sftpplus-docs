DOCS_ROOT=`pwd`

cd $1
SERVER_ROOT=`pwd`

./brink.sh documentation_website
cp -r build-server/doc_source $DOCS_ROOT/src/
cp extension/* $DOCS_ROOT/extension/
cp -r build-server/lib/python2.7/site-packages/sftpplus_website/sphinx $DOCS_ROOT

mkdir -p $DOCS_ROOT/chevah/server/extension
touch $DOCS_ROOT/chevah/__init__.py
touch $DOCS_ROOT/chevah/server/__init__.py
touch $DOCS_ROOT/chevah/server/extension/__init__.py
cp chevah/server/extension/auth_ldap_noop.py $DOCS_ROOT/chevah/server/extension/

cd $DOCS_ROOT
rm -rf venv/lib/python2.7/site-packages/chevah
mv chevah venv/lib/python2.7/site-packages/
sed 's/^templates_path.*/templates_path = ["..\/..\/sphinx"]/'g -i src/doc_source/conf.py
sed 's/^html_theme_path.*/html_theme_path = ["..\/..\/sphinx"]/'g -i src/doc_source/conf.py
