# Bluetooth-YT-Music-On-Demand
Use your mobile phone as a server and automatically play YouTube songs in a Bluetooth speaker whenever a song requested by any other device.
## Use Case Scenario
Parties are incomplete without a music player. Let's say, you're hosting a party and you're having a Bluetooth speaker. You can connect only a single device to the speaker. If anyone wants to play a song, they should come to you and request the song. And it's up to you whether you want to play it or not. If you didn't play it because your other friends don't like it, your friends won't be having good time and the reason they think is you because you've just denied their request. Or if you play it, your other friends won't be having a good time.

Stuck in the middle of this dilemma? This tool is here to help! You can host a server on your mobile so that your friends can visit it using your phone's IP address and send a YouTube song link that they want to be played on the speaker.

Oh, but what if others try to send another link before a song finishes? Not an issue. The server won't accept any new song until the current song is finished playing. It's completely based on **First Come First Serve basis**. So your friends have to be ready with their song links to submit, whenever the currently playing song is coming to an end. This puts you on a safer side as not being able to request a song on time is technically their fault.
## Working
The Django server needs to be hosted in your mobile with the Hotspot & Bluetooth turned on. The mobile should be connected to the speakers via Bluetooth. In order to request a song link using other device, the device should first be connected to your mobile hotspot and the server homepage should be visited in their browser using your mobile IP address along with the server port number. The server homepage consists of an input text field where you can provide the link and a submit button. On clicking submit, the provided YouTube link will be opened on your mobile and the audio will be played through the speaker. You can't operate your mobile while using this tool. So it's better to dedicate a mobile phone just for this purpose.
## Implementation
### Requirements
- Android Phone with at least version 7.0 and above
- Internet
- Pydroid3 App
- Django Framework
- Mozilla Firefox Nightly App
- Bluetooth Speaker (only for streaming music. Also works without this)
### Setup
<details>
<summary><h4>Setting up Pydroid3</h4></summary>
Install <a href="https://play.google.com/store/apps/details?id=ru.iiec.pydroid3">Pydroid3</a> from the Play Store in your mobile phone with Android of at least 7.0 version.

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
Download this repository on your mobile by turning on the desktop mode in your browser and clicking the green ***Code*** button and ***Download ZIP***. After downloading, extract the ZIP file anywhere in your mobile. You should have the `Bluetooth-YT-Music-On-Demand-master` folder, inside which you may or may not have a folder again with the same name (Depends on the way you extract in your mobile).

Open Pydroid3 and go to the terminal again and navigate into this folder by executing the following command if you have extracted it into your `Download/` folder:

    cd Download/Bluetooth-YT-Music-On-Demand-master/Bluetooth-YT-Music-On-Demand-master/
If you don't have another folder inside the `Bluetooth-YT-Music-On-Demand-master` folder with the same name, then execute the following command:

    cd Download/Bluetooth-YT-Music-On-Demand-master/
Or else if you've extracted it to somewhere else, then provide that directory after `cd` and execute it.

After navigating to the relevant folder, execute the following command to start hosting the server:

    python manage.py runserver 0.0.0.0:8000
