![logo](https://static.creatordev.io/logo-md-s.svg)


# PyLetMeCreate

This is the python binding of the LetMeCreate library. It requires Python 3. See [LetMeCreate](https://github.com/francois-berder/LetMeCreate) for the complete list of interface and click board supported.
PyLetMeCreate relies on LetMeCreate, hence it is important that both versions match. 

Examples are installed in /usr/bin/pyletmecreate_examples.

## Integration in Openwrt

PyLetMeCreate is already part of Imagination Technologies' OpenWrt.
To compile the library (only possible once you built Openwrt once):

```sh
$ make package/pyletmecreate/{clean,compile} -j1 V=s
```

### Installation steps

You can install PyLetMeCreate package on OpenWRT executing:

```sh
$ opkg install pyletmecreate
```

Each release has the ipk as an attachment. You can download the ipk, copy it to your Ci40 and install with opkg:

```sh
$ opkg install path-to-the-ipk
```

### Usage example


```python
#!/usr/bin/env python3
"""This example shows how to read the temperature using a Thermo3 Click
on Mikrobus 1.
"""

from letmecreate.core import i2c
from letmecreate.core.common import MIKROBUS_1
from letmecreate.click import thermo3


# Initialise I2C on Mikrobus 1
i2c.init()
i2c.select_bus(MIKROBUS_1)

# Read temperature
thermo3.enable(0)
print('{} degrees celsius'.format(thermo3.get_temperature()))
thermo3.disable()

# Release I2C
i2c.release()
```

## This repository is no longer maintained.

Issue reports and pull requests will not be attended.

---

