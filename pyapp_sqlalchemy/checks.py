import pyapp.checks

import pyapp_sqlalchemy.factories

# Register checks for our settings factory
pyapp.checks.register(pyapp_sqlalchemy.factories.engines, 'settings')
