rpicam-hello --list-cameras

cat /etc/debian_version 
12.10




You can also stream video over TCP. As before, we can send an unencapsulated H.264 stream over the network. To use a Raspberry Pi as a server:

rpicam-vid -t 0 -n --inline --listen -o tcp://0.0.0.0:<port>

To view video streamed over TCP using a Raspberry Pi as a client, assuming the server is running at 30 frames per second, use the following command:

ffplay tcp://<ip-addr-of-server>:<port> -vf "setpts=N/30" -fflags nobuffer -flags low_delay -framedrop
