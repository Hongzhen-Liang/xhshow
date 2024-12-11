import asyncio
from xhs.request.AsyncRequestFramework import AsyncRequestFramework
from xhs.request.note import Notes
from xhs.request.feeds import Feeds,FeedType

arf = AsyncRequestFramework()
note = Notes(arf)
response = asyncio.run(note.search_notes(keyword="马岭花都植物园",search_id="2e4y7th83yq4ok8atm3a5",page=1))
print(response)

# feed = Feeds(arf)
# response = asyncio.run(feed.get_feed_content(feed_type=FeedType.RECOMMEND,num=1,page=1))
# print(response)