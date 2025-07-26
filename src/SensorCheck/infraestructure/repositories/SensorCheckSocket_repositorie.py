import json
import asyncio
import websockets

class WebSocketClientRepository:
    def __init__(self, ws_url: str = "ws://localhost:8080/ws/vaccine-stats"):
        self.ws_url = ws_url

    async def listen_to_data(self):
        try:
            async with websockets.connect(self.ws_url) as websocket:
                print("Conectado al WebSocket del servidor Go")

                while True:
                    message = await websocket.recv()
                    data = json.loads(message)
                    print("Mensaje recibido del servidor:", json.dumps(data, indent=2))

        except Exception as e:
            print(f"Error al conectar o recibir del WebSocket: {e}")
