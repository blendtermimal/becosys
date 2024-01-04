import asyncio
import websockets

async def handle_connection(websocket, path):
  
    print(f"New connection established: {websocket.remote_address}")

    try:
        while True:
           
            message = await websocket.recv()
            print(f"Received message from {websocket.remote_address}: {message}")

            # Process the message (Will differ based on data received and sent)

            response = f"Received your message: {message}"
            await websocket.send(response)

    except websockets.exceptions.ConnectionClosedError:
        print(f"Connection closed by {websocket.remote_address}")

async def main():
    
    server = await websockets.serve(handle_connection, "localhost", 8765)

    print("Blendpoint Core WebSocket server started. Listening on ws://localhost:8765")

    
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())


