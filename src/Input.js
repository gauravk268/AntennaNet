import React, { useRef, useState } from "react";
import { Form, Button, Alert } from "react-bootstrap";

import "./input.css";

const Input = () => {
  const heightRef = useRef();
  const radiusRef = useRef();
  const freqRef = useRef();

  const [error, setError] = useState("false");
  const [result, setResult] = useState("false");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const inputValue = {
      height: heightRef.current.value,
      radius: radiusRef.current.value,
      freq: freqRef.current.value,
    };

    if (
      inputValue.height === "" ||
      inputValue.radius === "" ||
      inputValue.freq === ""
    ) {
      setError("None of the valus can be empty.");
      return;
    }

    if (inputValue.height < 9 || inputValue.height > 11) {
      setError("Height value out of range.");
      return;
    }

    if (inputValue.radius < 7 || inputValue.radius > 9) {
      setError("Radius value out of range.");
      return;
    }

    if (inputValue.freq < 4 || inputValue.freq > 12) {
      setError("Frequency value out of range.");
      return;
    }

    const data = {
      exp: [inputValue.height, inputValue.radius, inputValue.freq],
    };

    await fetch("http://localhost:5000/api", {
      method: "POST",
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        setResult(data);
      })
      .catch((error) => {
        console.error("Error:", error);
        setError(error);
      });
  };

  const resetError = (e) => {
    setError("false");
  };

  return (
    <div className="input-form">
      <h1>Enter required values to predict S11 in db</h1>
      <Form>
        {error !== "false" && <Alert variant={"danger"}>{error}</Alert>}
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Height [mm] * (min: 9mm, max: 11mm)</Form.Label>
          <Form.Control
            type="text"
            placeholder="Height [mm]"
            ref={heightRef}
            onChange={resetError}
            required
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Radius [mm] * (min: 7mm, max: 9mm)</Form.Label>
          <Form.Control
            type="text"
            placeholder="Radius [mm]"
            ref={radiusRef}
            onChange={resetError}
            required
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Frequency [GHz] * (min: 4GHz, max: 12GHz)</Form.Label>
          <Form.Control
            type="text"
            placeholder="Frequency [GHz]"
            ref={freqRef}
            onChange={resetError}
            required
          />
        </Form.Group>

        {result === "false" ? (
          <Button variant="primary" type="submit" onClick={handleSubmit}>
            Submit
          </Button>
        ) : (
          <Alert variant={"success"}>
            S11 db value of antenna for given values is: {result}
          </Alert>
        )}
      </Form>
    </div>
  );
};

export default Input;
