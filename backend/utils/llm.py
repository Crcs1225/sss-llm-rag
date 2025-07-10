import os
import requests
from typing import Dict, List, Optional, Tuple

class LightweightLLM:
    def __init__(self, hf_token: Optional[str] = None):
        self.model = None
        self.model_id = None
        self.hf_token = hf_token or os.getenv("HF_TOKEN")
        self.current_api_url = None
        
        # API endpoints for different providers
        self.api_endpoints = {
            "fireworks": "https://router.huggingface.co/fireworks-ai/inference/v1/chat/completions",
            "novita": "https://router.huggingface.co/novita/v3/openai/chat/completions"
        }
        
        # Map model IDs to (provider, model_name) tuples
        self.model_mapping = {
            "deepseek": ("fireworks", "accounts/fireworks/models/deepseek-r1"),
            "llama": ("fireworks", "accounts/fireworks/models/llama-v3p1-8b-instruct"),
            "mistral": ("novita", "mistralai/mistral-7b-instruct")
        }

    def load_model(self, model_id="mistral"):
        """Load a model configuration for API usage"""
        try:
            if model_id not in self.model_mapping:
                model_id = "mistral"  # Default fallback
            
            provider, model_name = self.model_mapping[model_id]
            self.model_id = model_id
            self.model = model_name
            self.current_api_url = self.api_endpoints[provider]
            
            print(f"✓ Model {model_id} ({model_name}) configured for API usage via {provider}")
            return True
            
        except Exception as e:
            print(f"Error configuring model: {e}")
            return False

    def _api_request(self, messages: List[Dict[str, str]], temperature: float = 0.7, 
                     max_tokens: int = 256) -> Optional[str]:
        """Make API request to HuggingFace Router API"""
        if not self.model or not self.current_api_url:
            raise ValueError("Model is not configured.")
        
        if not self.hf_token:
            raise ValueError("HF_TOKEN is required for this API.")
        
        headers = {
            "Authorization": f"Bearer {self.hf_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messages": messages,
            "model": self.model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False
        }
        
        try:
            response = requests.post(
                self.current_api_url,
                headers=headers,
                json=payload,
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    return result["choices"][0]["message"]["content"]
            else:
                print(f"API Error: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"Request error: {e}")
            return None

    def generate(self, prompt: str, temperature: float = 0.7, max_tokens: int = 256) -> str:
        """Generate text using the API"""
        if not self.model:
            raise ValueError("Model is not configured.")
        
        # Create messages format
        system_msg = "You are a helpful SSS (Social Security System) assistant. Answer based on the context provided if available. If the context doesn't contain the answer, say so. Do not include reference citations or links in your response."
        
        messages = [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
        
        response = self._api_request(
            messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        if response:
            # Clean up response
            response = response.strip()
            
            # Remove <think> tags and their content (common in DeepSeek)
            import re
            # Handle both single-line and multi-line think tags
            response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL).strip()
            # Also handle unclosed <think> tags at the start
            response = re.sub(r'^<think>.*', '', response, flags=re.DOTALL).strip()
            
            # Remove reference sections
            reference_markers = [
                "\n\nReference(s):",
                "\nReference(s):",
                "\n\nReferences:",
                "\nReferences:",
                "\n\nSource(s):",
                "\nSource(s):",
                "\n\n[",  # Markdown links that start references
            ]
            
            for marker in reference_markers:
                if marker in response:
                    response = response.split(marker)[0].strip()
            
            # Also remove any trailing incomplete sentences that might be cut off
            if response.endswith("SSS%") or response.endswith(".pdf)"):
                # Find the last complete sentence
                sentences = response.split(". ")
                if len(sentences) > 1:
                    response = ". ".join(sentences[:-1]) + "."
            
            # Final cleanup - ensure no empty response
            if not response or response == "":
                return "I apologize, but I couldn't generate a proper response. Please try again."
            
            return response
        else:
            return "Error generating response. Please try again."

    def get_available_models(self) -> List[Dict[str, str]]:
        """List available models for API usage"""
        models = []
        for model_id, (provider, model_name) in self.model_mapping.items():
            models.append({
                "id": model_id,
                "provider": provider,
                "model": model_name,
                "status": "available"
            })
        return models