Voila! Now the server is up and running. You can test it by visiting [127.0.0.1:8000](http://127.0.0.1:8000) in your browser. This is the Homepage of the server. However, the setup hasn't finished yet. So let's close the terminal for now.
</details>

<details>
<summary><h4>Configuring Firefox Nightly</h4></summary>
<em>(If you have a YouTube Premium account, you can skip to the "<a href="#for-youtube-premium-users">For YouTube Premium Users</a>" section below. You don't need to install Firefox and set the defaults. The goal here is to avoid ads at all costs.)</em><br><br>

Install [Firefox Nightly Browser](https://play.google.com/store/apps/details?id=org.mozilla.fenix) on your mobile from the Play Store. We are using this browser because autoplay on every other mobile browsers has been disabled ever since. So either no other mobile browser will allow a video to be played immediately when a website is visited, or they'll play it only on mute. Even YouTube does the same thing. Only this mobile browser has the option to enable it. Do it by navigating to the browser `Settings`, then `Site Permissions` and enable `Autoplay` by clicking the first option and selecting the `Allow audio and video` option inside.

<img src="https://user-images.githubusercontent.com/65415209/165261330-849892ac-3787-4d4e-8ddc-3fa0c4aed6fe.gif" width="25%"></img>

Now the videos will be autoplayed, but only on mute. On using desktop mode, the autoplay will work perfectly. So we have to set the desktop view as the default view for displaying the webpages. In order to set that, type `about:config` in the address bar and press Enter. Then tap the the Plus (+) icon on the top left corner, then enter `general.useragent.override` for the *"Name"* and select *"String"* as the type, instead of *"Boolean"*. For *"Enter a string"*, paste the following: `Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0` and click on *"Create"*. And that's it! The Firefox will now display the webpages in the desktop view by default.

<img src="https://user-images.githubusercontent.com/65415209/165261841-cacf969f-a902-417e-ab13-7aebd98280f6.png" width="25%"></img>
</details>

<details>
<summary><h4>Setting Defaults<h4></summary>
Now lastly, we have to make the Firefox as the default browser and stop YouTube from opening the YouTube links in the YouTube App. To do that go to <code>Default Apps</code> in your mobile settings and make the Firefox Nightly as the Default Browser App.
<br><br>
<img src="https://user-images.githubusercontent.com/65415209/165272834-8fc96abc-723e-40a0-9cfd-dccbeb59886e.png" width="25%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/165273685-697443a9-a2b9-4a3b-baf5-535935f2e2ac.png" width="25%"></img>

In `Opening Links` section find YouTube and select `Don't allow app to open links` for the `Open supported links` option.

<img src="https://user-images.githubusercontent.com/65415209/165274662-321142d4-e83a-45f1-a279-33e448521906.png" width="25%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/165274044-1565d085-b821-45c9-9dc8-8fcc5fcdfef4.png" width="25%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/165274442-f3f44108-976e-400b-8daa-8494bf64b30c.png" width="25%"></img>
</details>

<details>
<summary><h4>For YouTube Premium Users</h4></summary>
If you have YouTube Premium, skip the above two steps. You only have to set the <code>YT_PREMIUM</code> variable to <code>True</code> in the <a href="https://github.com/Raj-Srikar/Bluetooth-YT-Music-On-Demand/blob/master/todo/views.py#L12">views.py file on the line-12</a>. You should be signed in, in your YouTube app with your Premium account. The server will then use the YouTube app to play the songs.
<br><br>

***Finally, we're now done with the Setup.***

</details>

### Usage
<details>
<summary><h4>Using the Music Server</h4></summary>
Now that everything has been setup, it's time to put this tool at work! So firstly we should connect our mobile to the Bluetooth speaker and turn on the mobile internet and hotspot. Know the IP Address of your mobile by navigating to the `About Phone` in mobile settings and clicking on the `IMEI & IP` option. Under the IP address section you can find your IP address. Better note it down somewhere because you have to share it with your friends so that they can access the homepage of the server using this IP.
<br><br>
<img src="https://user-images.githubusercontent.com/65415209/165276126-05716006-a0dc-4fb8-83af-1101bc7cd701.png" width="25%"></img>

Now fire up the server using previously mentioned command in the Pydroid3 terminal. Then start using the split screen while the terminal is open (this prevents the android from killing the pydroid terminal session). And that's pretty much it for setting up the server. You can leave your mobile aside now.

<img src="https://user-images.githubusercontent.com/65415209/165275665-5cd18c68-1edb-4ec7-88d9-8c6d9b20ffc9.png" width="25%"></img>

Now to access the homepage of the server from another device, you just have to connect to your mobile hotspot and type in the IP address of your mobile that you've noted earlier in the address bar of any browser in this device and add `:8000` at the end and hit Enter. You'll see this page on doing so:

<img src="https://user-images.githubusercontent.com/65415209/165276701-df4609bd-3f36-4b58-b17e-9bddf16868c3.jpg" width="20%"></img>

You can now paste the YouTube song link in the text field and click on submit.

<img src="https://user-images.githubusercontent.com/65415209/165276765-c206415a-9437-4118-ab2b-6dadca9cfc76.jpg" width="20%"></img>

The YouTube video will be opened on **your** mobile in the Firefox browser on the other half of the split screen and it will start playing automatically. The audio will be streamed to a Bluetooth speaker, if connected.

<img src="https://user-images.githubusercontent.com/65415209/165984492-62fa06c0-28fe-46df-9f17-e806deaddd8f.png" width="25%"></img>

Or if you have YT Premium and have skipped the Firefox setup, the YouTube app will be opened on the other half of the split screen and the video will start playing in the application.

<img src="https://user-images.githubusercontent.com/65415209/165984106-f4bb870e-bfe1-427c-b3a6-d6fdb2eeac02.png" width="25%"></img>

On submitting another song before the current song is finished, the server will display this page on the other devices:

<img src="https://user-images.githubusercontent.com/65415209/164992195-dfbc8846-8a8f-46f1-96eb-c47da18b6920.jpg" width="20%"></img>

</details>

<details>
<summary><h4>Using the Admin Panel</h4></summary>
&emsp;As an owner, you can make the server available and unavailable to accept new song requests, from any device that's connected to the server. To enable this feature follow the steps below:
<ol><li><details><summary><h5>Adding a user:</h5></summary>

Log in to the Django server Admin panel by going to `/admin` (add this at the end of your server URL) with the credentials, username as `user` and password as `password`.

<img src="https://user-images.githubusercontent.com/65415209/166682662-4da99daf-305e-4dfe-9509-e0c8e57a42ca.jpg" width="20%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/166682791-d302452a-3ea9-4da5-b3c6-6fb8c2e8f121.jpg" width="20%"></img>

Now click <code><img src="https://user-images.githubusercontent.com/93818916/166888195-64d359cd-67cc-4bd9-8694-ddcc8c5019c4.svg"></img> Add</code> button near the `Users` and fill in your new credentials in this page and click save when you're done.

<img src="https://user-images.githubusercontent.com/65415209/166685826-65bbe29d-d22e-44c3-91ca-61fe0e1f4b31.jpg" width="20%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/166683433-a8fbbaa6-6fb8-4d3c-9325-8242960f4a3c.jpg" width="16%"></img>

In the next page, scroll down to `Permissions` sections and enable the `Staff status` & `Superuser status` options and scroll all the way to the bottom of the page and click the save button:

<img src="https://user-images.githubusercontent.com/65415209/166686510-b49ee9ff-655b-4a5d-9407-13f0b12d031b.jpg" width="20%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/166687024-381660b2-fbd2-48c2-aef3-e3d0c21b5e22.jpg" width="20%"></img>

Now log out and log in with your new credentials and delete the default `user` account by following the below GIF:

<img src="https://user-images.githubusercontent.com/65415209/166688083-b257cf41-13de-4da4-b3e1-f43fc2452e5f.gif" width="20%"></img>

</details>
</li>

<li>
<details><summary><h5>Setting the server status:</h5></summary>

This helps you make the server available to accept new song requests and override the currently playing song from any device, if wanted.

To do that, log in to the Django Administration with your newly created account, and select `Controls`. In the next page, the status of your server is shown under the `IS OPENED` section. "![icon-yes](https://user-images.githubusercontent.com/65415209/166694309-032b9d82-a2dd-40f2-a797-1aed08db5cac.svg)" indicates that the server is **Available** and "![icon-no](https://user-images.githubusercontent.com/65415209/166694486-d9ff8032-2065-4710-91fa-cb82ddd403c1.svg)" indicates that the server is **Unavailable**.

<img src="https://user-images.githubusercontent.com/65415209/166696473-c2f56872-85ec-47ea-a8ab-aa595e4c63cb.jpg" width="20%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/166697429-6a6a204c-f59e-4df0-815c-5c0dd90830c2.jpg" width="20%"></img>
   
Then click on the `Open for New Song Requests` option and check the CheckBox to make the player available or uncheck to make it unavailable.

<img src="https://user-images.githubusercontent.com/65415209/166698203-1ca3d4fb-3e8d-4d76-8252-a3d4e94932c8.jpg" width="20%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/166698584-0becfc9e-2d12-4631-9d4b-cad604c90b76.jpg" width="20%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/166698817-23953cba-c106-437c-bfaf-5c2078d0e09e.jpg" width="20%"></img>&ensp;<img src="https://user-images.githubusercontent.com/65415209/166698933-d7503af9-0d30-4384-8148-e3339879ffaf.jpg" width="20%"></img>

While a song is being played and the server is made unavailable after making it available, the timer will be continued so that the player can be automatically made available when the song ends, if it was played uninterruptedly.
</li>
</ol>
</details>

## Note from the Developer
It's highly recommended to have a proper internet connection. Because the buffering will mess with the working of this tool as the server sets a timer according to the video length as to when it has to start accepting a new song reuqest. As the buffering will eat up some time and make the server to accept new requests before the song even finishes, the currently playing song will be overridden by the newly requested song.

If luckily there was no buffering, then the server will nicely accept new requests only after the song ends.

*This tool was developed while having almost no knowledge about Django. Hopefully, I'll clean the code after I learn it ;)*
