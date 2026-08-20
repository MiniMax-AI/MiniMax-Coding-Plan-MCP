import asyncio
import os
import sys

from mcp import Client
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client
from mcp.server import MCPServer


EXPECTED_TOOLS = {"understand_image", "web_search"}
TEST_ENV = {
    "MINIMAX_API_KEY": "test-api-key",
    "MINIMAX_API_HOST": "https://example.invalid",
}


def _server_module():
    os.environ.update(TEST_ENV)
    from minimax_mcp import server

    return server


def test_server_uses_mcp_v2_public_api():
    server = _server_module()

    assert isinstance(server.mcp, MCPServer)


def test_modern_client_lists_expected_tools_without_api_calls():
    async def run_test():
        server = _server_module()

        async with Client(server.mcp) as client:
            result = await client.list_tools()

        assert {tool.name for tool in result.tools} == EXPECTED_TOOLS

    asyncio.run(run_test())


def test_stdio_initialize_and_tools_list_without_api_calls():
    async def run_test():
        parameters = StdioServerParameters(
            command=sys.executable,
            args=["-m", "minimax_mcp.server"],
            env=TEST_ENV,
        )

        async with stdio_client(parameters) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                result = await session.list_tools()

        assert {tool.name for tool in result.tools} == EXPECTED_TOOLS

    asyncio.run(run_test())


def test_registered_tools_use_mocked_api(monkeypatch):
    server = _server_module()
    requests = []

    def fake_post(endpoint, **kwargs):
        requests.append((endpoint, kwargs["json"]))
        if endpoint == "/v1/coding_plan/search":
            return {"organic": [{"title": "Mock result"}]}
        return {"content": "Mock image analysis"}

    monkeypatch.setattr(server.api_client, "post", fake_post)
    monkeypatch.setattr(
        server,
        "process_image_url",
        lambda image_source: f"mocked:{image_source}",
    )

    async def run_test():
        async with Client(server.mcp) as client:
            search_result = await client.call_tool("web_search", {"query": "mcp v2"})
            image_result = await client.call_tool(
                "understand_image",
                {"prompt": "describe", "image_source": "image.png"},
            )

        assert search_result.is_error is False
        assert "Mock result" in search_result.content[0].text
        assert image_result.is_error is False
        assert image_result.content[0].text == "Mock image analysis"

    asyncio.run(run_test())

    assert requests == [
        ("/v1/coding_plan/search", {"q": "mcp v2"}),
        (
            "/v1/coding_plan/vlm",
            {"prompt": "describe", "image_url": "mocked:image.png"},
        ),
    ]
