# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Alex Comba <alex.comba@agilebg.com>
#    Copyright (C) 2014 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "MRP Group by Origin and Category",
    'version': '1.0',
    'category': 'Manufacturing',
    'description': """
Production order webkit grouped by origin and category
======================================================

* Add a webkit report on production order grouped by origin and category.

Depends on base_headers_webkit community addon available here:
`https://launchpad.net/webkit-utils <https://launchpad.net/webkit-utils>`

Contributors
------------

* Alex Comba <alex.comba@agilebg.com>
""",
    'author': 'Agile Business Group',
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    'depends': [
        'mrp',
        'report_webkit',
        'base_headers_webkit',
    ],
    'data': [
        'mrp_report.xml',
    ],
    'test': [
    ],
    'installable': True
}
