[app]

# (string) Title of your application (English Only)
title = Todo AdMob App

# (string) Package name
package.name = todoadmob

# (string) Package domain (needed for android packaging)
package.domain = org.test

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application version
version = 0.1

# (list) Application requirements (Only what your code needs)
requirements = python3,kivy,kivmob

# (list) Permissions required by AdMob
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk_version = 25.1.8937393

# (bool) Use private storage for to private data
android.private_storage = True

# (list) Android application meta-data (Required for AdMob to prevent crashes)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8214981197698574~9486833110

# (list) Android gradle dependencies
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.6.0

# (bool) Android accept SDK license
android.accept_sdk_license = True

# (list) The Android archs to build for.
android.archs = armeabi-v7a, arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
