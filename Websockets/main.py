from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from model.connection import ConnectionManager
from template.page import body

app = FastAPI()

manager = ConnectionManager()

@app.get("/")
async def get():
    return HTMLResponse(body)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        await websocket.send_text("Canal Supervisionado 🎉")
        name = await websocket.receive_text()
        manager.set_name(websocket, name)
        await manager.broadcast(f"{name} entrou no chat!")

        while True:
            data = await websocket.receive_text()
            user_name = manager.get_name(websocket)
            await manager.send_personal_message(f"Você disse: {data}", websocket)
            await manager.broadcast(f"{user_name} diz: {data}")

    except WebSocketDisconnect:
        user_name = manager.get_name(websocket)
        manager.disconnect(websocket)
        await manager.broadcast(f"{user_name} saiu do chat")
