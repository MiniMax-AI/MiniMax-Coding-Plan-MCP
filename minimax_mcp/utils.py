import os
import base64
import requests
from minimax_mcp.const import *
from minimax_mcp.exceptions import MinimaxMcpError, MinimaxRequestError



def process_image_url(image_url: str) -> str:
    """
    Process image URL and convert to base64 data URL format.
    
    This function handles three types of image inputs:
    1. HTTP/HTTPS URLs: Downloads the image and converts to base64
    2. Base64 data URLs: Passes through as-is
    3. Local file paths: Reads the file and converts to base64
    
    Args:
        image_url (str): The image URL, data URL, or local file path
        
    Returns:
        str: Base64 data URL in format "data:image/{format};base64,{data}"
        
    Raises:
        MinimaxRequestError: If image cannot be downloaded, read, or processed
    """
    # If already in base64 data URL format, pass through
    if image_url.startswith("data:"):
        return image_url
    
    # Handle HTTP/HTTPS URLs
    if image_url.startswith(("http://", "https://")):
        try:
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image_data = image_response.content
            
            # Detect image format from content-type header
            content_type = image_response.headers.get('content-type', '').lower()
            if 'jpeg' in content_type or 'jpg' in content_type:
                image_format = 'jpeg'
            elif 'png' in content_type:
                image_format = 'png'
            elif 'gif' in content_type:
                image_format = 'gif'
            elif 'webp' in content_type:
                image_format = 'webp'
            else:
                # Default to jpeg if cannot detect
                image_format = 'jpeg'
            
            # Convert to base64 data URL
            base64_data = base64.b64encode(image_data).decode('utf-8')
            return f"data:image/{image_format};base64,{base64_data}"
            
        except requests.RequestException as e:
            raise MinimaxRequestError(f"Failed to download image from URL: {str(e)}")
    
    # Handle local file paths
    else:
        if not os.path.exists(image_url):
            raise MinimaxRequestError(f"Local image file does not exist: {image_url}")
        
        try:
            with open(image_url, "rb") as f:
                image_data = f.read()
                
                # Detect image format from file extension
                image_format = 'jpeg'  # Default
                if image_url.lower().endswith('.png'):
                    image_format = 'png'
                elif image_url.lower().endswith('.gif'):
                    image_format = 'gif'
                elif image_url.lower().endswith('.webp'):
                    image_format = 'webp'
                elif image_url.lower().endswith(('.jpg', '.jpeg')):
                    image_format = 'jpeg'
                
                base64_data = base64.b64encode(image_data).decode('utf-8')
                return f"data:image/{image_format};base64,{base64_data}"
                
        except IOError as e:
            raise MinimaxRequestError(f"Failed to read local image file: {str(e)}")


