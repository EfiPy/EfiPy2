# EfiPy2 Library
* Efi\StdLib\lib\python36.8\EfiPy2

# EfiPy2 Sample
* Efi\Apps\EfiPy2Sample

# EfiPy Information

* Here: https://github.com/EfiPy/EfiPy2
* Blog: https://efipy.blogspot.com/
* X (Twitter): https://x.com/EfiPy

* Contact: EfiPy.core@gmail.com

# Install in OS

Due to EfiPy2 is what is about hardware platform operating strcture.
Recommand using supervisor privilege to install EfiPy2.
## Linux 
```
chmod 755 install.sh
./install.sh
```

# Windows
```
install.bat
```

## Build deb package
```
apt install fakeroot python3-stdeb dh-python
python setup.py --command-packages=stdeb.command bdist_deb
```
