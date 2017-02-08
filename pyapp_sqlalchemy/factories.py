from pyapp.conf.helpers import NamedSingletonFactory, DefaultCache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__all__ = ('get_engine', 'get_connection', 'get_session')


class EngineFactory(NamedSingletonFactory):
    """
    Factory that creates SQLAlchemy engine instances from configuration.
    """
    required_keys = ('uri',)
    optional_keys = ('connect_args', 'pool_size')

    def create_instance(self, name=None):
        """
        Obtain an engine

        :rtype: sqlalchemy.engine.Engine

        """
        definition = self.get(name)
        return create_engine(definition.pop('uri'), **definition)

engines = EngineFactory('DB')
get_engine = engines.create_instance


def get_connection(name=None):
    """
    Obtain a DBAPI connection.

    :param name: Name of the configuration entry.
    :rtype: sqlalchemy.engine.Connection

    """
    return get_engine(name).connect()


class SessionFactory(object):
    """
    Factory that generates a SQLAlchemy session from configuration.
    """
    def __init__(self, engine_factory=None):
        self.engine_factory = engine_factory or engines
        self.session_maker_cache = DefaultCache(self._session_maker_factory)

    def create_instance(self, name=None):
        """
        Obtain a session.

        Note this applications default behaviour is to require explicit transactions.

        :param name: Name of the configuration entry.
        :rtype: sqlalchemy.orm.Session

        """
        return self.session_maker_cache[name]()

    def _session_maker_factory(self, name):
        engine = self.engine_factory(name)
        return sessionmaker(bind=engine, autocommit=True)

sessions = SessionFactory()
get_session = sessions.create_instance
