'use client'
import { useState } from "react";

type Sentiment = {
  polarity: number;
  subjectivity: number;
};

type Result = {
  summary: string;
  sentiment: Sentiment;
};

export default function Home() {
  const [url, setUrl] = useState<string>(""); 
  const [result, setResult] = useState<Result | null>(null); 
  const [loading, setLoading] = useState<boolean>(false); 
  const [error, setError] = useState<string | null>(null); 

  const handleSummarize = async () => {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const response = await fetch("http://127.0.0.1:5000/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      const data: Result = await response.json();
      setResult(data);
    } catch (err: unknown) {
      setError("Failed to fetch the summary or sentiment analysis. Please try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <div className="max-w-3xl w-full bg-white p-8 rounded-lg shadow-md">
        <h1 className="text-2xl font-bold text-gray-800 mb-4">
          News Summarization & Sentiment Analysis
        </h1>
        <div className="flex gap-4 mb-6">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter news article URL"
            className="flex-grow px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleSummarize}
            className={`px-6 py-2 bg-blue-500 text-white rounded-md ${
              loading ? "opacity-50 cursor-not-allowed" : "hover:bg-blue-600"
            }`}
            disabled={loading}
          >
            {loading ? "Loading..." : "Summarize"}
          </button>
        </div>
        {error && <p className="text-red-500 font-medium">{error}</p>}
        {result && (
          <div className="mt-6">
            <h2 className="text-xl font-semibold text-gray-700">Summary:</h2>
            <p className="text-gray-800">{result.summary}</p>
            <h2 className="text-xl font-semibold text-gray-700 mt-4">
              Sentiment analysis:
            </h2>
            <p className="text-gray-800">Polarity: {result.sentiment.polarity}</p>
            <p className="text-gray-800">
              Subjectivity analysis: {result.sentiment.subjectivity}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
