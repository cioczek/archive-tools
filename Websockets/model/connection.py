# model/connection.py
from typing import Dict
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket, dict] = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[websocket] = {"name": None}  

    def disconnect(self, websocket: WebSocket):
        self.active_connections.pop(websocket, None)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections.keys():
            await connection.send_text(message)

    def set_name(self, websocket: WebSocket, name: str):
        if websocket in self.active_connections:
            self.active_connections[websocket]["name"] = name

    def get_name(self, websocket: WebSocket) -> str:
        return self.active_connections.get(websocket, {}).get("name", "Desconhecido")
