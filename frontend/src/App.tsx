import {useState} from "react";

function App() {
    const [expression, setExpression] = useState("");

    function handleButtonClick(value: string) {
        setExpression(expression + value)
    }

    function handleClear() {
        setExpression("")
    }


    return (
        <div>
            <h1>Scientific Calculator</h1>
            <div className="calculator-display">
                {expression || "0" }
            </div>
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
            </div>
        </div>

    );
}

export default App;
