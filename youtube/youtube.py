from pytube import YouTube
import re
import sys

url = input("URL: ").strip()
if not url:
	print("No URL provided.")
	sys.exit(1)

try:
	yt = YouTube(url)
	title = yt.title
	print(f"\nVideo found: {title}\n")

	video_stream = yt.streams.get_highest_resolution()

	# Sanitize title for use as a filename on most filesystems
	safe_title = re.sub(r'[<>:\\\"/\\|?*]', '_', title)

	print("Downloading Video...")
	try:
		video_stream.download(filename=f"{safe_title}.mp4")
		print("Program Completed")
	except Exception as e:
		print("Download failed with pytube, will try yt_dlp fallback:", e)
		raise
except Exception:
	# fallback to yt_dlp for robustness
	try:
		import yt_dlp
	except Exception as ie:
		print("Fallback downloader not available (yt_dlp):", ie)
		sys.exit(1)

	# build safe title from URL if title unavailable
	try:
		safe_title
	except NameError:
		safe_title = re.sub(r'[^A-Za-z0-9 _-]', '_', url)

	ydl_opts = {
		'outtmpl': f"{safe_title}.%(ext)s",
		'format': 'bestvideo+bestaudio/best',
		'noplaylist': True,
	}
	print("Using yt_dlp fallback to download...")
	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		print("Program Completed (yt_dlp)")
	except Exception as e:
		err = str(e)
		print("yt_dlp download failed:", err)
		if 'ffmpeg' in err.lower() or 'merging' in err.lower():
			print("ffmpeg not found — retrying with single-file format 'best' (no merge)...")
			ydl_opts['format'] = 'best'
			try:
				with yt_dlp.YoutubeDL(ydl_opts) as ydl:
					ydl.download([url])
				print("Program Completed (yt_dlp, single-file)")
			except Exception as e2:
				print("yt_dlp single-file download failed:", e2)
				sys.exit(1)
		else:
			sys.exit(1)
