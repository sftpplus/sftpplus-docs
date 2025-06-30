# Command to build the docs on Netlify.
set -eo  # We want to stop the build on any error.

TARGET="latest"
if [ $BRANCH ]; then
  # Possible values
  # BRANCH="main"
  # BRANCH="v5-12-0"
  if [ $BRANCH != "main" ]; then
    # Convert to v/5.12.0
    TARGET="${BRANCH//-/.}"
    TARGET="${TARGET/v/v/}"
  fi
fi

# Show all variables.
declare -p

# Install example code.
python -m site
SITE_PACKAGES=`python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])'
`
cp -r chevah $SITE_PACKAGES


mkdir -p deploy/documentation/sftpplus/$TARGET/

# Build the standalone version in root.
sphinx-build -b html --keep-going -W -D html_theme=standalone -A robots="$DOCS_ROBOT" src/doc_source/ deploy/
# Build the integrated version to a path that will match the website.
sphinx-build -b html --keep-going -W -D html_theme=integrated -A robots="$DOCS_ROBOT" src/doc_source/ deploy/documentation/sftpplus/$TARGET/
cp src/doc_source/_static/versions.js deploy/documentation/sftpplus/versions.js

# Update the download pages
mkdir -p deploy/documentation/sftpplus/trial/
cp -r download_pages/trial.html deploy/documentation/sftpplus/trial/index.html

ls -al deploy/
