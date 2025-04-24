These are helpers for raspbian bookworm

sudo apt update
sudo apt upgrade
reboot
sudo apt install git python-dev-is-python3
sudo raspi-config nonint do_i2c 0

git clone https://github.com/Deepthought-Solutions/rasptank
cd rasptank
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

rpicam-hello --list-cameras

cat /etc/debian_version 
12.10




You can also stream video over TCP. As before, we can send an unencapsulated H.264 stream over the network. To use a Raspberry Pi as a server:

rpicam-vid -t 0 -n --inline --listen -o tcp://0.0.0.0:<port>

To view video streamed over TCP using a Raspberry Pi as a client, assuming the server is running at 30 frames per second, use the following command:

ffplay tcp://<ip-addr-of-server>:<port> -vf "setpts=N/30" -fflags nobuffer -flags low_delay -framedrop
