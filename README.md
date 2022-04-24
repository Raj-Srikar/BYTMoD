# Bluetooth-YT-Music-On-Demand
Use your mobile phone as a server and automatically play YouTube songs in a Bluetooth speaker whenever a new song requested by any other device.
## Scenario
Parties are incomplete without a music player. Let's say, you're hosting a party and you're having a Bluetooth speaker. You can connect only a single device to the speaker. If anyone wants to play a song, they should come to you and request the song. And it's up to you whether you want to play it or not. If you didn't play it because your other friends don't like it, your friends won't be having good time and the reason they think is you because you've just denied their request. Or if you play it, your other friends won't be having a good time.

Stuck in the middle of this dilemma? This tool is here to help! You can host a server on your mobile so that your friends can visit it using your phone's IP address and send a YouTube song link they want to be played on the speaker.

Oh, but what if others try to send another link before a song finishes? Not an issue. The server won't accept any new song until the current song is finished playing. It's completely based on **First Come First Serve basis**. So your friends has to be ready with their song links whenever the currently playing song is coming to an end. This puts you on a safer side as not being able to request a song on time is technically their fault.
## Working
The Django server needs to be hosted in your mobile with the Hotspot & Bluetooth turned on. The mobile should be connected to the speakers via Bluetooth. In order to request a song link using other device, the device should first be connected to your mobile using the hotspot and the server homepage should be visited in the browser using the IP address along with the server port number. The server homepage consists of an input text field where you can provide the link and a submit button. On clicking submit the provided YouTube link will be opened on your mobile and the audio will be played through the speaker. You can't operate your mobile while using this tool. So it's better to dedicate a mobile phone just for this purpose.
## Usage
### Requirements
- Android Phone with at least version 6.0 and above
- Internet
- Pydroid3 App
- Django Framework
- Mozilla Firefox Nightly App
- Bluetooth Speaker (only for streaming music. Also works without this)
### Setup
Install Pydroid3 from the Play Store in your mobile phone with Android of at least 6.0 version.

Open the side navigation on the left side in Pydroid3 and click on "Terminal".

Now execute the following command by pasting and clicking enter and wait for the Django to install:

    pip install django

To check whether it has been installed or not, execute the following command:

    django-admin
If everything goes well, you will see this message:

<img src="https://user-images.githubusercontent.com/65415209/164992059-f074c17f-a8e8-4d5b-bed6-e3de99f77d10.png" width="35%"></img>

Install the `apscheduler`, `pafy` and `youtube-dl` libraries by executing the following commands in the terminal:

    pip install apscheduler
    pip install pafy
    pip install youtube-dl==2020.12.2
    .
Download this repository on your mobile by turning on the desktop mode and clicking the green ***Code*** button and ***Download ZIP***. After downloading, extract the ZIP file anywhere in your mobile. You should have the `Bluetooth-YT-Music-On-Demand-master` folder, inside which you may or may not have a folder again with the same name.

Open Pydroid3 and go to the terminal again and navigate into this folder by executing the following command if you have extracted it into your `Download/` folder:

    cd Download/Bluetooth-YT-Music-On-Demand-master/Bluetooth-YT-Music-On-Demand-master/
If you don't have another folder inside the `Bluetooth-YT-Music-On-Demand-master` folder with the same name, then execute the following command:

    cd Download/Bluetooth-YT-Music-On-Demand-master/
Or else if you've extracted it to somewhere else, then provide that directory after `cd` and execute it.

After navigating to the relevant folder, execute the following command to start hosting the server:

    python manage.py runserver 0.0.0.0:8000
Voila! Now the server is up and running. You can test it by visiting [127.0.0.1:8000](http://127.0.0.1:8000) in your browser. This is the Homepage of the server. However, the setup hasn't finished yet. So let's close the terminal for now.

Now install the [Firefox Nightly Browser](https://play.google.com/store/apps/details?id=org.mozilla.fenix) on your mobile from the Play Store. We are using this browser since autoplay on the mobile browsers has been disabled ever since. So either no mobile browser will allow a video to be played immediately when a website is visited on mobile, or they'll play it only on mute. Even the YouTube does the same thing. So, only this mobile browser has the option to enable it. Do it by navigating to the browser "Settings", then "Site Permissions" and enable the "Autoplay" by clicking the first option and selecting the "Allow audio and video" option inside.

Now the videos are autoplayed, but only on mute. On using desktop mode, the autoplay will work perfectly. So we have to set the desktop view as the default view for displaying the webpages. In order to set that, type `about:config` in the address bar and press Enter. Then tap the the Plus (+) icon on the top left corner, then enter `general.useragent.override` for the *"Name"* and select *"String"* as the type. For the *"Enter a string"*, paste: `Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0` there and click on *"Create"*. And that's it! The Firefox will now defaultly display the webpages in the desktop view.

Also it's highly recommended to sign in with a YouTube Premium account in the browser to prevent the annoying YouTube ads. Because they mess with the working of this tool as the server sets a timer according to the video length as to when it has to start accepting a new song reuqest. So the playing of ads will eat up some time and make the server to accept requests before the song even finishes and as a result, the song will be overridden by the newly requested song.

Now lastly, we have to make the Firefox as the default browser and stop YouTube from opening the YouTube links in the YouTube App. To do that go to `Default Apps` in your mobile settings and make the Firefox Nightly as the Default Browser App. In `Opening Links` section find YouTube and select `Don't allow app to open links` for the `Open supported links` option. Finally, we're now done with the Setup.
### Working
Now that everything has been setup, it's time to put this tool at work! So firstly we should connect our mobile to the Bluetooth speaker and turn on the mobile internet and hotspot. Know the IP Address of your mobile by navigating to the "About Phone" in the mobile settings and clicking on the "IMEI & IP" option. Under the IP address section you can find your IP address. Better note it down somewhere because you have to share it with your friends so that they can access the homepage of the server using this IP.

Now fire up the server using the previously mentioned command in the Pydroid3 terminal. Now start using the split screen while the terminal is open. And that's pretty much it for setting up the server. You can leave your mobile aside now.

Now to access the homepage of the server from another device, you just have to type in the IP address of your mobile that you've noted earlier, in the address bar of any browser in this device and add `:8000` at the end and hit Enter. You can now paste the YouTube song link in the text field and click on submit. The YouTube link will be opened on your mobile in the Firefox browser on the other half of the split screen and the video will start playing. The audio will be streamed to a Bluetooth speaker, if connected.

On submitting another song before the current song is finished, the server will display this page:

<img src="https://user-images.githubusercontent.com/65415209/164992195-dfbc8846-8a8f-46f1-96eb-c47da18b6920.jpg" width="30%"></img>

If luckily no ads are played at the beginning of the song, then the server will nicely accept new requests only after the song ends. That's why a premium YouTube account is preferred.

