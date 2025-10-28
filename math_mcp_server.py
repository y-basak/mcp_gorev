
from mcp.server.fastmcp import FastMCP

# FastMCP server instance oluştur
mcp = FastMCP("math-server")


@mcp.resource("resource://addition")
def addition() -> str:

    result = 10 + 27
    return f"Addition result: 10 + 27 = {result}"


@mcp.resource("resource://multiplication")
def multiplication() -> str:
    
    result = 8 * 12
    return f"Multiplication result: 8 * 12 = {result}"


if __name__ == "__main__":
    # stdio transport ile server'ı başlat
    mcp.run(transport="stdio")
 