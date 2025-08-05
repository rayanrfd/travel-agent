# Travel Agent AI 🧳✈️

> **Status: 🚧 In Development**

## Project Goal

The goal of this project is to create an intelligent AI-powered travel agent that can:

- **Parse natural language travel queries** and extract key information (origin, destination, dates, preferences)
- **Provide comprehensive travel plans** based on user preferences such as:
  - Cost optimization (cheapest routes)
  - Comfort preferences (most comfortable options)
  - Speed requirements (fastest travel)
  - Trip type (one-way vs round-trip)
- **Integrate real-time data** for accurate planning and recommendations
- **Generate structured, actionable travel itineraries**

## Current Progress

### ✅ Completed
- Basic project structure setup
- Integration with Google Gemini AI for natural language processing
- Timezone detection and calculation functionality
- Tool-based function calling for enhanced AI capabilities
- Initial travel information extraction from user queries

### 🔄 Currently Working On
- Structured output parsing and data modeling
- Improving AI prompt engineering for better travel plan extraction
- Debugging API integration issues with Gemini AI

### 📋 Planned Features
- [ ] Flight search and booking integration
- [ ] Hotel and accommodation recommendations
- [ ] Travel preference handling (budget, comfort, speed)
- [ ] Multi-city itinerary support
- [ ] Weather information integration
- [ ] Cost estimation and comparison
- [ ] Real-time pricing data
- [ ] Trip optimization algorithms
- [ ] User preference learning and personalization

## Tech Stack

- **AI Model**: Google Gemini 2.0 Flash
- **Language**: Python
- **Key Libraries**: OpenAI SDK, python-dotenv, pytz
- **Architecture**: Tool-based AI agent with function calling

## Project Structure

```
travel-agent/
├── main.py                    # Main application logic
├── schemas/
│   └── UserPlan.py           # Data models for travel plans
├── tools/
│   └── get_date_and_time.py  # Timezone utilities
├── .env                      # Environment configuration
└── README.md                 # This file
```

## Development Status

This is an early-stage project with the core AI integration in place. The foundation for natural language processing and structured data extraction is working, and development is ongoing to add comprehensive travel planning capabilities.
