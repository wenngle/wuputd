# What's up, UTD?
A one-stop shop for all your campus info.

## Inspiration
We thought about the issues we face as UTD students and how we struggle to find relevant information on a day-to-day basis. First and foremost, we created something not just for ourselves, but to improve the lives of all UTD students.

## What it does
What's up, UTD is a chat bot that you can ask questions about courses, events, weather, and more: anything pertaining to UTD. It integrates with the Nebula Labs API to ground its answers with facts, so it always has the most accurate information. The website also contains a dashboard with information about weather, news, and events, so that you can see "what's up" at a glance.

## How we built it
The app consists of a server built with Flask to aggregate data from numerous sources, including the Nebula Labs API, Google Gemini AI, news feeds and weather. We created an agentic chatbot by using Gemini's "automatic function calling" mechanism in Google's `genai` SDK. The user interface is built with react to dynamically respond to the user's input and fetch data in real time.

## Challenges we ran into
We struggled displaying all of the disparate data on the frontend in a useful manner. It was challenging to create a layout that showcased the chat interface as well as the dashboard UI.

It was also challenging to integrate so many tools together. We struggled to narrow our scope to create something useful for students.

## Accomplishments that we're proud of
We're proud of creating a LLM-powered chatbot that has the ability to answer queries about UTD with information grounded in Nebula Labs data.

## What we learned
- LLM tool use / function calling
- API integrations
- Crafting intuitive interfaces

## What's next for What's up UTD?
This project could be extended to support a mobile app, generate a personalized email briefing, store user information (course assignment calendar), and more!