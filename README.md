# vmhub3

Simple python module to send instructions to VM Hub 3 router.

### Example - Reading configs and attributes:

    import logging
    from vmhub3 import VMHub3

    logging.basicConfig(level=logging.DEBUG)

    router = VMHub3(ip='1.1.1.1', password='your-router-pwd')
    router.connect()
    router.get_global_config()
    router.get_language_config()
    router.get_languages()
    router.get_wifi_state()
    router.get_wifi_config()
    router.get_wifi_basic_config()
    router.get_wifi_advanced_config()
    router.get_status()
    router.get_wps()
    router.get_lan()

### Example - Rebooting router:

    from vmhub3 import VMHub3

    router = VMHub3(ip='1.1.1.1', password='your-router-pwd')
    router.connect()
    router.reboot()
