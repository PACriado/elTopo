from googleapiclient.discovery import build

class googleSearch:

    def search(self,query):
        service = build("customsearch", "v1",
            developerKey="AIzaSyDRRpR3GS1F1_jKNNM9HCNd2wJQyPG3oN0")

        res = service.cse().list(
            q=query,
            cx='017576662512468239146:omuauf_lfve',
          ).execute()
        print(res)
