import asyncio
import logging
import json
from mediaflow_proxy.extractors.dlhd import DLHDExtractor

# Setting log agar kita bisa melihat prosesnya di GitHub Actions
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    # 1. Header simulasi agar tidak dianggap bot
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # 2. Inisialisasi Extractor
    extractor = DLHDExtractor(request_headers=headers)

    # 3. URL yang ingin kamu ambil (Contoh URL DaddyLive)
    # Pastikan ID ini valid dan sedang live
    target_url = "https://dlhd.dad/watch.php?id=2" 

    try:
        logger.info(f"Mencoba mengekstrak: {target_url}")
        
        # 4. Proses Ekstraksi
        result = await extractor.extract(target_url)

        # 5. Output hasil ke console
        print("\n--- HASIL EKSTRAKSI ---")
        print(f"URL Stream: {result['destination_url']}")
        print(f"Endpoint: {result['mediaflow_endpoint']}")
        
        # 6. Simpan ke file agar bisa diambil dari GitHub
        with open("playlist.m3u8", "w") as f:
            f.write("#EXTM3U\n")
            f.write(f"#EXTINF:-1, Daddylive Stream\n")
            f.write(f"{result['destination_url']}\n")
            
        logger.info("Berhasil! File playlist.m3u8 telah dibuat.")

    except Exception as e:
        logger.error(f"Gagal menjalankan main: {e}")

if __name__ == "__main__":
    asyncio.run(main())
