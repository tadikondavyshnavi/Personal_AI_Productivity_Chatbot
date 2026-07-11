from llm.llm_service import ask_llm
from llm.prompt_templates import task_planner


def generate_task_plan(goal: str) -> str:
    """
    Generate AI task plan
    """

    if not goal.strip():
        return "Please enter your goal."

    prompt = task_planner(goal)

    return ask_llm(prompt)



