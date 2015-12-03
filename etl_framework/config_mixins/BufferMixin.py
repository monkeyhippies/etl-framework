"""parses configuration and returns useful things"""
#pylint: disable=relative-import
from etl_framework.method_wrappers.check_config_attr import check_config_attr

class BufferMixin(object):
    """parses configuration files"""

    BUFFER_SIZE_ATTR = 'buffer_size'
    SQL_STATEMENT_ATTR = 'sql_statement'
    SQL_FIELDS_ATTR = 'sql_fields'

    @check_config_attr
    def get_buffer_size(self):
        """stuff"""

        return self.config[self.BUFFER_SIZE_ATTR]

    @check_config_attr
    def get_sql_statement(self):
        """stuff"""

        return self.config[self.SQL_STATEMENT_ATTR]

    @check_config_attr
    def get_sql_fields(self):
        """stuff"""

        return self.config[self.SQL_FIELDS_ATTR]

    def get_sql_fields_and_statement(self):
        """stuff"""

        return self.get_sql_fields(), self.get_sql_statement()

    @check_config_attr
    def set_buffer_size(self, buffer_size):
        """stuff"""

        self.config[self.BUFFER_SIZE_ATTR] = buffer_size

    @check_config_attr
    def set_sql_statement(self, sql_statement):
        """stuff"""

        self.config[self.SQL_STATEMENT_ATTR] = sql_statement

    @check_config_attr
    def set_sql_fields(self, sql_fields):
        """stuff"""

        self.config[self.SQL_FIELDS_ATTR] = sql_fields

    def set_sql_fields_and_statement(self, sql_fields, sql_statement):
        """stuff"""

        self.set_sql_fields(sql_fields)
        self.set_sql_statement(sql_statement)

    def set_loader_fields_and_statement(self):
        """stuff"""

        raise NotImplementedError
