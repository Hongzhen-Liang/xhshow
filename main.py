import asyncio
from xhs.request.AsyncRequestFramework import AsyncRequestFramework
from xhs.request.note import Notes

note = Notes(AsyncRequestFramework())
response = asyncio.run(note.search_notes(keyword="番禺发生什么了",search_id="2e4y7th83yq4ok8atm3a5",page=1))
print(response)

