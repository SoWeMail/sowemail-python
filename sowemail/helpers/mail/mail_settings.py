class MailSettings(object):
    """A collection of mail settings that specify how to handle this email."""

    def __init__(self,
                 bcc_settings=None,
                 footer_settings=None,
                 sandbox_mode=None):
        """Create a MailSettings object

        :param bcc_settings: The BCC Settings of this MailSettings
        :type bcc_settings: BCCSettings, optional
        :param footer_settings: The default footer specified by this
                                MailSettings
        :type footer_settings: FooterSettings, optional
        :param sandbox_mode: Whether this MailSettings enables sandbox mode
        :type sandbox_mode: SandBoxMode, optional
        """
        self._bcc_settings = None
        self._footer_settings = None
        self._sandbox_mode = None

        if bcc_settings is not None:
            self.bcc_settings = bcc_settings

        if footer_settings is not None:
            self.footer_settings = footer_settings

        if sandbox_mode is not None:
            self.sandbox_mode = sandbox_mode

    @property
    def bcc_settings(self):
        """The BCC Settings of this MailSettings.

        :rtype: BCCSettings
        """
        return self._bcc_settings

    @bcc_settings.setter
    def bcc_settings(self, value):
        """The BCC Settings of this MailSettings.

        :param value: The BCC Settings of this MailSettings.
        :type value: BCCSettings
        """
        self._bcc_settings = value

    @property
    def footer_settings(self):
        """The default footer specified by this MailSettings.

        :rtype: FooterSettings
        """
        return self._footer_settings

    @footer_settings.setter
    def footer_settings(self, value):
        """The default footer specified by this MailSettings.

        :param value: The default footer specified by this MailSettings.
        :type value: FooterSettings
        """
        self._footer_settings = value

    @property
    def sandbox_mode(self):
        """Whether this MailSettings enables sandbox mode.

        :rtype: SandBoxMode
        """
        return self._sandbox_mode

    @sandbox_mode.setter
    def sandbox_mode(self, value):
        """Whether this MailSettings enables sandbox mode.

        :param value: Whether this MailSettings enables sandbox mode.
        :type value: SandBoxMode
        """
        self._sandbox_mode = value

    def get(self):
        """
        Get a JSON-ready representation of this MailSettings.

        :returns: This MailSettings, ready for use in a request body.
        :rtype: dict
        """
        mail_settings = {}
        if self.bcc_settings is not None:
            mail_settings["bcc"] = self.bcc_settings.get()

        if self.footer_settings is not None:
            mail_settings["footer"] = self.footer_settings.get()

        if self.sandbox_mode is not None:
            mail_settings["sandbox_mode"] = self.sandbox_mode.get()

        return mail_settings
