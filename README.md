# Transformers-with-RaspberryPi

This repository showcases the implementation of various natural language processing (NLP) tasks using Hugging Face's Transformers library on a Raspberry Pi 4. Specifically, it includes code examples for text generation utilizing the Phi-3 Mini-128K-Instruct model and other efficient models suitable for the computational constraints of a Raspberry Pi 4.

## Overview

The Hugging Face Transformers library provides an easy-to-use interface for a wide range of NLP tasks, including text generation, sentiment analysis, translation, and more. By using pre-trained models, you can quickly set up pipelines and perform complex NLP tasks with minimal effort. This repository demonstrates how to integrate and utilize these models on a Raspberry Pi 4.

### Models Used

- **Phi-3 Mini-128K-Instruct**: Integrated into the development version (4.41.0.dev0) of Transformers, this model is used for instruct-based tasks.
- **DistilGPT-2**: A smaller, efficient version of GPT-2 suitable for text generation on devices with limited resources like the Raspberry Pi 4.
- **msmarco-distilbert-base-tas-b**: A model from Sentence Transformers, designed for tasks requiring sentence embeddings and similarity computations.

## Requirements

To run the provided examples, ensure you have the following installed on your Raspberry Pi 4:

- Python 3
- pip (Python package installer)
- torch (PyTorch)
- transformers (Hugging Face Transformers library)
- sentence-transformers (Sentence Transformers library)

You can install the necessary libraries using the following commands:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install torch transformers sentence-transformers
```


## Code Examples
#### 1. Text Generation Pipeline (text_generation.py)
This example demonstrates how to set up and use a text generation pipeline with a pre-trained model.

#### 2. Text Embedding and Similarity (text_embedding_similarity.py)
This example shows how to encode texts into embeddings and compute similarity scores.

####  3. Sentence Embedding and Similarity using Sentence Transformers (sentence_transformers_similarity.py)
This example demonstrates how to use the sentence-transformers library to encode sentences and compute similarity scores.



## Usage
1. Clone the repository to your Raspberry Pi:
     
```bash
git clone https://gitlab.com/inoshas/transformers-with-raspberrypi.git
cd transformers-with-raspberrypi
```

2. Ensure all dependencies are installed:
```bash
pip3 install torch transformers sentence-transformers
```

3. Run the provided Python scripts to see the NLP tasks in action:
```bash
python3 text_generation.py
python3 text_embedding_similarity.py
python3 sentence_transformers_similarity.py
```

## Notes
- Due to the limited computational resources of the Raspberry Pi 4, consider using smaller models or applying optimizations such as quantization.
- The Phi-3 Mini-128K-Instruct model might require additional setup and configurations.

## Acknowledgments
- Hugging Face for the Transformers library
- The open-source community for contributing models and tools
