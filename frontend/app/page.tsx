"use client";

import { useState } from "react";
import { QueryInterface } from "./components/QueryInterface";
import { ResultsPanel } from "./components/ResultsPanel";

interface ApiResponse {
  data: Record<string, unknown>[];
  sql: string;
  question?: string;
  error?: string;
  type?: string;
}

export default function Home() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState<ApiResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const askQuestion = async (questionText: string) => {
    setLoading(true);
    setResponse(null);

    try {
      const res = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: questionText }),
      });

      if (!res.ok) {
        throw new Error("Failed to fetch data");
      }

      const data = await res.json();
      setResponse({ ...data, question: questionText });
    } catch (error) {
      console.error("Error fetching data:", error);
      setResponse({
        data: [],
        sql: "",
        question: questionText,
        error: "Network error: Unable to connect to the server",
        type: "network_error",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen">
      <div className="max-w-4xl mx-auto px-4 py-8 mt-10">
        <div className="text-center my-8">
          <h2 className="text-3xl font-bold mb-4">
            What would you like to know?
          </h2>
          <p className="text-gray-600 text-lg">
            Ask questions about your data and get instant visualizations
          </p>
        </div>

        <div className="mb-8">
          <QueryInterface
            onSubmit={askQuestion}
            isLoading={loading}
            question={question}
            onQuestionChange={setQuestion}
          />
        </div>

        {response && <ResultsPanel response={response} />}
      </div>
    </div>
  );
}
