# -*- coding: utf-8 -*-
import werkzeug

from odoo.addons.website_sale.controllers import main as main_file


class QueryURL(object):
    def __init__(self, path="", **args):
        self.path = path
        self.args = args

    def __call__(self, path=None, **kw):
        if not path:
            path = self.path
        is_category = path.startswith("/shop/category/")
        for k, v in self.args.items():
            if is_category and k == "search":
                continue
            kw.setdefault(k, v)
        lst = []
        for k, v in kw.items():
            if v:
                if isinstance(v, list) or isinstance(v, set):
                    lst.append(werkzeug.url_encode([(k, i) for i in v]))
                else:
                    lst.append(werkzeug.url_encode([(k, v)]))
        if lst:
            path += "?" + "&".join(l)
        return path


main_file.QueryURL = QueryURL
