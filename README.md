# Blockchain_Pi

Setting up Raspberry Pi with a blockchain connection

## Hardware setup

We will describe our approach with a defined hardware list (see below). 
Everyone who is interested can change these components to test different configurations 
and other use cases, for example, light emission or distance measuring. 
All components that we used can be found on, for example, Amazon.

The optional components (DC engine and battery pack) are used in our case for creating live results.
The Battery pack powers the DC Engine, what is creating vibrations, thermal energy, 
and power consumption that our sensors are measuring.

Hardware components:
- Raspberry Pi 3
- Case
- GPIO Breakout and Wires (Male-Male, Male-Female)
- Sensor SW-420
- Sensor WCS1800
- Sensor DHT11
- DC Engine (optional)
- Battery pack (optional)

There are no tools, like for example, a screwdriver, are needed for the whole configuration. 
The housing has clips to connect with each other, so there are also no tools needed.

Once all hardware components are available they must be connected.
We suggest to use a breakout board, for example, a general-purpose input/output (GPIO) board. 
You can find the GPIO layout for Fritzing that we used in the "Wiring" folder.

## Raspberry Pi Layout

![Wiring Layout with Fritzing](/Wiring/Layout_GPIO_Steckplatine.jpg)


After connecting all components, the Raspberry can now be connected to power. 
All sensor lights/LEDs should be on. 
If there is some vibration, the LED from the vibration sensor is blinking.


## Software setup
First of all install IPFS on your machine: https://docs.ipfs.io/introduction/install/ 
One example hash from the project is: QmPP9Co2F7pz5xdybeRAUzcb3ED4pgBusvTnzdfNhMHUVU
You can find this also at originstamp: https://originstamp.org/s/8b18e4989ab800e96d7e3ae6de9fa62906a91e68d5bccd42a0e951d9a22cceea

After this, the following package is needed for running the **API**

**MySQL**

For Python (Version 2.x or before):

```
pip install mysqlclient
```


For Python (Version 3.x):

```
pip3 install mysqlclient
```


To run the server use:

```
python API.py
python Update.py
```


