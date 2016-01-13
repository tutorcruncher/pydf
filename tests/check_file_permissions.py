#!/usr/bin/env python
import os
import stat

for root, dirs, files in os.walk('env'):
    if root.endswith('/pydf/bin'):
        assert 'wkhtmltopdf' in files, '"wkhtmltopdf" not in files %r' % files
        assert len(files) == 1, 'more than file: %r' % files
        path = os.path.join(root, files[0])
        st = os.stat(path)
        perms = oct(st[stat.ST_MODE])[-3:]
        assert perms == '775', 'wrong file permissions for "%s": "%s"' % (path, perms)
