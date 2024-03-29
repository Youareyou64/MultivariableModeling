import serial
import time

serial_path = 'COM4'
serial_list = ["COM1", "COM2", "COM3", "COM4", "COM5"]
baud_rate = 115200

global globalresponse
globalresponse = ""


class Connection:
    def __init__(self):
        try:
            self.ser = serial.Serial(serial_path, baud_rate, timeout=1)
            print("Connected")
        except Exception as e:

            print(f"Error encountered during connection: {e}")
            
    def send(self, data):
        formatted = data + "\n"

        if(data=="G28 X Y"):
            homing_complete = False
            time.sleep(1)
            self.ser.write(formatted.encode())
            print(f"Sent command {data}")
            time.sleep(1)
            while(homing_complete == False):
                response = self.ser.read(64)
                # print(f"Response: {response.decode()}")
                time.sleep(1)
                if("busy" not in response.decode() and "processing" not in response.decode()):
                    homing_complete = True
                    print("Homing complete")
                else:
                    print("Homing ongoing")

        else:
            try:
                move_complete = False
                # time.sleep(1)
                self.ser.write(formatted.encode())
                print(f"Sent command {data}")
                time.sleep(0.5)
                while(move_complete==False):

                    response = self.ser.read(64)
                    # print(f"Response: {response.decode()}")
                    time.sleep(0.6)
                    global globalresponse
                    globalresponse = response.decode()
                    if ("busy" not in response.decode() and "processing" not in response.decode()):
                        move_complete = True
                        print(f"move complete {data}")
                    else:
                        pass
                        # print("move ongoing")

            except Exception as e:
                print(f"Error : {e}")
                print(f"Error encountered during GCode send: {data}")

    def get_state(self):
        return globalresponse



    

