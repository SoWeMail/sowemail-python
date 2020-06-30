#########################################################
# Various types of extensible SoWeMail related exceptions
#########################################################


class SoWeMailException(Exception):
    """Wrapper/default SoWeMail-related exception"""
    pass


class ApiKeyIncludedException(SoWeMailException):
    """Exception raised for when SoWeMail API Key included in message text"""

    def __init__(self,
                 expression="Email body",
                 message="SoWeMail API Key detected"):
        """Create an exception for when SoWeMail API Key included in message text

            :param expression: Input expression in which the error occurred
            :type expression: string
            :param message: Explanation of the error
            :type message: string
        """
        self._expression = None
        self._message = None

        if expression is not None:
            self.expression = expression

        if message is not None:
            self.message = message

    @property
    def expression(self):
        """Input expression in which the error occurred

        :rtype: string
        """
        return self._expression

    @expression.setter
    def expression(self, value):
        """Input expression in which the error occurred

        :param value: Input expression in which the error occurred
        :type value: string
        """
        self._expression = value

    @property
    def message(self):
        """Explanation of the error

        :rtype: string
        """
        return self._message

    @message.setter
    def message(self, value):
        """Explanation of the error

        :param value: Explanation of the error
        :type value: string
        """
        self._message = value
