from odoo import _, api, exceptions, fields, models, modules
from odoo.addons.base.models.res_users import is_selection_groups


class Users(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    notification_type = fields.Selection([
        ('email', 'Handle by Emails'),
        ('inbox', 'Handle in Xamaam')],
        'Notification', required=True, default='email',
        help="Policy on how to handle Chatter notifications:\n"
             "- Handle by Emails: notifications are sent to your email address\n"
             "- Handle in Xamaam: notifications appear in your Xamaam Inbox")