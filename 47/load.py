
import googleapiclient.discovery
import googleapiclient.errors
import io

api_service_name="youtube"
api_version="v3"
DEVELOPER_KEY="AIzaSyD1SXEou8XbVaOe04BmMtxN8yQc0Crfkhw"

youtube=googleapiclient.discovery.build(api_service_name,api_version,developerKey=DEVELOPER_KEY)
request=youtube.commentThreads().list(
    part="snippet",
    videoId="H_dPOuhbB1k",
    textFormat="plainText"
)
response=request.execute()
comment=[]
while response:
    for item in response["items"]:
            comment.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"])
    if "nextPageToken" in response:
        response=youtube.commentThreads().list(
        part="snippet",
        videoId="nj8J6K3NnwQ",
        textFormat="plainText",
        pageToken=response["nextPageToken"]
        ).execute()
    else:
        break


with io.open("comment.txt","a",encoding="utf-8") as f1:
    for data in comment:
        f1.write(data+"\n")
f1.close()

        







