
import asyncio
import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


# ==================== GREETING SERVER TESTS ====================

@pytest.mark.asyncio
async def test_greeting_server_connection():
    """Test 1: Greeting server connects successfully"""
    server_params = StdioServerParameters(
        command="python",
        args=["greeting_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            assert session is not None
            print("✓ Greeting Server connection successful")


@pytest.mark.asyncio
async def test_greet_resource():
    """Test 2: Greet resource returns correct message"""
    server_params = StdioServerParameters(
        command="python",
        args=["greeting_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            response = await session.read_resource("resource://greet")
            content = response.contents[0].text
            
            assert "Hello" in content
            assert "Greeting Server" in content
            print(f"✓ Greet resource test passed: {content}")


@pytest.mark.asyncio
async def test_farewell_resource():
    """Test 3: Farewell resource returns correct message"""
    server_params = StdioServerParameters(
        command="python",
        args=["greeting_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            response = await session.read_resource("resource://farewell")
            content = response.contents[0].text
            
            assert "Goodbye" in content
            assert "Greeting Server" in content
            print(f"✓ Farewell resource test passed: {content}")


@pytest.mark.asyncio
async def test_greeting_server_invalid_resource():
    """Test 4: Greeting server handles invalid resource correctly"""
    server_params = StdioServerParameters(
        command="python",
        args=["greeting_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            with pytest.raises(Exception):
                await session.read_resource("resource://invalid")
            print("✓ Invalid resource correctly raises exception")


# ==================== MATH SERVER TESTS ====================

@pytest.mark.asyncio
async def test_math_server_connection():
    """Test 5: Math server connects successfully"""
    server_params = StdioServerParameters(
        command="python",
        args=["math_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            assert session is not None
            print("✓ Math Server connection successful")


@pytest.mark.asyncio
async def test_addition_resource():
    """Test 6: Addition resource returns correct result"""
    server_params = StdioServerParameters(
        command="python",
        args=["math_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            response = await session.read_resource("resource://addition")
            content = response.contents[0].text
            
            assert "Addition result" in content
            assert "42" in content  # 15 + 27 = 42
            print(f"✓ Addition resource test passed: {content}")


@pytest.mark.asyncio
async def test_multiplication_resource():
    """Test 7: Multiplication resource returns correct result"""
    server_params = StdioServerParameters(
        command="python",
        args=["math_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            response = await session.read_resource("resource://multiplication")
            content = response.contents[0].text
            
            assert "Multiplication result" in content
            assert "96" in content  # 8 * 12 = 96
            print(f"✓ Multiplication resource test passed: {content}")


@pytest.mark.asyncio
async def test_math_server_invalid_resource():
    """Test 8: Math server handles invalid resource correctly"""
    server_params = StdioServerParameters(
        command="python",
        args=["math_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            with pytest.raises(Exception):
                await session.read_resource("resource://division")
            print("✓ Invalid resource correctly raises exception")


@pytest.mark.asyncio
async def test_math_both_resources():
    """Test 9: Both math resources work together"""
    server_params = StdioServerParameters(
        command="python",
        args=["math_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            add_response = await session.read_resource("resource://addition")
            mult_response = await session.read_resource("resource://multiplication")
            
            assert "42" in add_response.contents[0].text
            assert "96" in mult_response.contents[0].text
            print("✓ Both math resources work correctly together")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
