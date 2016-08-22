# PyLetMeCreate

This is the python binding of the LetMeCreate library. It requires Python 3. See [LetMeCreate](https://github.com/francois-berder/LetMeCreate) for the complete list of interface and click board supported.

## Integration in Openwrt

Before reading any further, make sure that you installed the LetMeCreate library as shown on its github page.


### Installation steps

Clone the library and openwrt somewhere on you computer:

```sh
$ mkdir ci-40
$ cd ci-40
$ git clone https://github.com/CreatorDev/openwrt.git
$ mkdir -p custom/pyletmecreate
$ cd custom/pyletmecreate
```
#### Stable release

If you are only interested in getting the latest release of LetMeCreate library, then download a copy of Makefile.stable located in miscellaneous folder. Copy this file inside the pyletmecreate folder you have just created and rename it to Makefile.

#### Development configuration

If you are interested in modifying the library, getting the latest changes, then clone it in custom/pyletmecreate folder you just created:

```sh
$ git clone https://github.com/francois-berder/PyLetMeCreate.git
```

Copy the Makefile to the right location:
```sh
$ cp PyLetMeCreate/miscellaneous/Makefile.devel Makefile
```

This project uses two branches. The dev branch contains all the latest changes and should not be considered stable. The dev branch is sometimes merged to master once new features are considered stable.

#### Register PyLetMeCreate in Openwrt

To register the feed in openwrt, go back in openwrt folder and open feeds.conf.default.
Add this line:
```
src-link custom /change/this/path/to/the/location/of/ci-40/custom/directory/
```

Update and install all feeds:
```sh
$ ./scripts/feeds update -a
$ ./scripts/feeds install -a
```
Select python3-letmecreate in make menuconfig. It will automatically select python3 and letmecreate. Then, compile Openwrt:

```sh
$ make -j1 V=s
```
To create an ipk, run this command (only possible once you built Openwrt once):

```sh
$ make package/pyletmecreate/{clean,compile} -j1 V=s
```

### Installation of PyLetMeCreate on Ci40

#### Install PyLetMeCreate using ipk

In openwrt folder, the ipk is located in bin/pistachio/packages/custom. Transfer it to your Ci40 using scp:
```sh
$ scp bin/pistachio/packages/custom/python3-letmecreate_1.0.1_pistachio.ipk root@<ip-of-your-ci40>:/tmp
```

On you Ci40:
```sh
$ opkg install /tmp/python3-letmecreate_1.0.1_pistachio.ipk
```

#### Install PyLetMeCreate by copying letmecreate folder


In your PyLetMeCreate folder, transfer the files to:
```sh
$ scp letmecreate root@<ip-of-your-Ci40>:/usr/lib/python3.5/site-packages
```

This will only work if python3.5 is already installed on your Ci40. You might need to change the directory path if you have a different version of Python installed.
