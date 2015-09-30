import os
import subprocess
from tempfile import NamedTemporaryFile

__version__ = '0.21'


def execute_wk(*args):
    """
    Generate path for the wkhtmltopdf binary and execute command.

    :param args: args to pass straight to subprocess.Popen
    :return: stdout, stderr
    """
    this_dir = os.path.dirname(__file__)
    wk_name = 'wkhtmltopdf'
    wkhtmltopdf_default = os.path.join(this_dir, 'bin', wk_name)
    # Reference command
    wkhtmltopdf_cmd = os.environ.get('WKHTMLTOPDF_CMD', wkhtmltopdf_default)
    if not os.path.isfile(wkhtmltopdf_cmd):
        raise IOError('wkhtmltopdf binary not found at %s' % wkhtmltopdf_cmd)
    wk_args = (wkhtmltopdf_cmd,) + args
    p = subprocess.Popen(wk_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout, stderr, p.returncode


def generate_pdf(source,
                 quiet=True,
                 grayscale=False,
                 lowquality=False,
                 margin_bottom=None,
                 margin_left=None,
                 margin_right=None,
                 margin_top=None,
                 orientation=None,
                 page_height=None,
                 page_width=None,
                 page_size=None,
                 image_dpi=None,
                 image_quality=None,
                 **extra_kwargs):
    """
    Generate a pdf from either a url or a html string.

    After the html and url arguments all other arguments are
    passed straight to wkhtmltopdf

    For details on extra arguments see the output of get_help()
    and get_extended_help()

    All arguments whether specified or caught with extra_kwargs are converted
    to command line args with "'--' + original_name.replace('_', '-')"

    Arguments which are True are passed with no value eg. just --quiet, False
    and None arguments are missed, everything else is passed with str(value).

    :param source: html string to generate pdf from or url to get
    :param quiet: bool
    :param grayscale: bool
    :param lowquality: bool
    :param margin_bottom: string eg. 10mm
    :param margin_left: string eg. 10mm
    :param margin_right: string eg. 10mm
    :param margin_top: string eg. 10mm
    :param orientation: Portrait or Landscape
    :param page_height: string eg. 10mm
    :param page_width: string eg. 10mm
    :param page_size: string: A4, Letter, etc.
    :param image_dpi: int default 600
    :param image_quality: int default 94
    :param extra_kwargs: any exotic extra options for wkhtmltopdf
    :return: string representing pdf
    """
    is_url = any(source.strip().startswith(s) for s in ('http', 'www'))

    loc = locals()
    py_args = {n: loc[n] for n in
               ['quiet', 'grayscale', 'lowquality', 'margin_bottom', 'margin_left', 'margin_right', 'margin_top',
               'orientation', 'page_height', 'page_width', 'page_size', 'image_dpi', 'image_quality']}
    py_args.update(extra_kwargs)
    cmd_args = []
    for name, value in py_args.items():
        if value in [None, False]:
            continue
        arg_name = '--' + name.replace('_', '-')
        if value is True:
            cmd_args.append(arg_name)
        else:
            cmd_args.extend([arg_name, str(value)])

    def gen_pdf(src, cmd_args):
        with NamedTemporaryFile(suffix='.pdf', mode='rwb+') as pdf_file:
            cmd_args += [src, pdf_file.name]
            _, stderr, returncode = execute_wk(*cmd_args)
            pdf_file.seek(0)
            pdf_string = pdf_file.read()
            # it seems wkhtmltopdf's error codes can be false, we'll ignore them if we
            # seem to have generated a pdf
            if returncode != 0 and pdf_string[:4] != '%PDF':
                raise IOError('error running wkhtmltopdf, command: %r\nresponse: "%s"' %
                              (cmd_args, stderr.strip(' \n')))
            return pdf_string

    if is_url:
        return gen_pdf(source, cmd_args)

    with NamedTemporaryFile(suffix='.html', mode='w') as html_file:
        html_file.write(source.encode('utf-8'))
        html_file.flush()
        html_file.seek(0)
        return gen_pdf(html_file.name, cmd_args)


def get_version():
    """
    Get version of pydf and wkhtmltopdf binary

    :return: version string
    """
    v = 'pydf version: %s\n' % __version__
    try:
        wk_version = execute_wk('-V')[0]
    except Exception, e:
        # we catch all errors here to make sure we get a version no matter what
        wk_version = 'Error: %s' % str(e)
    v += 'wkhtmltopdf version: %s' % wk_version
    return v


def get_help():
    """
    get help string from wkhtmltopdf binary
    uses -h command line option

    :return: help string
    """
    return execute_wk('-h')[0]


def get_extended_help():
    """
    get extended help string from wkhtmltopdf binary
    uses -H command line option

    :return: extended help string
    """
    return execute_wk('-H')[0]
