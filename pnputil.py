import argparse

from winapi.cfgmgr32.constants import CM_GETIDLIST_FILTER_CLASS, CM_GETIDLIST_FILTER_NONE, CM_GETIDLIST_FILTER_PRESENT
from winapi.cfgmgr32.helper import get_all_interfaces, get_device_interfaces_with_properties, \
    get_device_via_instance_id, all_devices
from winapi.guid import GUID


def print_array(key, array):
    print_output(key, array[0])
    for i in array[1:]:
        print_output(None, i)


def print_output(key, value):
    print("{:<28}{}".format(key + ":" if key else '', value))


def enum_devices(connected=False, disconnected=False, instance_id: str = None, class_guid: str = None, ids=False,
                 interfaces=False, detailed=False):
    if instance_id:
        def data_set(): return [get_device_via_instance_id(instance_id)]
    else:
        flags = CM_GETIDLIST_FILTER_NONE
        filter_keyword = None

        if class_guid:
            GUID.is_valid(class_guid)
            filter_keyword = class_guid
            flags = CM_GETIDLIST_FILTER_CLASS

        if connected:
            flags = CM_GETIDLIST_FILTER_PRESENT

        def data_set(): return all_devices(filter_keyword=filter_keyword, flags=flags)

    for d in data_set():
        if instance_id and not d.instance_id:  # if instance_id option is specified and if the instance id doesn't exist
            print("\nNo devices were found on the system\n")
            break

        if disconnected and d.status != 'Disconnected':
            continue

        if interfaces: d.interfaces    # this statement doesn't do anything except pre-populates the Interface cache

        print_output("Instance ID", d.instance_id)
        print_output("Device Description", d.friendly_name if d.friendly_name else d.desc if d.desc else d.name)
        print_output("Class Name", d.class_name if d.class_name else 'Unknown')
        print_output("Class GUID", d.class_guid if d.class_guid else 'Unknown')
        print_output("Manufacturer Name", d.manufacturer if d.manufacturer else 'Unknown')
        print_output("Status", d.status)
        print_output("Driver Name", d.driver_inf_path if d.driver_inf_path else 'Unknown')

        if d.extended_config_ids:
            print_array("Extension Driver Names", [i.split(':', 1)[0] for i in d.extended_config_ids])

        if ids:
            if d.hw_ids:
                print_array("Hardware IDs", d.hw_ids)

            if d.compat_ids:
                print_array("Compatible IDs", d.compat_ids)

        if interfaces:
            if d.interfaces:
                print_array("Device Interfaces", [i.path for i in d.interfaces])

        if detailed:
            if d.interfaces:
                print_output("Interface Class Guid", d.interfaces[0].class_guid)

            if d.name:
                print_output("Device Name", d.name)

            if d.desc:
                print_output("Device Description", d.desc)

            if d.friendly_name:
                print_output("Friendly Name", d.friendly_name)

            if d.service:
                print_output("Service", d.service)

            if d.location_info:
                print_output("Location Info", d.location_info)

            if d.location_paths:
                print_array("Location Paths", d.location_paths)

            if d.pdo_name:
                print_output("PDO Name", d.pdo_name)

            if d.model:
                print_output("Model", d.model)

            if d.model_id:
                print_output("Model ID", d.model_id)

            if d.sds:
                print_output("Security Descriptor", d.sds)

            if d.container_id:
                print_output("Container ID", d.container_id)

            if d.is_present:
                print_output("Present", d.is_present)

            if d.stack:
                print_array("Stack", d.stack)

            if d.bios_name:
                print_output("BIOS Name", d.bios_name)

            if d.fw_version:
                print_output("Firmware Version", d.fw_version)

            if d.fw_revision:
                print_output("Firmware Revision", d.fw_revision)

            if d.install_date:
                print_output("Install Date", str(d.install_date.to_local_time()))

            if d.driver:
                print_output("Driver", d.driver)

            if d.driver_desc:
                print_output("Driver Description", d.driver_desc)

            if d.driver_version:
                print_output("Driver Version", d.driver_version)

            if d.driver_provider:
                print_output("Driver Provider", d.driver_provider)

            if d.driver_date:
                print_output("Driver Date", str(d.driver_date.to_local_time()))

            if d.driver_inf_section:
                print_output("Driver INF Section", d.driver_inf_section)

            if d.driver_inf_driver_store_location:
                print_output("Driver INF Location", d.driver_inf_driver_store_location)

        print("")


