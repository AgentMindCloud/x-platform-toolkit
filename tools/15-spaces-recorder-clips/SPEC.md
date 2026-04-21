# SPEC · 15 Spaces Recorder + Clips

## Tagline

Spaces shouldn't disappear. Record, transcribe, clip — automated.

## Why it exists

X Spaces generate some of the highest-signal conversation on the platform, but the format is hostile to reuse. Recordings are time-limited, search is nonexistent, and manually clipping a good moment requires scrubbing hours of audio. Most creators leave that content value on the floor.

This tool treats every Space as a raw asset pipeline. Audio in, captioned video clips out, with transcripts and chapter markers as side products. A single 90-minute Space can yield a dozen clips, a full transcript blog post, and a week of quote-tweet fodder.

## User journey

1. User pastes a Space URL (live or recently-ended, within the recording retention window).
2. Tool downloads the full audio using Twspace-dl or yt-dlp.
3. Whisper transcribes with speaker diarization (pyannote) and produces an SRT with timestamps.
4. Energy-detection worker scans the audio for volume spikes, laughter, applause, and host-signaled moments ("great question", "that's huge"), producing a ranked list of candidate clip windows.
5. For the top N moments, FFmpeg cuts 60-second segments, renders a waveform-plus-caption video (vertical 1080x1920), and burns in subtitles from the SRT.
6. User reviews clips in a web UI, trims start/end if needed, and downloads MP4s or posts directly to X via API.

## Data sources

- Space audio stream (m3u8) via yt-dlp or Twspace-dl
- Whisper (local `whisper.cpp` large-v3, OpenAI API as fallback for low-resource deployments)
- pyannote.audio for speaker diarization
- librosa for volume-spike and applause detection
- X API v2 `POST /2/tweets` with video media upload for direct publishing

## Tech stack

- Node.js orchestration service with BullMQ job queue, hosted on Render
- Python worker container for Whisper + librosa (GPU-optional)
- FFmpeg for all audio/video transforms
- Cloudflare R2 for artifact storage (audio, clips, transcripts)
- React frontend with a clip-review timeline UI

## Estimated build

20–30 hours.

## Open questions / risks

- Most complex tool in the toolkit; ship v0 as a manual flow (paste URL, get transcript and ranked moments, user clips manually) and add auto-clipping in v1.
- Whisper large-v3 on CPU takes roughly real-time per minute of audio; long Spaces require chunked parallel transcription or a GPU worker.
- Twspace-dl and yt-dlp break when X changes endpoints; pin versions and monitor for upstream fixes.
- Diarization quality degrades with overlapping speakers and crowded stages.
- Storage costs grow quickly; enforce a 30-day artifact retention policy with a "keep" pin for user favorites.
- Posting clips directly requires X API video upload, which has a 512MB and 140s cap — clip length must stay under both.
