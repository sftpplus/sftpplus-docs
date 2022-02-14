# Copyright (c) 2021 Adi Roiban.
# See LICENSE for details.
"""
Helpers to create the documentation pages.
"""
from sftpplus_website import MODULE_PATH
from brink.pavement_commons import pave


def _create_html(arguments=None, source=None, target=None):
    """
    Execute the command for building the documentation in HTML format.

    This is used by the documentation and APIdoc projects.
    The Sphinx command is executed inside the build folder, and all
    paths are relative to the build folder.
    """
    from sphinx.cmd.build import main as sphinx_main
    sphinx_command = ['-n']
    if arguments:
        sphinx_command.extend(arguments)

    if source is None:
        source = [pave.path.build, 'doc_source']

    if target is None:
        target = [pave.path.build, 'doc']

    sphinx_command.extend([
        '-d', pave.fs.join([pave.path.build, 'doc_build'])])

    sphinx_command.extend([
        '-b', 'html', pave.fs.join(source), pave.fs.join(target)])

    return sphinx_main(sphinx_command)


def _create_configuration(
        destination, project, version, themes_path,
        theme_name='standalone', intersphinx_mapping=None,
        copyright='Chevah Team',
        robots=None,
        canonical_site='https://www.sftpplus.com/documentation/sftpplus/latest/',
        extra_configuration='',
        ):
    """
    Generates the configuration files for creating Sphinx based
    documentation.

    Configuration file is stored in 'destination' file, and should
    be named 'conf.py'.
    """
    if intersphinx_mapping is None:
        intersphinx_mapping = "{}"

    if robots is None:
        robots = 'noindex, nofollow'

    content = """

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    ]
suppress_warnings = ['toc.secnum']
source_suffix = '.rst'
# Ignore included files in root and in child folders from being reported
# as not part of the toctree.
exclude_patterns = ['**.include.rst', '**/*.include.rst']
master_doc = 'index'
pygments_style = 'sphinx'
smartquotes = False
html4_writer = False
html_experimental_html5_writer = True
intersphinx_mapping = %(intersphinx_mapping)s
templates_path = ['%(themes_path)s']
html_static_path = ['_static']
html_theme_path = ['%(themes_path)s']
html_theme = '%(theme_name)s'
project = "%(project)s"
copyright = "%(copyright)s"

html_context = {
    'robots': '%(robots)s',
    'canonical_site': '%(canonical_site)s',
}


version = "%(version)s"
release = "%(version)s"

autodoc_default_flags = ['members']
primary_domain = 'py'

pdf_documents = [(
    'index',
    u'%(project)s-%(version)s',
    u'%(project)s Documentation',
    u'%(copyright)s',
    )]
pdf_stylesheets = ['sphinx', 'kerning', 'a4']
pdf_use_toc = False
pdf_toc_depth = 2

%(extra_configuration)s
""" % (  # Indentation here is strange, since we use multi-line string.
        {
            'theme_name': theme_name,
            'project': project,
            'version': version,
            'intersphinx_mapping': intersphinx_mapping,
            'copyright': copyright,
            'themes_path': themes_path,
            'extra_configuration': extra_configuration,
            'robots': robots,
            'canonical_site': canonical_site,
            }
        )

    with open(pave.fs.join(destination), 'w') as conf_file:
        conf_file.write(content)


def generate_documentation(
    product_name='UNNAMED-PRODUCT',
    version='0.0.1dev0',
    copyright='No copyright.',
    arguments=None,
    theme='standalone',
    extra_configuration='',
    website_package='sftpplus.website',
    robots=None,
        ):
    """
    Generate project documentation and return exit code.

    To re-build the whole documentation use ['-a', '-E', '-n']
    To test the documentation use ['-a', '-E', '-W', '-N', '-n']
    """
    if arguments is None:
        arguments = []

    _create_configuration(
        destination=[pave.path.build, 'doc_source', 'conf.py'],
        project=product_name,
        version=version,
        copyright=copyright,
        themes_path=pave.fs.join([MODULE_PATH, 'sphinx']),
        theme_name=theme,
        robots=robots,
        extra_configuration=extra_configuration,
        )

    destination = [pave.path.build, 'doc', 'html']
    exit_code = _create_html(
        arguments=arguments,
        source=[pave.path.build, 'doc_source'],
        target=destination,
        )

    print("Documentation files generated in %s" % (
        pave.fs.join(destination)))
    print("Exit with %d." % (exit_code))
    return exit_code
