# Command to build the docs on Netlify.


TARGET="latest"
if [ $BRANCH ]; then
  # BRANCH="v5-12-0"
  # Convert to v/5.12.0
  TARGET="${BRANCH//-/.}"
  TARGET="${TARGET/v/v/}"
fi

# Show all variables.
declare -p

# Install example code.
cp -r chevah /opt/buildhome/python3.12/lib/python3.12/site-packages/


mkdir -p deploy/documentation/sftpplus/$TARGET/

# Build the standalone version in root.
sphinx-build -b html --keep-going -W -D html_theme=standalone -A robots="$DOCS_ROBOT" src/doc_source/ deploy/
# Build the integrated version to a path that will match the website.
sphinx-build -b html --keep-going -W -D html_theme=integrated -A robots="$DOCS_ROBOT" src/doc_source/ deploy/documentation/sftpplus/$TARGET/
cp src/doc_source/_static/versions.js deploy/documentation/sftpplus/versions.js

ls -al deploy/
