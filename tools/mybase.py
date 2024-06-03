from crewai_tools import BaseTool

from models.case import Case

class MyBase(BaseTool):
    name: str = "Name of my tool"
    description: str = "What this tool does. It's vital for effective utilization."
    mycase: Case
    
    def _run(self, argument: str) -> str:
        # Your tool's logic here
        execute(self, argument)
        save(self)
        return "Tool's result"
    def execute(self, argument: str):
        # Execute the tool's logic
        pass
    def save(self, ):
        # Save the tool's state
        pass