def enum_interfaces(interface_class_guid: str = None, present=False, disabled=False, device=False):
    guid = GUID.from_guid_string(interface_class_guid) if interface_class_guid else None

    if guid:
        def func(): return get_device_interfaces_with_properties(guid, present=present)
    else:
        def func(): return get_all_interfaces(present=present)

    found = False
    for i in func():
        if not found: found = True

        if disabled and i.status:
            continue

        print_output("Interface Path", i.path)
        print_output("Interface Description", i.desc if i.desc else 'Unknown')
        print_output("Interface Class Guid", i.class_guid)
        if i.reference:
            print_output("Reference String", i.reference)
        print_output("Device Instance Id", i.device_instance_id)
        print_output("Interface Status", 'Enabled' if i.status else 'Disabled')
        if device:
            d = i.device
            print_output("Device Name", d.friendly_name if d.friendly_name else d.desc if d.desc else d.name)
        print("")

    if not found:
        print("\nNo devices were found on the system\n")


main_parser = argparse.ArgumentParser(
    description='Python implementation of Microsoft PnP Utility for enumeration only.'
    ' (This has been tested to work with Windows 10 and Python 3.9 64bit)')
subparsers = main_parser.add_subparsers(title='Enumeration options', metavar="", dest='which_parser')

device_parser = subparsers.add_parser(name='/enum-devices', help='Enumerate all available devices')
device_parser.add_argument('-ids', '--ids', action='store_true', default=False,
                           help='Display hardware IDs and compatible IDs.')
device_parser.add_argument('-interfaces', '--interfaces', action='store_true', default=False,
                           help='Display all the available interface paths')
device_parser.add_argument('-d', '--detailed', action='store_true', default=False,
                           help='Display all the available info for the device')

device_parser_options = device_parser.add_mutually_exclusive_group()
device_parser_options.add_argument('-c', '--class', type=str, help='Enumerate all devices with specific class')
device_parser_options.add_argument('-i', '--instanceid', type=str, help='Enumerate device with specific instance ID')

device_parser_connectivity_options = device_parser.add_mutually_exclusive_group()
device_parser_connectivity_options.add_argument('-connected', '--connected', action='store_true', default=False,
                                                help='Enumerate only connected devices on the system')
device_parser_connectivity_options.add_argument('-disconnected', '--disconnected', action='store_true', default=False,
                                                help='Enumerate only disconnected devices on the system')

interface_parser = subparsers.add_parser(name='/enum-interfaces', help="Enumerate all interfaces")
interface_parser.add_argument('-c', '--class', type=str,
                              help='Enumerate all interfaces with specific interface class GUID')
interface_parser.add_argument('-device', '--device', action='store_true', default=False, help='Retrieve device name as well')

interface_parser_options = interface_parser.add_mutually_exclusive_group()
interface_parser_options.add_argument('-e', '--enabled', action='store_true', default=False,
                                      help='Enumerate only enabled interfaces on the system')
interface_parser_options.add_argument('-d', '--disabled', action='store_true', default=False,
                                      help='Enumerate only disabled interfaces on the system')

args = main_parser.parse_args()

if not args.which_parser:
    main_parser.print_help()

if args.which_parser == "/enum-devices":
    kwargs = {}

    if args.ids:
        kwargs['ids'] = True

    if args.connected:
        kwargs['connected'] = True

    if args.disconnected:
        kwargs['disconnected'] = True

    if args.instanceid:
        kwargs['instance_id'] = args.instanceid

    if args.interfaces:
        kwargs['interfaces'] = True

    if args.detailed:
        kwargs['ids'] = True
        kwargs['interfaces'] = True
        kwargs['detailed'] = True

    if getattr(args, 'class'):
        guid = getattr(args, 'class')

        if guid.startswith("'") and guid.endswith("'"):
            guid = guid[1:-1]

        kwargs['class_guid'] = guid

    enum_devices(**kwargs)

elif args.which_parser == "/enum-interfaces":
    kwargs = {}

    if args.enabled:
        kwargs['present'] = True

    if args.device:
        kwargs['device'] = True

    if args.disabled:
        kwargs['disabled'] = True

    if getattr(args, 'class'):
        guid = getattr(args, 'class')

        if guid.startswith("'") and guid.endswith("'"):
            guid = guid[1:-1]
        kwargs['interface_class_guid'] = guid

    enum_interfaces(**kwargs)
