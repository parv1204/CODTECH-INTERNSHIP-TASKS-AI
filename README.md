# Task 2: Speech Recognition Tool

## Objective
Transcribe WAV audio files into text using a speech recognition model.

## Deliverables
- `Task2_AI.py`: Script for transcribing audio with Wav2Vec2.
- `transcription.txt`: Contains transcription results.
- `harvard.wav` (optional): Sample WAV (5-10s, 16 kHz, mono).

## How to Run
1. Install: `pip install -r ../requirements.txt`
2. Place `Task2_AI.py` in `Task2/`.
3. Add WAV file to `Task2/`.
4. Run: `python Task2_AI.py`
5. Check `transcription.txt`.

## Notes
- Uses Wav2Vec2 (`facebook/wav2vec2-base-960h`).
- WAV: 16 kHz, 16-bit, mono.
- Requires `transformers`, `torch`, `librosa`.
