# Windows Classes vs. Interface Classes

It is important to distinguish between the two types of device classes: device interface classes and device setup 
classes. The two can be easily confused because in user-mode code the same set of device installation functions and 
the same set of data structures (device information sets) are used with both classes. Moreover, a device often belongs 
to both a setup class and several interface classes at the same time. Nevertheless, the two types of classes serve 
different purposes, make use of different areas in the registry, and rely on a different set of header files for 
defining class GUIDs.

- _**Device setup classes**_ provide a mechanism for grouping devices that are installed and configured in the same way. 
A setup class identifies the class installer and class co-installers that are involved in installing the devices that 
belong to the class. For example, **all CD-ROM drives belong to the CDROM setup class and will use the same co-installer 
when installed**.

- _**Device interface classes**_ provide a mechanism for grouping devices according to shared characteristics. Instead of 
tracking the presence in the system of an individual device, drivers and user applications can register to be notified 
of the arrival or removal of any device that belongs to a particular interface class.

### Overview of Device Setup Classes

To facilitate device installation, devices that are set up and configured in the same manner are grouped into a device 
setup class. For example, SCSI media changer devices are grouped into the MediumChanger device setup class. The device 
setup class defines the class installer and class co-installers that are involved in installing the device.

Microsoft defines setup classes for most devices. IHVs and OEMs can define new device setup classes, but only if none 
of the existing classes apply. For example, a camera vendor does not have to define a new setup class because cameras 
fall under the Image setup class. Similarly, uninterruptible power supply (UPS) devices fall under the Battery class.

There is a GUID associated with each device setup class. System-defined setup class GUIDs are defined in Devguid.h and 
typically have symbolic names of the form GUID_DEVCLASS_Xxx.

### Overview of Device Interface Classes

Any driver of a physical, logical, or virtual device to which user-mode code can direct I/O requests must supply some 
sort of name for its user-mode clients. Using the name, a user-mode application (or other system component) identifies 
the device from which it is requesting I/O.

In Windows NT 4.0 and earlier versions of the NT-based operating system, drivers named their device objects and then 
set up symbolic links in the registry between these names and a user-visible Win32 logical name.

Starting with Windows 2000, drivers do not name device objects. Instead, they make use of device interface classes. 
A device interface class is a way of exporting device and driver functionality to other system components, including 
other drivers, as well as user-mode applications. A driver can register a device interface class, then enable an 
instance of the class for each device object to which user-mode I/O requests might be sent.

Each device interface class is associated with a GUID. The system defines GUIDs for common device interface classes 
in device-specific header files. **Vendors can create additional device interface classes**.

For example, three different types of mouse devices could be members of the same device interface class, even if one 
connects through a USB port, a second through a serial port, and the third through an infrared port. Each driver 
registers its device as a member of the interface class GUID_DEVINTERFACE_MOUSE. This GUID is defined in the header 
file Ntddmou.h.

Typically, drivers register for only one interface class. However, _**drivers for devices that have specialized 
functionality beyond that defined for their standard interface class might also register for an additional class**_. 
For example, a driver for a disk that can be mounted should register for both its disk interface class 
(GUID_DEVINTERFACE_DISK) and the mountable device class (MOUNTDEV_MOUNTED_DEVICE_GUID).

When a driver registers an instance of a device interface class, the **_I/O manager associates the device and the device 
interface class GUID with a symbolic link name_**. The link name is stored in the registry and persists across system 
starts. An application that uses the interface can query for instances of the interface and receive a symbolic link 
name representing a device that supports the interface. **_The application can then use the symbolic link name as a target 
for I/O requests_**.


###### Examples

Let's take an example of a device (Intel Management Engine Interface).

**_Instance ID_**:                PCI\VEN_8086&DEV_02E0&SUBSYS_22B117AA&REV_00\3&11583659&0&B0 <br>
**_Device Description_**:         Intel(R) Management Engine Interface <br>
**_Class Name_**:                 System <br>
**_Class GUID_**:                 {4d36e97d-e325-11ce-bfc1-08002be10318} <br>
**_Manufacturer Name_**:          Intel <br>

The class guid shown above is the setup class GUID with the name of System. A system setup class guid can have multiple 
devices registered to it. Similarly, a device can have multiple interface classes registered for it.

**_Device Instance Id_**:         PCI\VEN_8086&DEV_02E0&SUBSYS_22B117AA&REV_00\3&11583659&0&B0 <br>
**_Interface Path_**:             \\?\PCI#VEN_8086&DEV_02E0&SUBSYS_22B117AA&REV_00#3&11583659&0&B0#{e2d1ff34-3458-49a9-88da-8e6915ce9be5} <br>
**_Interface Class Guid_**:       {e2d1ff34-3458-49a9-88da-8e6915ce9be5} <br>

