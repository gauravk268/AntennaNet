import React, { useRef, useState } from "react";
import { Form, Button, Alert } from "react-bootstrap";

import "./input.css";

const Input = () => {
  const heightRef = useRef();
  const radiusRef = useRef();
  const freqRef = useRef();

  const [error, setError] = useState("false");

  const handleSubmit = (e) => {
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
    }

    console.log(inputValue);
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
          <Form.Label>Height [mm]*</Form.Label>
          <Form.Control
            type="text"
            placeholder="Height [mm]"
            ref={heightRef}
            onChange={resetError}
            required
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Radius [mm]*</Form.Label>
          <Form.Control
            type="text"
            placeholder="Radius [mm]"
            ref={radiusRef}
            onChange={resetError}
            required
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Frequency [GHz]*</Form.Label>
          <Form.Control
            type="text"
            placeholder="Frequency [GHz]"
            ref={freqRef}
            onChange={resetError}
            required
          />
        </Form.Group>

        <Button variant="primary" type="submit" onClick={handleSubmit}>
          Submit
        </Button>
      </Form>
    </div>
  );
};

export default Input;
