"""
Optional NeMo Agent Toolkit registration sketch.

Use this after installing NeMo Agent Toolkit. The exact package structure may change
with NAT versions, so keep the standalone CLI as the reliable MVP and then register
these functions as NAT tools.
"""

from pydantic import BaseModel, Field

# Example imports based on NAT docs:
# from nat.cli.register_workflow import register_function
# from nat.builder.builder import Builder
# from nat.builder.function_info import FunctionInfo

from app.canvas_tool import canvas_context
from app.website_tool import search_menlo_website

class MenloWebsiteInput(BaseModel):
    query: str = Field(description="Question to search against Menlo public website pages")

class CanvasInput(BaseModel):
    query: str = Field(description="Question about assignments or announcements")

async def menlo_website_tool(input: MenloWebsiteInput) -> str:
    return search_menlo_website(input.query)

async def canvas_readonly_tool(input: CanvasInput) -> str:
    return canvas_context()

# Pseudocode registration:
#
# @register_function(config_type=MenloWebsiteToolConfig)
# async def register_menlo_website_tool(config, builder: Builder):
#     yield FunctionInfo.from_fn(
#         menlo_website_tool,
#         description="Searches indexed Menlo public website pages."
#     )
#
# @register_function(config_type=CanvasReadonlyToolConfig)
# async def register_canvas_readonly_tool(config, builder: Builder):
#     yield FunctionInfo.from_fn(
#         canvas_readonly_tool,
#         description="Reads Canvas assignments and announcements only."
#     )
