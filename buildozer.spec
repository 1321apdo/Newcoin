[app]
title = Todo AdMob
package.name = todoadmob
package.domain = myname
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy, kivmob, jnius
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8214981197698574~9486833110

[buildozer]
log_level = 2
warn_on_root = 1
