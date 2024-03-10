#!/usr/bin/python3
import asyncio
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import time
import json

from config import ADMIN_ID
from database import db
from loader import bot
from server import server
from aiogram import executor
from handlers import dp


async def on_startup(_):
    print("GO GO GO")
    await db.create_db()
    await bot.send_message(ADMIN_ID, "I'm Work!")


async def on_shutdown(dp):
    await bot.close()
    await bot.send_message(ADMIN_ID, "I'm Down!")


async def start_polling():
    executor.start_polling(
        dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown
    )


async def main():
    await asyncio.gather(
        start_polling(),
        start_http_server(),
    )


async def start_http_server():
    hostName = "0.0.0.0"
    serverPort = 8080

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                content = open('/app/index.html', 'rb').read()
                self.wfile.write(content)
            else:
                self.send_response(400)
            return

    class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
        """Handle requests in a separate thread."""

    webServer = ThreadedHTTPServer((hostName, serverPort), Handler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    print("It is Work!")
    asyncio.run(main())
