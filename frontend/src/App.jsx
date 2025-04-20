import {useEffect, useState} from 'react'
import './App.css'

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
            {news.map((item, index) => (
                <div key={index} className="newsCard card">
                    <div className="card-header">
                        {news[index]["source"]}
                    </div>
                    <div className="card-body container">
                        <h4 className="card-title">
                            <a href={news[index]["link"]}>{news[index]["title"]}</a>
                        </h4>
                        <div className="card-text row">
                            <div className={"col-6"}>
                                Published: {news[index]["published"][1]}/{news[index]["published"][2]}/{news[index]["published"][0]}
                            </div>
                            <div className={"col-6"}>
                                Updated: {news[index]["updated"][1]}/{news[index]["updated"][2]}/{news[index]["updated"][0]}
                            </div>
                        </div>
                    </div>
                </div>
            ))}
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

    return (<>
        <div id="weatherCard" className={"card container"}>
            <div className={"card-body row"}>
                <div className={"col-7"}>
                    <h5 className={"card-title"}>Weather</h5>
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
    </>)
}
function Events(){
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
    return(
        <div id = "eventContainer" className="card">
            <div className="card-header">
                Today's Events
            </div>
            <ul className="list-group list-group-flush">
                {events.map((item, index) => (
                    <li key={index} className="list-group-item">
                        {events[index]["title"]}
                        <br />
                        <span>@{events[index]["location"]}</span>
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
                    <div className={"col-12 col-md-8 order-1 order-md-0"}>
                        {/*NEWS*/}
                        <News/>
                    </div>
                    <div className={"col-8 col-md-4 order-0 order-md-1"}>
                        {/*WEATHER*/}
                        <Weather/>

                        {/*EVENTS*/}
                        <Events/>
                    </div>
                </div>
            </div>

        </>
    );
}


function App() {
    // const [count, setCount] = useState(0)
    // const [apiMessage, setApiMessage] = useState('')
    // const [isLoading, setIsLoading] = useState(true)
    // const [error, setError] = useState(null)
    //
    // useEffect(() => {
    //     // Use relative URL - this will be proxied by Vite
    //     fetch('/api/hello')
    //         .then(response => {
    //             if (!response.ok) {
    //                 throw new Error(`HTTP error! Status: ${response.status}`);
    //             }
    //             return response.json();
    //         })
    //         .then(data => {
    //             setApiMessage(data.message);
    //             setIsLoading(false);
    //         })
    //         .catch(error => {
    //             console.error('Error fetching from API:', error);
    //             setError(error.message);
    //             setIsLoading(false);
    //         });
    // }, []); // Empty dependency array means this runs once on mount

    return (
        <>
            <div className={"bg"}></div>
            <div id="titleContainer">
                <div className={"container"}>
                    <div id="ChatTitle" className={"element"}>
                        <a>What's Up</a>
                        <br/>
                        UTD?
                    </div>
                </div>
            </div>
            <div id="feedContainer">
                <Page/>
            </div>
            <div className={"mb-3 container input"}>
                      <textarea className="form-control" id="chatInput" rows="3">
                        Type Here
                      </textarea>
            </div>

            {/*<div id="Chatbox" className={"mt-auto"}>*/}
            {/*    <div className="container">*/}
            {/*        <div id="ChatTitle" className={""}>*/}
            {/*                What's Up*/}
            {/*                <br/>*/}
            {/*                UTD?*/}
            {/*        </div>*/}
            {/*        <div id = "chatspace" className="align-items-end"></div>*/}
            {/*    </div>*/}
            {/*</div>*/}
            {/*    <Chatbox/>*/}
            {/*<Page/>*/}


            {/*    <div>*/}
            {/*        <a href="https://vite.dev" target="_blank">*/}
            {/*            <img src={viteLogo} className="logo" alt="Vite logo"/>*/}
            {/*        </a>*/}
            {/*        <a href="https://react.dev" target="_blank">*/}
            {/*            <img src={reactLogo} className="logo react" alt="React logo"/>*/}
            {/*        </a>*/}
            {/*    </div>*/}
            {/*    <h1>Vite + React</h1>*/}

            {/*    /!* API Response Display *!/*/}
            {/*    <div className="api-section">*/}
            {/*        <h2>API Response</h2>*/}
            {/*        {isLoading ? (*/}
            {/*            <p>Loading...</p>*/}
            {/*        ) : error ? (*/}
            {/*            <p style={{color: 'red'}}>{error}</p>*/}
            {/*        ) : (*/}
            {/*            <p><strong>{apiMessage}</strong></p>*/}
            {/*        )}*/}
            {/*    </div>*/}

            {/*    <div className="card">*/}
            {/*        <button onClick={() => setCount((count) => count + 1)}>*/}
            {/*            count is {count}*/}
            {/*        </button>*/}
            {/*        <p>*/}
            {/*            Edit <code>src/App.jsx</code> and save to test HMR*/}
            {/*        </p>*/}
            {/*    </div>*/}
            {/*    <p className="read-the-docs">*/}
            {/*        Click on the Vite and React logos to learn more*/}
            {/*    </p>*/}
        </>
    )
}

export default App