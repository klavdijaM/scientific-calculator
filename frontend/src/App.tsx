import {useState} from "react";

function App() {
    const [expression, setExpression] = useState("");

    return (
        <div>
            <h1>Scientific Calculator</h1>
            <div className="calculator-display">
                {expression || "0" }
            </div>
        </div>

    );
}

export default App;
