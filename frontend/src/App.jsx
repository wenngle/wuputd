import React, {useEffect, useRef, useState} from 'react'
import './App.css'
import {v4 as uuidv4} from "uuid";

function News() {
    let [news, setNews] = useState("loading")
    useEffect(() => {
        fetch("/api/news").then(res => res.json()).then((data) => {
            setNews(data);
        })
    }, []) // Empty dependency array added here

    if (news === "loading") {
        return (
            <></>
        );
    }


    return (
        <div id="newsContainer">
            <div id={"newsTitle"}><h4>News </h4><br/></div>
            <div className="newsFeed">
                {news.map((item, index) => (
                    <div key={index} className="newsCard card">
                        <div className="card-header">
                            {item["source"]}
                        </div>
                        <div className="card-body container">
                            <h5 className="card-title">
                                <a href={item["link"]}>{item["title"]}</a>
                            </h5>
                            <div className="card-text row">
                                <div className={"col-6"}>
                                    Published: {item["published"][1]}/{item["published"][2]}/{item["published"][0]}
                                </div>
                                <div className={"col-6"}>
                                    Updated: {item["updated"][1]}/{item["updated"][2]}/{item["updated"][0]}
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

function Weather() {
    let [weather, setWeather] = useState("loading")

    useEffect(() => {
        fetch("/api/campus-weather").then(res => res.json()).then((data) => {
            setWeather(data);
        })
    }, []) // Empty dependency array added here

    return <div id="weatherCard" className={"card container"}>
        <div className={"card-body row"}>
            <div className={"col-7"}>
                <h5 className={"card-title"}>Weather &nbsp;&nbsp;</h5>
                <h6 className={"card-subtitle mb-2 text-body-secondary"}>
                    Wind: {weather["wind_speed"]}mph {weather["wind_direction"]}
                </h6>
            </div>
            <div className={"col-5"}>
                <h5 className={"card-title"}>
                    {weather["temp"]}ºF {weather["icon"]}
                </h5>
                <h6 className={"card-subtitle mb-2 text-body-secondary"}>
                    Rain: {weather["rain_percent"]}%
                </h6>
            </div>
        </div>
    </div>
}

function ConvertDateToTime(isoDateString) {
    try {
        const date = new Date(isoDateString);
        return date.toLocaleTimeString([], {hour: "2-digit", minute: "2-digit"}).toLowerCase();
    } catch (error) {
        console.error("Error converting date:", error);
        return "Invalid Date";
    }
}

function Events() {
    let [events, setEvents] = useState("loading")
    useEffect(() => {
        fetch("/api/campus-events/today").then(res => res.json()).then((data) => {
            setEvents(data);
        })
    }, []) // Empty dependency array added here

    if (events === "loading") {
        return (
            <></>
        );
    }
    return (
        <div id="eventContainer" className="card">
            <div className="card-header">
                Happening Today
            </div>
            <ul className="list-group list-group-flush">
                {[...events]
                    // Use the standard numerical comparison for dates
                    .sort((a, b) => new Date(a["start_date"]) - new Date(b["start_date"]))
                    // Map over the resulting sorted array
                    .map((item, index) => ( // Use 'item' directly in the map callback
                        <li key={index} className="list-group-item">
                            {item["title"]} {/* Use item instead of events[index] */}
                            <br/>
                            {ConvertDateToTime(item["start_date"])}-{ConvertDateToTime(item["end_date"])}
                            <a href={"https://locator.utdallas.edu/" + item["location"].replace(" ", "_")}>@{item["location"]}</a>
                        </li>
                    ))}
            </ul>
        </div>
    );
}

function Page() {
    return (
        <>
            <div id="mainpage" className={"container"}>
                <div className={"row"}>
                    <div id="rightFeed" className={"smContainer col-8 col-md-4 order-0 order-md-1"}>
                        {/*WEATHER*/}
                        <Weather/>

                        {/*EVENTS*/}
                        <Events/>
                    </div>
                    <div className={"smContainer col-12 col-md-8 order-1 order-md-0"}>
                        {/*NEWS*/}
                        <News/>
                    </div>
                </div>
            </div>

        </>
    );
}


function GetMessage() {
    // State management
    const [messages, setMessages] = useState([]);
    const [inputMessage, setInputMessage] = useState('');
    const [userId, setUserId] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const messagesEndRef = useRef(null);

    // Initialize userId on component mount (reset on refresh)
    useEffect(() => {
        setUserId(uuidv4());
    }, []);


    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const scrollToBottom = () => {
        messagesEndRef.current?.scroll();
    };


    // Handle sending a message
    const handleSendMessage = async (e) => {
        e.preventDefault();

        if (!inputMessage.trim()) return;

        // Add user message to chat
        const userMessage = {
            id: Date.now(),
            sender: 'user',
            content: inputMessage,
            timestamp: new Date().toISOString()
        };

        setMessages(prevMessages => [...prevMessages, userMessage]);
        setInputMessage('');
        setIsLoading(true);

        try {
            // Call the API
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user_id: userId,
                    message: inputMessage
                })
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }

            const data = await response.json();

            // Add bot response to chat
            const botMessage = {
                id: Date.now() + 1,
                sender: 'bot',
                content: data.response || "Sorry, I couldn't process your request.",
                timestamp: new Date().toISOString()
            };

            setMessages(prevMessages => [...prevMessages, botMessage]);
        } catch (error) {
            console.error('Error sending message:', error);

            // Add error message to chat
            const errorMessage = {
                id: Date.now() + 1,
                sender: 'bot',
                content: "Sorry, there was an error processing your message. Please try again.",
                timestamp: new Date().toISOString()
            };

            setMessages(prevMessages => [...prevMessages, errorMessage]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-screen max-w-2xl mx-auto">
            {/* Messages container */}
            <div className="flex-grow overflow-y-auto space-y-4 mb-4">
                {messages.length === 0 ? (<></>
                ) : (
                    messages.map(message => (
                        <div
                            key={message.id}
                            className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
                        >
                            <div
                                className={`max-w-xs md:max-w-md lg:max-w-lg px-4 py-2 rounded-lg ${
                                    message.sender === 'user'
                                        ? 'bg-blue-500 text-white rounded-br-none'
                                        : 'bg-gray-200 text-gray-800 rounded-bl-none'
                                }`}
                            >
                                <div dangerouslySetInnerHTML={{__html:message.content}}></div>
                                <p className="text-xs opacity-75 mt-1">
                                    {new Date(message.timestamp).toLocaleTimeString()}
                                </p>
                            </div>
                        </div>
                    ))
                )}
                {isLoading && (
                    <div className="flex justify-start">
                        <div className="px-4 py-2">
                            <div className="flex space-x-2">
                                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce"></div>
                                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce delay-75"></div>
                                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce delay-150"></div>
                            </div>
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef}/>
            </div>

            {/* Input form */}
            <form onSubmit={handleSendMessage} className="flex space-x-2 p-4 rounded-b-lg">
                <input
                    type="text"
                    value={inputMessage}
                    onChange={e => setInputMessage(e.target.value)}
                    placeholder="Type your message..."
                    className="flex-grow p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    disabled={isLoading}
                />
                <button
                    type="submit"
                    disabled={isLoading || !inputMessage.trim()}
                    className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-blue-300"
                >
                    Send
                </button>
            </form>
        </div>
    );

}

function App() {
    // const [apiMessage, setApiMessage] = useState('')
    // const [isLoading, setIsLoading] = useState(true)
    // const [error, setError] = useState(null)
    //
    // const theme = window.matchMedia('(prefers-color-scheme: dark)');
    const theme = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
    useEffect(() => {
        document.documentElement.setAttribute('data-bs-theme', theme ? "dark" : "light");
        localStorage.setItem('theme', theme); // Store theme preference
    }, [theme]);

    return (
        <>
            <div className={"bg"}></div>
            <div className={"bgIMG"}></div>
            <div id="titleContainer">
                <div id = "titleContainerIn" className={"container"}>
                    <div id="ChatTitle" className={"element"}>
                        <a>What's Up</a>
                        <br/>
                        UTD?
                    </div>
                    <div id={"chatbot"}>
                        <GetMessage/>
                    </div>
                </div>
            </div>
            <div id="feedContainer">
                <Page/>
            </div>


        </>
    )
}

export default App