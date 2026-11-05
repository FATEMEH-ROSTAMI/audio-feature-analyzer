# Audio Feature Analyzer 
A beginner-friendly Python project for analyzing digital audio signals and extracting basic audio features.

## About the Project
Audio Feature Analyzer is a learning project developed to explore digital audio processing using Python.

The first version focuses on loading an audio file, calculating basic audio properties, and visualizing its waveform.

## Current Features
- Loading audio files using Librosa
- Reading the audio sample rate
- Calculating the total number of audio samples
- Measuring audio duration
- Calculating Root Mean Square (RMS)
- Visualizing the audio waveform using Matplotlib

## Technologies Used
- Python
- Librosa
- NumPy
- SoundFile
- Matplotlib

## Project Structure
```text
audio_feature_analyzer/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation
Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/audio-feature-analyzer.git
```

Navigate to the project directory:

```bash
cd audio-feature-analyzer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run
Place an audio file in the project directory and update its filename in `main.py`.

Then run:

```bash
python main.py
```

## Future Improvements
- Short-time RMS analysis
- Silence detection
- Frequency analysis using FFT
- Spectrogram visualization
- More advanced audio feature extraction

## Project Status
Currently under development. New features and improvements will be added progressively.