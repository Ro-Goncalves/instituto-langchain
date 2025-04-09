from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Calculadora", settings={"debug": True, "log_level": "DEBUG"})

@mcp.tool(
    name="add",
    description="Add two numbers",
)
def add(x: float, y: float) -> float:
    return x + y

@mcp.tool(
    name="multiply",
    description="Multiply two numbers",
)
def multiply(x: float, y: float) -> float:
    return x * y

if __name__ == "__main__":
    mcp.run(transport='stdio')