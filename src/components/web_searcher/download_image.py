import os
import time

from icrawler.builtin import GoogleImageCrawler


class ImageDownloader:
    def __init__(self):
        self.home_dir = os.path.expanduser("~")
        self.documents_path = os.path.join(self.home_dir, "Documents")
        self.program_dir = os.path.join(self.documents_path, "Bocchizer")

    def create_folder(self, urls: dict[str, str], num_image: int = 6) -> tuple[bool, str]:
        if not os.path.exists(self.program_dir):
            os.mkdir(self.program_dir)

        result = True

        for ref, search_term in urls.items():
            ref_path = os.path.join(self.program_dir, ref)

            if not os.path.exists(ref_path):
                os.mkdir(ref_path)

            sucess = self.download_image(search_term, num_image, ref_path)

            if sucess:
                self.rename_images(ref_path, ref)
            else:
                result = False
                break

            time.sleep(1)

        return result, self.program_dir

    def download_image(self, search_term: str, num_image: int, ref_path: str) -> bool:
        attempts = 0;

        while attempts < 3:
            try:
                google_crawler = GoogleImageCrawler(
                    feeder_threads=1,
                    parser_threads=2,
                    downloader_threads=4,
                    storage={'root_dir': ref_path}
                )

                google_crawler.crawl(
                    keyword=search_term,
                    max_num=num_image,
                    filters={"size": "medium"}
                )

                return True
            except Exception as e:
                print(f"Error downloading images: {e}")
                attempts += 1
                time.sleep(1)

        return False


    def rename_images(self, path: str, ref: str) -> None:
        images = os.listdir(path)

        for i, image in enumerate(images, start=1):
            new_name = f"{ref}-{i}.jpg"
            os.rename(os.path.join(path, image), os.path.join(path, new_name))

if __name__ == "__main__":
    downloader = ImageDownloader()

    urls = {
        "725y7": "Dell 725y7",
        "UVC-G3-FLEX": "Ubiquiti UVC-G3-FLEX",
        "680BA000006": "SALICRU 680BA000006"
    }
    sucess, path = downloader.create_folder(urls)
    print(f"Download sucess: {sucess}, images saved to: {path}")