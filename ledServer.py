import asyncio
import websockets
import RPi.GPIO as GPIO

#Set up GPIO for LED control
GPIO.setmode(GPIO.BCM)
LEDPIN = 18
GPIO.setup(LEDPIN, GPIO.OUT)
pwm = GPIO.PWM(LEDPIN, 1000)  # 1 kHz frequency
pwm.start(0)  # Start with 0% brightness

connected_clients = set()

async def handle_client(websocket, path):
    connected_clients.add(websocket)
    try:
        # Send a welcome message to the client upon connection
        await websocket.send("Connected to the server!")

        async for message in websocket:
            try:
                # Convert the message to a float representing brightness
                brightness = float(message)
                print(f"Received brightness: {brightness:.2f}%")

                # Adjust the brightness of the LED using PWM
                pwm.ChangeDutyCycle(brightness)

                # Broadcast the brightness value to all connected clients
                tasks = [asyncio.create_task(client.send(f"{brightness:.2f}")) for client in connected_clients]
                await asyncio.gather(*tasks)

            except ValueError:
                print("Invalid brightness value received.")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, "0.0.0.0", 8765)
    print("Server started, waiting for communication...")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
