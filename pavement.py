"""
Build file for the SFTPPlus Documentation project.
"""
import os
import re
import sys
from pkg_resources import load_entry_point

from paver.easy import call_task, consume_args, needs, no_help, task

from brink.pavement_commons import pave, SETUP
from brink.sphinx import doc_html, test_documentation  # noqa

SETUP['website_package'] = 'sftpplus.website'
EXTRA_PYPI_INDEX = 'https://pypi.chevah.com/simple'


@task
def default():
    call_task('test_documentation')


@task
def build():
    """
    Generate documentation folder in build.
    """
    pave.fs.createFolder([pave.path.build, 'doc'])

    pave.fs.copyFile(
        source=['LICENSE'],
        destination=[pave.path.build, 'doc', 'LICENSE'],
        )

    # Binary dist are for now part of server repo.
    pave.fs.createFolder([pave.path.build, 'doc'])
    pave.fs.copyFolder(
        source=['legal'],
        destination=[pave.path.build, 'doc', 'legal'],
        )

    pave.fs.copyFile(
        source=['chevah', 'server', 'static', 'documentation', 'README'],
        destination=[pave.path.build, 'doc', 'README'],
        )
    pave.fs.copyFile(
        source=[
            'chevah', 'server', 'static', 'documentation', 'release-notes.rst'
            ],
        destination=[pave.path.build, 'doc', 'ReleaseNotes'],
        )

    documentation_source = ['chevah', 'server', 'static', 'documentation']

    pave.fs.deleteFolder(
        [pave.path.build, 'doc_source'])
    pave.fs.copyFolder(
        source=documentation_source,
        destination=[pave.path.build, 'doc_source'])
    pave.fs.createFolder([pave.path.build, 'doc_source', '_static'])


@task
@needs('build')
@no_help
def update_setup():
    """
    Updates project configuration for python files.
    """
    SETUP['product']['name'] = 'SFTPPlus'
    SETUP['product']['version'] = '1.2.3'
    SETUP['product']['version_major'] = '1'
    SETUP['product']['version_minor'] = '2'


@task
def deps():
    """
    Install all dependencies.
    """
    pip = load_entry_point('pip', 'console_scripts', 'pip')
    pip(args=[
        'install',
        '--extra-index-url', EXTRA_PYPI_INDEX,

        'sphinx==1.2.2',
        'repoze.sphinx.autointerface==0.7.1.c4',
        # Docutils is required for RST parsing and for Sphinx.
        'docutils==0.12.c1',

        'sftpplus-website==0.18.0',
        ])


@task
def test():
    """
    Run the test tests.
    """
    import nose

    coverage = load_entry_point('coverage', 'console_scripts', 'coverage')

    nose_args = ['nosetests']
    nose_args.extend([
        '--with-coverage',
        '--cover-package=chevah.keycert',
        '--cover-erase',
        '--cover-test',
        ])
    nose_code = nose.run(argv=nose_args)
    nose_code = 0 if nose_code else 1

    coverage_args = [
        'report',
        '--include=chevah/keycert/tests/*',
        '--fail-under=100',
        ]
    covergate_exit = coverage(argv=coverage_args)
    if not covergate_exit:
        print('Tests coverage OK')

    coverage(argv=['html', '-d', 'build/cover'])
    print("See HTML coverate in build/cover")

    sys.exit(nose_code or covergate_exit)


@task
def test_ci():
    """
    Run tests in the Buildbot CI environment.
    """
    test_type = os.environ.get('TEST_TYPE', '')
    if test_type == "os-independent":
        call_task('lint')
    else:
        call_task('test')



@task
def lint():
    """
    Run the static code analyzer.
    """
    from pyflakes.api import main as pyflakes_main
    from pycodestyle import _main as pycodestyle_main

    sys.argv = [
        re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])] + [
        'chevah',
        ]

    try:
        pyflakes_main()
    except SystemExit as pyflakes_exit:
        pass

    sys.argv.extend(['--ignore=E741', '--hang-closing'])
    pycodestyle_exit = pycodestyle_main()

    sys.exit(pyflakes_exit.code or pycodestyle_exit)


@task
@consume_args
def documentation_standalone(options):
    """
    Create documentation using the standalone theme.
    """
    call_task('doc_html', options={
        'production': True,
        'all': True,
        'theme': 'standalone'
        })

    website_path = pave.importAsString(
        SETUP['website_package']).get_module_path()
    pave.fs.copyFolder(
        source=[website_path, 'static'],
        destination=[pave.path.build, 'doc', 'html', 'static'])
