#!/usr/bin/env python
import os
import stat

virtual_env_path = os.getenv('VIRTUAL_ENV')
assert virtual_env_path, 'VIRTUAL_ENV environment variable not found'

found = False
for root, dirs, files in os.walk(virtual_env_path):
    if root.endswith('/pydf/bin') and files == ['wkhtmltopdf']:
        assert len(files) == 1, 'more than file: %r' % files
        path = os.path.join(root, files[0])
        st = os.stat(path)
        perms = oct(st[stat.ST_MODE])[-3:]
        assert perms == '775', 'wrong file permissions for "%s": "%s"' % (path, perms)
        print('"%s" has correct permissions 775' % path)
        found = True
        break

if not found:
    raise Exception('wkhtmltopdf binary not found')
