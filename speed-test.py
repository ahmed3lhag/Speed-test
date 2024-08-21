from speedtest import Speedtest

wifi = Speedtest()

print("Getting Download speed...")
download = wifi.download()
print(f"Your download speed is: {download / 1024 / 1024:.2f} MB/s")

print("Getting Upload speed...")
upload = wifi.upload()
print(f"Your upload speed is: {upload / 1024 / 1024:.2f} MB/s")
