import asyncio
import websockets
import json
from django.http import HttpResponse

# WebSocket server address
WEBSOCKET_SERVER_URL = "ws://localhost:8765"

async def send_message_to_ws(target_id, progress_percentage, client_id):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Register the Django client with the server
        await websocket.send(json.dumps({'client_id': client_id}))
        
        # Send message to the target client
        print({
            'target_id': target_id,
            'progress_percentage': progress_percentage
        })
        await websocket.send(json.dumps({
            'target_id': target_id,
            'progress_percentage': progress_percentage,
        }))

# Django view function
def send_message_view(target_id, progress_percentage):
    client_id = 'client_django'
    asyncio.run(send_message_to_ws(target_id, progress_percentage, client_id))