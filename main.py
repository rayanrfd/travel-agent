from openai import OpenAI
from schemas.UserPlan import TravelPlan
from tools.get_date_and_time import get_date_and_time_tool, get_date_and_time
from dotenv import load_dotenv
import os
import json
import datetime

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def extract_travel_plan(prompt):

    messages=[
            {"role": "system", "content": "Extract the travel information in a JSON format."},
            {"role": "user", "content": f"{prompt}"},
        ]
    
    
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=messages,
        tools=get_date_and_time_tool,
        tool_choice="required",
    )
    
    tool_call = response.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)

    time_info = get_date_and_time(args["departure_tz"], args["destination_tz"])

    messages.append(response.choices[0].message)  # append model's function call message
    messages.append({                               # append result message
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": f"User time: {time_info['user_time']}, Destination time: {time_info['destination_time']}"
    })

    completion = client.beta.chat.completions.parse(
        model="gemini-2.0-flash",
        messages=messages,
        response_format=TravelPlan,
    )

    return completion.choices[0].message.parsed.origin

def main():
    print(extract_travel_plan("I want to travel from Paris to the lake Balkhash in Kazakstan in two days for a week."))


if __name__ == "__main__":
    main()

