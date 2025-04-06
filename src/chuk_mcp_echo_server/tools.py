# chuk_mcp_echo_server/tools.py
from pydantic import ValidationError
from mcp.shared.exceptions import McpError  # Adjust if needed for your project

# Import the runtime's tool decorator
from chuk_mcp_runtime.common.mcp_tool_decorator import mcp_tool

# Project imports – using absolute imports to reference the echo server models
from chuk_mcp_echo_server.models import EchoInput, EchoResult

@mcp_tool(name="echo", description="Echo back the input message")
def echo(message: str) -> dict:
    """
    Validate input using EchoInput and return an echo response as defined by EchoResult.
    """
    try:
        validated_input = EchoInput(message=message)
    except ValidationError as e:
        raise ValueError(f"Invalid input for echo: {e}")

    # Build the result by simply echoing the message back.
    result = EchoResult(message=validated_input.message)
    return result.model_dump()

