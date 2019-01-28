# Blockchain_Pi

Seting up Raspberry Pi with Blockchain connection

## Hardware setup
```
To set up the hardware, first of all, you have to buy some components. These components can be changed, 
if you want to research other values, e.g., light emission or distances of objects. In our case, we use 
the following components. You can find them around the internet. 

Hardware components and prices
- Raspberry Pi 3
- Case
- GPIO Breakout and Wires (Male-Male, Male-Female)
- Sensor SW-420
- Sensor WCS1800
- Sensor DHT11
- DC Engine (optional)
- Battery pack (optional)

If done, all components must be connected. Because of the many wires, it is the best to use a breakout board, 
e.g., a general-purpose input/output (GPIO) board. The GPIO layout incl. The layout is in the “Wireing” 
folder. 
You can see also a DC engine and a battery pack. These components are just for testing the current, 
vibration and temperature live. You can skip this if you want to use the model, e.g., just to measure 
environmental temperature and humidity.

After connecting everything, the raspberry can now be connected to power. All sensor lights/LEDs should 
be on. 
The LED from the vibration sensor is blinking, if there is some vibration.
```

## Software setup
First of all install IPFS on your machine: https://docs.ipfs.io/introduction/install/ 
One example hash from the project is: QmPP9Co2F7pz5xdybeRAUzcb3ED4pgBusvTnzdfNhMHUVU
You can find this also at originstamp: https://originstamp.org/s/8b18e4989ab800e96d7e3ae6de9fa62906a91e68d5bccd42a0e951d9a22cceea

After this, the following package is needed for running the **API**

**Mysql**

```
pip install mysqlclient

```

Install on the used version of python. For Python3
use:
```text
pip3 install mysqlclient
```

To run the server use

```
python API.py
python Update.py
```


