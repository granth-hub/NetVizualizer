from flask import Flask, render_template
from flask_socketio import SocketIO
from scapy.all import sniff, IP
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# This function runs every time a packet is caught
def packet_callback(packet):
    if IP in packet:
        data = {
            'src': packet[IP].src,
            'dst': packet[IP].dst,
            'len': len(packet)
        }
        # Send the data to the web dashboard
        socketio.emit('new_packet', data)

# This function runs the scanner in the background
def start_sniffing():
    sniff(iface="eth0", prn=packet_callback, store=0)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Start the packet sniffer in a background thread
    thread = threading.Thread(target=start_sniffing)
    thread.daemon = True
    thread.start()
    
    print("\n🚀 Server starting! Open http://127.0.0.1:5000 in your browser\n")
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
