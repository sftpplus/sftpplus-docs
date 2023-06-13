# Copyright (c) 2021 Adi Roiban.
# See LICENSE for details.
"""
Helpers to create the documentation pages.
"""
from brink.pavement_commons import pave
from sftpplus_website import MODULE_PATH


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
    destination, project, version, theme_name='standalone', html_context=None,
        ):
    """
    Generates the configuration files for creating Sphinx based
    documentation.

    Configuration file is stored in 'destination' file, and should
    be named 'conf.py'.
    """

    # These are the variables injected in the Jinja template.
    html_context_values = {
        'wip_redirect': '',
        'robots': 'noindex, nofollow',
        'canonical_site': (
            'https://www.sftpplus.com/documentation/sftpplus/latest/'),
        }
    if html_context:
        html_context_values.update(html_context)
    html_context_parts = ['html_context = {']
    for key, value in html_context_values.items():
        html_context_parts.append('"%s": "%s",' % (key, value))
    html_context_parts.append('}')
    html_context_raw = '\n'.join(html_context_parts)

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
templates_path = ['%(themes_path)s']
html_static_path = ['_static']
html_theme_path = ['%(themes_path)s']
html_theme = '%(theme_name)s'
project = "%(project)s"
copyright = "%(copyright)s"

version = "%(version)s"
release = "%(version)s"

autodoc_default_flags = ['members']
primary_domain = 'py'

pdf_documents = [(
    'index',
    '%(project)s-%(version)s',
    '%(project)s Documentation',
    '%(copyright)s',
    )]
pdf_stylesheets = ['sphinx', 'kerning', 'a4']
pdf_use_toc = False
pdf_toc_depth = 2

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    ]

%(html_context)s
""" % (  # Indentation here is strange, since we use multi-line string.
        {
            'theme_name': theme_name,
            'project': project,
            'version': version,
            'copyright': 'ProAtria Team',
            'themes_path': pave.fs.join([MODULE_PATH, 'sphinx']),
            'html_context': html_context_raw,
            }
        )

    with open(pave.fs.join(destination), 'w') as conf_file:
        conf_file.write(content)


def build_documentation(
    project,
    version,
    arguments=None,
    theme='standalone',
    html_context=None,
        ):
    """
    Build project documentation and return exit code.

    To re-build the whole documentation use ['-a', '-E', '-n']
    To test the documentation use ['-a', '-E', '-W', '-N', '-n']
    """
    if arguments is None:
        arguments = []

    _create_configuration(
        destination=[pave.path.build, 'doc_source', 'conf.py'],
        project=project,
        version=version,
        theme_name=theme,
        html_context=html_context,
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
