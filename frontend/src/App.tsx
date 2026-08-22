import {useEffect, useState} from "react";

function App() {
    const [message, setMessage] = useState("Loading...");

    useEffect(() => {
        fetch("http://localhost:8000/hello")
        .then((response) => response.json())
        .then((data) => {
            setMessage(data.message);
            });
    }, []);

    return (
        <div>
            <h1>Scientific Calculator</h1>
            <p>Backend says: {message}</p>
        </div>

    );
}

export default App;
