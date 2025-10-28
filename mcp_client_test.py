"""
MCP Client - Test client for both Greeting and Math servers
"""
import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def test_greeting_server():
    """Test Greeting Server and its resources"""
    print("\n" + "="*60)
    print("TESTING GREETING SERVER")
    print("="*60)
    
    server_params = StdioServerParameters(
        command="python",
        args=["greeting_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # 1. Connection test
            print("\n✓ Client is connected to Greeting MCP Server")
            
            # 2. Test greet resource
            print("\n--- Testing greet resource ---")
            greet_response = await session.read_resource("resource://greet")
            greet_content = greet_response.contents[0].text
            print(f"Response: {greet_content}")
            
            # 3. Test farewell resource
            print("\n--- Testing farewell resource ---")
            farewell_response = await session.read_resource("resource://farewell")
            farewell_content = farewell_response.contents[0].text
            print(f"Response: {farewell_content}")
            
            # 4. Test invalid resource
            print("\n--- Testing invalid resource ---")
            try:
                await session.read_resource("resource://invalid")
                print("❌ Should have thrown an error!")
            except Exception as e:
                print(f"✓ Correctly handled invalid resource: {type(e).__name__}")


async def test_math_server():
    """Test Math Server and its resources"""
    print("\n" + "="*60)
    print("TESTING MATH SERVER")
    print("="*60)
    
    server_params = StdioServerParameters(
        command="python",
        args=["math_mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # 1. Connection test
            print("\n✓ Client is connected to Math MCP Server")
            
            # 2. Test addition resource
            print("\n--- Testing addition resource ---")
            addition_response = await session.read_resource("resource://addition")
            addition_content = addition_response.contents[0].text
            print(f"Response: {addition_content}")
            
            # 3. Test multiplication resource
            print("\n--- Testing multiplication resource ---")
            multiplication_response = await session.read_resource("resource://multiplication")
            multiplication_content = multiplication_response.contents[0].text
            print(f"Response: {multiplication_content}")
            
            # 4. Test invalid resource
            print("\n--- Testing invalid resource ---")
            try:
                await session.read_resource("resource://division")
                print("❌ Should have thrown an error!")
            except Exception as e:
                print(f"✓ Correctly handled invalid resource: {type(e).__name__}")


async def main():
    """Main function to run all tests"""
    print("\n" + "█"*60)
    print("█" + " "*18 + "MCP SERVERS TEST SUITE" + " "*19 + "█")
    print("█"*60)
    
    # Test both servers
    await test_greeting_server()
    await test_math_server()
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED")
    print("="*60 + "\n")


if __name__ == "__main__":
    # Asenkron main fonksiyonunu çalıştır
    asyncio.run(main())
