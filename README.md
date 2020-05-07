# bb-connectivity
Beaglebone Green Wireless + peripherals

## Reading
* [Balena Getting Started](https://www.balena.io/docs/learn/getting-started/beaglebone-green-wifi/python/)
* [Docker](https://docker-curriculum.com/)
* [Docker Compose](https://www.baeldung.com/docker-compose)

### Generating your Dev Environment:
1. Clone this repository to your computer.
```
$ git clone git@github.com:dawnho/bb-connectivity.git
```

2. Visit the [Balena Dashboard](https://dashboard.balena-cloud.com/apps), and create a new Application. The settings should as follows:
  - Application Name: Whatever you want, might be nice to put your name on it.
  - Default Device Type: Beaglebone Green Wireless
  - Application Type: Starter

3. Download the Installer [Balena Client](https://github.com/balena-io/balena-cli/releases) and install on your laptop.

4. Install Docker (version [18.06.1-ce, build e68fc7a](https://download.docker.com/mac/stable/26764/Docker.dmg))
 Note: the newest version of Docker will not work. Don't update your Docker!
 Balena's preload function is dependent on the AUFS feature, which has been deprecated.

5. Login to your balena account
```
$ balena login
```

6. Upload a code release to your application
```
$ cd {into location of your bb-connectivity repo}`
$ balena push {name of your Application}
```

7. Navigate back to 'Devices', click 'Add device', select the following settings, and Download your SD card image:
  - Device Type: Beaglebone Green Wireless
  - BalenaOS Version: latest is okay
  - Select Edition: Development (this is preferable for development b/c you can ssh into the device directly. [More details on differences between the two editions](https://www.balena.io/docs/reference/OS/overview/2.x/#dev-vs-prod-images) can be found here.)
  - Network Connection: Ethernet Only or Wireless works.

8. Preload the image with your latest code release (this step is optional, the pi will download the latest release automatically when it's connected to the internet).
`$ balena preload {location of image file} --app {app id as found in Balena Application URL} --commit latest`

9. Burn the image onto an SD card. I like to use [Etcher](https://etcher.io/) for that.

10. Make sure the power is not plugged in on your Beaglebone Green Wireless.

11. Plug in your SD card into your Beaglebone Green Wireless:

![BBG SD](https://i.imgur.com/idthJQv.jpg)

12. Hold down the "User button", while you plug in the power, hold the button until you see the blue lights flashing wildly.

![BBG flashing](https://i.imgur.com/Ek3ebMY.jpg)

13. To connect your Pi to internet directly via an ethernet cable, follow [this guide](https://docs.google.com/document/d/1izqZt8YVsLykwC0sS3_QU7IvVkBN85xsrnbxHEeQqzA/edit). You'll need this step if you skipped Step 10 (the `balena preload ...` step).

### Pushing your Code Changes
Once you have a development pi set up (according to the above instructions), you can push code changes like so:
```
$ balena push {Application Name}
```

If this flow is too slow for you (which it will be, it takes a few minutes), you can make live changes to the pi by directly sshing into it:
```
$ balena ssh {uuid of device}
```
To see the list of running docker containers:
```
$ balena ps -a
```
To enter a particular docker container:
```
$ balena exec -it {name of container} /bin/bash
```

You might want to install `curl` or `vim` on your development image, so that you can make live edits on the Pi, you can do this by adding those packages in the install sequence on the image Dockerfile.

## Breakdown of each Docker container
- [./i2c](./i2c): i2c set up (don't use, copied from raspberry pi)
- [./spi](./spi): SPI, also untested, don't use
- [./uart](./uart): Look at me! Uart!
