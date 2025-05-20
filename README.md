"# Final_Year_Project" 
## video link : https://drive.google.com/file/d/1ETmjBL_kSQj64sz1GNvN5-XFBnZlVYH3/view?usp=drive_link
# 🧠 Image Caption Generator and Tutor for Visually Impaired Persons

An assistive AI-based mobile application that generates descriptive image captions and provides auditory feedback to visually impaired users — empowering them to perceive and interact with visual content more independently.

---

## 📸 Project Overview

This project, **"Image Caption Generator and Tutor for Visually Impaired Persons,"** integrates cutting-edge **computer vision** and **natural language processing** technologies to assist visually impaired individuals by interpreting images and providing real-time audio descriptions.

The system combines:
- 🔍 **Vision Transformer (ViT)** for high-level visual feature extraction.
- 📝 **BLIP (Bootstrapping Language-Image Pretraining)** for generating human-like natural language captions.
- 🗣️ **Text-to-Speech (TTS)** to convert generated captions into audible speech.

The application was trained using the **Flickr8k dataset**, ensuring a diverse range of image contexts to enhance caption quality and generalization.

---

## 🧩 Tech Stack

### Frontend – Flutter
- Cross-platform mobile development (Android/iOS)
- Simple UI/UX for capturing or uploading images
- Integrates with backend via REST API
- Plays audio captions using text-to-speech

### Backend – Python (FastAPI or Flask)
- Pre-trained ViT + BLIP models
- Image preprocessing and inference pipeline
- RESTful API for caption generation
- TTS module using PyTTSx3 / gTTS

---

## 🚀 Features

- 📷 Upload or capture images from the camera
- 🧠 Generate contextual captions using vision-language models
- 🔊 Listen to audio descriptions via text-to-speech
- 🌐 Lightweight backend API deployable on local servers or cloud
- 🧪 Trained on **Flickr8k** for generalization across common objects and scenes


