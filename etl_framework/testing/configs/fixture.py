"""parses configuration and returns useful things"""
#pylint: disable=relative-import
#pylint: disable=super-on-old-class

from etl_framework.BaseConfig import BaseConfig

class FixtureConfig(BaseConfig):
    """parses configuration files"""

    @property
    def schema_from_filepath(self):

        return self.config["schema"]["from_filepath"]

    @property
    def schema(self):

        return self.config["schema"]

    @schema.setter
    def schema(self, schema):

        self.config["schema"] = schema

    @property
    def data(self):

        return self.config["data"]
