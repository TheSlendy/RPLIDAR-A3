#RPLIDAR A3 REALTIME DATA READING

#### How to build

1. Go into the Take_measurements folder

```
cd Take_measurements
```
2. Compile it
```
make
```
3. The program will be in
```
Take_measurements/output/Linux/Release/measure
```

#### How to take measurements

1. Make sure both USB ports of the rplidar are connected
2. Copy the measure binary anywhere or just go to the output (Take_measurements/output/Linux/Release/measure) folder
3. Run it
```
sudo ./measure
```
**Note:** The program assumes that the lidar is on /dev/ttyUSB0, if that is not the case you can call the program with the correct path, for example:
```
sudo ./measure /dev/ttyUSB1
```
4. When you need to stop a program press CTRL+C
