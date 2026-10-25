import {useState} from "react";

function App() {
    const [expression, setExpression] = useState("");
    const [error, setError] = useState("");

    function handleButtonClick(value: string) {
        setExpression(expression + value);
        setError("");
    }

    function handleClear() {
        setExpression("");
        setError("");
    }

    function handleBackspace() {
        setExpression(expression.slice(0, -1))
        setError("")
    }

    async function handleCalculate(){
        try{
            setError("");

            const response = await fetch("http://localhost:8000/calculate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({expression: expression})
            });

            if(!response.ok){
                throw new Error("Calculation failed");
            }

            const data = await response.json();
            setExpression(String(data.result));
        
        } catch {
            setError("Invalid expression");

        }
    }

    return (
        <div>
            <h1>Scientific Calculator</h1>

            <div className="calculator-display">
                {expression || "0" }
            </div>

            {error && <p>{error}</p>}

            <div className="calculator-buttons">
                <button onClick={() => handleButtonClick("7")}>7</button>
                <button onClick={() => handleButtonClick("8")}>8</button>
                <button onClick={() => handleButtonClick("9")}>9</button>
                <button onClick={() => handleButtonClick("/")}>/</button>

                <button onClick={() => handleButtonClick("4")}>4</button>
                <button onClick={() => handleButtonClick("5")}>5</button>
                <button onClick={() => handleButtonClick("6")}>6</button>
                <button onClick={() => handleButtonClick("*")}>*</button>

                <button onClick={() => handleButtonClick("1")}>1</button>
                <button onClick={() => handleButtonClick("2")}>2</button>
                <button onClick={() => handleButtonClick("3")}>3</button>
                <button onClick={() => handleButtonClick("-")}>-</button>

                <button onClick={() => handleButtonClick("0")}>0</button>
                <button onClick={() => handleButtonClick(".")}>.</button>
                <button onClick={() => handleButtonClick("(")}>(</button>
                <button onClick={() => handleButtonClick(")")}>)</button>
                <button onClick={() => handleButtonClick("+")}>+</button>

                <button onClick={handleClear}>C</button>
                <button onClick={handleBackspace}>⌫</button>
                <button onClick={handleCalculate}>=</button>
            
            </div>
        </div>

    );
}

export default App;
