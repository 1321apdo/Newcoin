[app]

# (string) Title of your application
title = قائمة مهام AdMob

# (string) Package name
package.name = todoadmob

# (string) Package domain (needed for android packaging)
package.domain = domain.name

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application version
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,jnius,android

# (str) Custom source for any requirements
# requirements.source.kivymd = %(source.dir)s/kivymd

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK API to use
android.ndk_api = 21

# (str) Android NDK version to use
android.ndk_version = 25.1.8937393

# (bool) Use private storage for to private data
android.private_storage = True

# (list) Android application meta-data to set (key=value)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8214981197607739~2379374465

# (list) Android gradle dependencies
android.gradle_dependencies = com.google.android.gms:play-services-ads:20.6.0

# (bool) Android accept SDK license
android.accept_sdk_license = True

# (bool) Skip update of Android SDK/NDK artifacts
android.skip_update = False

# (list) The Android archs to build for.
android.archs = armeabi-v7a, arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
