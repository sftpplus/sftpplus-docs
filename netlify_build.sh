# Command to build the docs on netfliy.
cp -r chevah /opt/buildhome/python3.12/lib/python3.12/site-packages/
mkdir -p deploy/documentation/sftpplus/latests/
sphinx-build -b html --keep-going -W -D html_theme=integrated -A robots="$DOCS_ROBOT" src/doc_source/ deploy/documentation/sftpplus/latests/

#find deploy -type f -name '*.html' -exec sed -i 's/class="reference internal" href="\([^\.]\)/class="reference internal" href=".\/\1/g' {} +
