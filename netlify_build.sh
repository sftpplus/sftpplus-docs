# Command to build the docs on netfliy.
cp -r chevah /opt/buildhome/python3.8/lib/python3.8/site-packages/
sphinx-build -b html --keep-going -W -D html_theme=integrated -A robots="$DOCS_ROBOT" src/doc_source/ deploy
echo "Debug result"
cat deploy/index.html
