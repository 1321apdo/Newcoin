[app]
title = Todo AdMob
package.name = todoadmob
package.domain = myname
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy, kivmob, jnius, android

# Permissions
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Android build configuration
android.api = 34
android.minapi = 21
android.ndk_api = 21
android.ndk_version = 25.1.8937393
android.private_storage = True
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8214981197698574~9486833110

# Gradle configuration
android.gradle_dependencies = com.google.android.gms:play-services-ads:20.6.0

# Build configuration
android.accept_sdk_license = True
android.skip_update = False
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
