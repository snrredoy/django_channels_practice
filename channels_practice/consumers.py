from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class ConsumerSync(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Sync connected....", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Websocket Sync Received...", event)
        self.send({
            'type': 'websocket.send',
            'text': 'Message from client'
        })
    
    def websocket_disconnect(self, event):
        print("Websocket Sync Disconnect...", event)
        raise StopConsumer()
    
class ConsumerAsync(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket Async connect...', event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('Websocket Async receive...', event)
        await self.send({
            'type': 'websocket.send',
            'text': 'Message from client'
        })

    async def websocket_disconnect(self, event):
        print('Websocket Async disconnect...', event)
        raise StopConsumer()