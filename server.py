import asyncio
import websockets

# Lista para armazenar as conexões WebSocket ativas
connected_clients = []


async def handler(websocket, path):
    # Adiciona o novo cliente à lista de conexões
    connected_clients.append(websocket)
    try:
        # Continuamente escuta as mensagens recebidas dos clientes
        async for message in websocket:
            # Reenvia a mensagem para todos os outros clientes conectados
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        # Remove o cliente da lista quando ele desconectar
        connected_clients.remove(websocket)


# Inicia o servidor WebSocket na porta 8080
start_server = websockets.serve(handler, "localhost", 8080)

# Loop de eventos para manter o servidor rodando
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
