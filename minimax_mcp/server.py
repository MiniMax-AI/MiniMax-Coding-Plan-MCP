"""
MiniMax Coding Plan MCP Server

⚠️ IMPORTANT: This server connects to Minimax API endpoints which may involve costs.
Any tool that makes an API call is clearly marked with a cost warning. Please follow these guidelines:

1. Only use these tools when users specifically ask for them
2. For audio generation tools, be mindful that text length affects the cost
3. Voice cloning features are charged upon first use after cloning

Note: Tools without cost warnings are free to use as they only read existing data.
"""

import os
import json
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent
from minimax_mcp.utils import (
    process_image_url,
)

from minimax_mcp.const import *
from minimax_mcp.exceptions import MinimaxAPIError, MinimaxRequestError
from minimax_mcp.client import MinimaxAPIClient

load_dotenv()
api_key = os.getenv(ENV_MINIMAX_API_KEY)
api_host = os.getenv(ENV_MINIMAX_API_HOST)
fastmcp_log_level = os.getenv(ENV_FASTMCP_LOG_LEVEL) or "WARNING"

if not api_key:
    raise ValueError("MINIMAX_API_KEY environment variable is required")
if not api_host:
    raise ValueError("MINIMAX_API_HOST environment variable is required")

mcp = FastMCP("Minimax",log_level=fastmcp_log_level)
api_client = MinimaxAPIClient(api_key, api_host)

@mcp.tool(
    description="""
    
    Web Search API, works like Google Search.
    
    Args:
        query (str): The search query string. Use 3-5 keywords. Add the current date for time-sensitive queries, e.g. `latest iPhone 2025`
        
    Search Strategy:
        - If no valid results found, try changing search keywords
        
    Returns:
        Text content with search results in JSON format. The response structure is:
        {
            "organic": [
                {
                    "title": "string - The title of the search result",
                    "link": "string - The URL link to the result",
                    "snippet": "string - A brief description or excerpt",
                    "date": "string - The date of the result"
                }
            ],
            "related_searches": [
                {
                    "query": "string - A related search query suggestion"
                }
            ],
            "base_resp": {
                "status_code": "int - Response status code",
                "status_msg": "string - Response status message"
            }
        }
    """
)
def web_search(
    query: str,
) -> TextContent:
    try:
        if not query:
            raise MinimaxRequestError("Query is required")
        
        # Build request payload
        payload = {
            "q": query
        }
        
        # Call search API
        response_data = api_client.post("/v1/coding_plan/search", json=payload)
        
        # Return JSON dump of response data
        return TextContent(
            type="text",
            text=json.dumps(response_data, ensure_ascii=False, indent=2)
        )
        
    except MinimaxAPIError as e:
        return TextContent(
            type="text",
            text=f"Failed to perform search: {str(e)}"
        )


@mcp.tool(
    description="""
    
    A powerful LLM that can analyze and understand image content from files or URLs, follow your instruction.
    Use this tool to understand images by LLM.
    Only support jpeg, png, webp formats. Other formats like pdf/gif/psd/svg and so on are not supported.

    Args:
        prompt (str): The text prompt describing what you want to analyze or extract from the image.
        image_source (str): The source location of the image to analyze.
            Accepts:
            - HTTP/HTTPS URL: "https://example.com/image.jpg"
            - Local file path:
                - Relative path: "images/photo.png"
                - Absolute path: "/Users/username/Documents/image.jpg"
            IMPORTANT: If the file path starts with @ symbol, you MUST remove the @ prefix before passing to this function.
            For example:
                - If you see "@Documents/photo.jpg", use "Documents/photo.jpg"
                - If you see "@/Users/username/image.png", use "/Users/username/image.png"
            Supported formats: JPEG, PNG, WebP
        
    Returns:
        Text content with the image analysis result.
    """
)
def understand_image(
    prompt: str,
    image_source: str,
) -> TextContent:
    try:
        if not prompt:
            raise MinimaxRequestError("Prompt is required")
        if not image_source:
            raise MinimaxRequestError("Image source is required")
        
        # Process image_source: convert HTTP URL or local file to base64, or pass through existing base64
        processed_image_url = process_image_url(image_source)
        
        # Build request payload
        payload = {
            "prompt": prompt,
            "image_url": processed_image_url
        }
        
        # Call VLM API
        response_data = api_client.post("/v1/coding_plan/vlm", json=payload)
        
        # Extract content from response
        content = response_data.get("content", "")
        
        if not content:
            raise MinimaxRequestError("No content returned from VLM API")
        
        # Return the content
        return TextContent(
            type="text",
            text=content
        )
        
    except MinimaxAPIError as e:
        return TextContent(
            type="text",
            text=f"Failed to perform VLM analysis: {str(e)}"
        )


def main():
    print("Starting Minimax MCP server")
    """Run the Minimax MCP server"""
    mcp.run()


if __name__ == "__main__":
    main()
