# MobileApp.PY

Learning build mobile app with Kivy and Python. Document and source code from https://www.udemy.com/course/the-python-mega-course.

## Installation

```powershell
> virtualenv env
> .\env\Scripts\activate
> python -m pip install --upgrade pip
> pip install kivy
```

## Build APK for Android:
1. Extract UbuntaProjectFiles.zip to a directory on Ubuntu
```bash
> unzip UbuntaProjectFiles.zip -d MobileApp.PY
```

2. Run the `kivy-buildozer-installer.sh`:
```bash
> cd MobileApp.PY
> chmod +x kivy-buildozer-installer.sh
> ./kivy-buildozer-installer.sh
```

3. Init buildozer, this process creates 'buildozer.spec':
```bash
> buildozer init
> ls
buildozer.spec  design.kv  get-pip.py  hoverable.py  kivy-buildozer-installer.sh  logout_hover.png  logout_nothover.png  main.py  quotes  users.json
```

4. Edit `buildozer.spec` file with specific data
```bash
> nano buildozer.spec
title = Quote for feeling
source.include_exts = py,png,jpg,kv,atlas,json,txt
orientation = all
android.arch = armeabi-v8a
```

5. Run buildozer
```bash
> sudo apt-get install openjdk-8-jdk
> buildozer android debug
```