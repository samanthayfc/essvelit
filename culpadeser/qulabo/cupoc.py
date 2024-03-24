def add_network(driver, name_network):
    """Adds a network to the driver.

    Args:
        driver: A WebDriver instance.
        name_network: The name of the network to add.
    """

    network_dict = {
        'name': name_network,
        'mode': 'bridge',
        'dns': ['8.8.8.8', '8.8.4.4'],
        'dhcp4': 'true',
        'dhcp6': 'false',
        'linkLocalIPv6Address': 'fe80::1',
        'hostName': 'test-host',
        'ipRanges': ['10.0.0.0/24'],
        'mtu': 1500,
        'aliases': ['test-alias']
    }

    driver.add_network(network_dict)

