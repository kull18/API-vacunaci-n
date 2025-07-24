import json
import asyncio
import websockets
from fastapi import HTTPException

class WebSocketClientRepository:
    def __init__(self, ws_url: str = "ws://localhost:8080/ws"):
        self.ws_url = ws_url

    async def send_sensor_data(self, data):
        try:
            async with websockets.connect(self.ws_url) as websocket:
                print("coneccted")
                await websocket.send(json.dumps(data))
                print(f" Mensaje enviado al WS: {data}")
        except Exception as e:
            print(f"Error al enviar al WebSocket: {e}")

