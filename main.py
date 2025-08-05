from openai import OpenAI
from schemas.schemas import TravelPlan
from tools.get_date_and_time import get_date_and_time_tool, get_date_and_time
from dotenv import load_dotenv
import os
import json
import datetime

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

client = OpenAI(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1",
)

def extract_travel_plan(prompt):
    messages=[
            {"role": "system", "content": "Extract the event information."},
            {"role": "user", "content": f"{prompt}, Answer in JSON"},
        ],
    
    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=messages,
        # response_format={
        #         "type": "json_schema",
        #         "schema": TravelPlan.model_json_schema(),
        #     },
        tools=[get_date_and_time_tool],
        tool_choice="required",
        )

    tool_call = completion.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)

    result = get_date_and_time(**args)

    messages.append(completion.choices[0].message)  # append model's function call message
    messages.append({                               # append result message
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    })

    completion_2 = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        tools=get_date_and_time_tool,
        response_format={
                "type": "json_schema",
                "schema": TravelPlan.model_json_schema(),
            },
    )

    return completion_2.choices[0].message.content


def main():
    print(extract_travel_plan("I want to travel from Paris to the lake Balkhash in Kazakstan in two days for a week."))


if __name__ == "__main__":
    main()
