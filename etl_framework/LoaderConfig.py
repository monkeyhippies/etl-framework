"""parses configuration and returns useful things"""
#pylint: disable=relative-import

from BaseConfig import BaseConfig
from config_mixins.AddFiltersMixin import AddFiltersMixin
from config_mixins.LoaderMixin import LoaderMixin
from config_mixins.BufferMixin import BufferMixin
from config_mixins.DsnMixin import DsnMixin

class LoaderConfig(BaseConfig,
                    LoaderMixin,
                    BufferMixin,
                    DsnMixin,
                    AddFiltersMixin):
    """parses configuration files"""
