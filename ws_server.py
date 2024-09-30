import asyncio
import websockets
import json

# Dictionary to store connected clients: {client_id: websocket}
connected_clients = {}

# Handle incoming WebSocket connections
async def handle_connection(websocket, path):
    try:
        # Wait for the client to send its ID
        message = await websocket.recv()
        client_data = json.loads(message)
        client_id = client_data['client_id']
        
        # Register the client ID and websocket connection
        connected_clients[client_id] = websocket
        print(f"Client {client_id} connected")

        # Listen for messages from the client
        async for message in websocket:
            data = json.loads(message)
            target_client_id = data['target_id']
            progress_percentage = data['progress_percentage']

            # Check if the target client exists
            if target_client_id in connected_clients:
                target_websocket = connected_clients[target_client_id]
                # Send the message to the target client
                await target_websocket.send(json.dumps({
                    'from': client_id,
                    'progress_percentage': progress_percentage
                }))
            else:
                await websocket.send(json.dumps({
                    'error': f"Client with ID {target_client_id} not found."
                }))
    except websockets.ConnectionClosed:
        print(f"Client {client_id} disconnected")
        # Remove the disconnected client
        if client_id in connected_clients:
            del connected_clients[client_id]

# Start WebSocket server
async def start_server():
    print("Starting WebSocket server...")
    server = await websockets.serve(handle_connection, "localhost", 8765)
    await server.wait_closed()

# Run the server using asyncio.run to ensure proper event loop management
if __name__ == "__main__":
    asyncio.run(start_server())
