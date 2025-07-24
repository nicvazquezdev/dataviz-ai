"use client";

import { useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const canChart = (data: any[]): boolean => {
  if (!data || data.length === 0) return false;
  const keys = Object.keys(data[0]);
  if (keys.length !== 2) return false;

  const secondKey = keys[1];
  return typeof data[0][secondKey] === "number";
};

export default function Home() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    setLoading(true);
    setResponse(null);

    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    const data = await res.json();
    setResponse(data);
    setLoading(false);
  };

  return (
    <main className="max-w-xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Mini Nivii</h1>
      <textarea
        className="w-full border p-2 mb-2"
        rows={3}
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded"
        onClick={askQuestion}
        disabled={loading}
      >
        {loading ? "Loading..." : "Ask"}
      </button>
      {response?.data?.length > 0 && (
        <div className="mt-6">
          <h2 className="font-semibold">SQL:</h2>
          <pre className="bg-gray-100 p-2 text-sm">{response.sql}</pre>

          <h2 className="font-semibold mt-4 mb-2">Result:</h2>

          {canChart(response.data) ? (
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={response.data}>
                <XAxis dataKey={Object.keys(response.data[0])[0]} />
                <YAxis />
                <Tooltip />
                <Bar
                  dataKey={Object.keys(response.data[0])[1]}
                  fill="#3b82f6"
                />
              </BarChart>
            </ResponsiveContainer>
          ) : (
            <table className="w-full text-sm mt-2 border">
              <thead>
                <tr>
                  {Object.keys(response.data[0]).map((col) => (
                    <th key={col} className="border p-2 text-left bg-gray-100">
                      {col}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {response.data.map((row, idx) => (
                  <tr key={idx}>
                    {Object.values(row).map((val, i) => (
                      <td key={i} className="border p-2">
                        {val}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      )}

      {response?.data?.length === 0 && (
        <p className="mt-4 text-red-600">No results found.</p>
      )}

      {response?.error && (
        <p className="mt-4 text-red-600">Error: {response.error}</p>
      )}
    </main>
  );
}
